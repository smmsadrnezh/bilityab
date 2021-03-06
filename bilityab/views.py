# -*- coding: utf-8 -*-
from operator import itemgetter

from django.db.models import Sum
from django.shortcuts import render

from event.models import Event, Categories, Showtime, PositionPrice
from promotion.models import Promotion


def get_category(event):
    category = Categories.objects.get(id=event.category_id)
    if Categories.objects.get(id=category.parent_id).title == "سینمایی"   :
        return Categories.objects.get(id=category.parent_id)
    return Categories.objects.get(id=event.category_id)


def get_type(event_id):
    sub_category = Categories.objects.get(id=Event.objects.get(id=event_id).category_id)
    category = Categories.objects.get(id=sub_category.parent_id).title
    return {
        'ورزشی': 'sport',
        'سینمایی': 'cinema',
        'موسیقی': 'music',
        'گردشگری': 'tourism'
    }[category]


def make_event_type_list(event_list):
    event_type_list = []
    for event in event_list:
        category = get_type(event.id)
        event_type_list.append((event, category))

    return event_type_list


def make_event_type_list1(event_list):
    event_type_list = []
    for event in event_list:
        category = get_type(event.id)
        organizer = event.event_organizers.all()[0]
        dates = Showtime.objects.filter(event=event)
        try:
            position_price = PositionPrice.objects.get(organizer_id=organizer, event_id=event)
        except PositionPrice.DoesNotExist:
            position_price = PositionPrice.objects.filter(organizer_id=1)[0]
        show_times = Showtime.objects.filter(event_id=event.id)
        max_promotion = 0
        for show_time in show_times:
            promotions = Promotion.objects.filter(showtime_id=show_time.id)
            for promotion in promotions:
                if promotion.discount > max_promotion:
                    max_promotion = promotion.discount
        total_capacity = 0
        for show_time in event.show_times.all():
            total_capacity += show_time.capacity
        if dates:
            date = get_nearest_date(dates)
            event_type_list.append((event, category, organizer, date, total_capacity, position_price.price, max_promotion, get_category(event)))
        else:
            event_type_list.append((event, category, organizer, total_capacity, position_price.price, max_promotion,get_category(event)))
    return event_type_list


def get_nearest_date(dates):
    if dates:
        result = dates[0]
        for date in dates:
            if date.date < result.date:
                result = date
        return result


def get_show_times_events(show_times):
    result = []
    for show_time in show_times:
        result.append(show_time.event)
    return result


def get_best_seller_events():
    event_price = []
    result = []
    events = Event.objects.all()
    for event in events:
        bought_tickets = 0
        for show_time in event.show_times.all():
            for ticket in show_time.tickets.all():
                bought_tickets += ticket.price
        event_price.append({'event': event, 'price': bought_tickets})
    for temp in sorted(event_price, key=itemgetter('price'), reverse=True):
        result.append(temp['event'])
    return result[:3]


def home(request, *args):
    going_recovery = 0
    categories = Categories.objects.filter(parent_id=0).exclude(title="ورزشی").exclude(title="سینمایی").exclude(title="گردشگری").exclude(title="موسیقی")
    category_subcategories = []
    for category in categories:
        sub_categories = Categories.objects.filter(parent_id=category.id)
        category_subcategories.append((category, sub_categories))
    if args:
        going_recovery = args[0]
    return render(request, 'home.html', {
        'going_recovery': going_recovery,
        'bestEvents': make_event_type_list1(Event.objects.annotate(rate=Sum('rates')).order_by('-rates')[:3]),
        'nearestEvents': make_event_type_list1(get_show_times_events(Showtime.objects.all().order_by('date')[:3])),
        'newestEvents': make_event_type_list1(Event.objects.all().order_by('-created_at')[:3]),
        'actionMovies': make_event_type_list1(Event.objects.filter(category__title='اکشن')),
        'dramaticMovies': make_event_type_list1(Event.objects.filter(category__title='درام')),
        'comicMovies': make_event_type_list1(Event.objects.filter(category__title='کمدی')),
        'volleyballEvents': make_event_type_list1(Event.objects.filter(category__title='والیبال')),
        'footballEvents': make_event_type_list1(Event.objects.filter(category__title='فوتبال')),
        'basketballEvents': make_event_type_list1(Event.objects.filter(category__title='بسکتبال')),
        'wrestleEvents': make_event_type_list1(Event.objects.filter(category__title='کشتی')),
        'zooEvents': make_event_type_list1(Event.objects.filter(category__title='باغ وحش')),
        'amusementEvents': make_event_type_list1(Event.objects.filter(category__title='شهر بازی')),
        'circusEvents': make_event_type_list1(Event.objects.filter(category__title='سیرک')),
        'traditionalMusic': make_event_type_list1(Event.objects.filter(category__title='سنتی')),
        'popMusic': make_event_type_list1(Event.objects.filter(category__title='پاپ')),
        'bestSellerEvents': make_event_type_list1(get_best_seller_events()),
        'mainCategories': category_subcategories,
        'pageTitle': " - سامانهٔ جامع خرید و فروش بلیط",
    })


def terms(request):
    return render(request, 'terms.html', {
        'pageTitle': " - شرایط و ضوابط",
    })


def FAQ(request):
    return render(request, 'FAQ.html', {
        'pageTitle': " - سوالات متداول",
    })


def Help(request):
    return render(request, 'help.html', {
        'pageTitle': " - راهنمای سامانه",
    })


def about(request):
    return render(request, 'about.html', {
        'pageTitle': " - درباره",
    })


def contact(request):
    return render(request, 'contact-us.html', {
        'pageTitle': " - تماس با ما",
    })
