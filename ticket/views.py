from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden

from ticket.models import PurchasedTicket
from event.models import Event, Showtime, Categories, EventOrganizer
from ticket.models import TicketPosition
from bilityab.views import get_type
from datetime import datetime
import calendar


def get_category(event):
    category = Categories.objects.get(id=event.category_id)
    if Categories.objects.get(id=category.parent_id).title == "سینمایی"  :
        return Categories.objects.get(id=category.parent_id)
    return Categories.objects.get(id=event.category_id)


def buy(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        seats = request.POST.get('seats')
        quantity = request.POST.get('quantity')
        show_time_id = request.POST.get('show_time_id')
        return render(request, 'buy.html', {
            'pageTitle': " - خرید بلیط",
            'price': price,
            'show_time_id': show_time_id,
            'seats': seats,
            'quantity': quantity
        })
    else:
        return HttpResponseForbidden()


def ticket(request, user_id, purchased_id):
    if int(user_id) == request.user.id:
        # find ticket and related event
        ticket = PurchasedTicket.objects.get(id=purchased_id)
        showtime = Showtime.objects.get(id=ticket.showtime_id)
        organizer = EventOrganizer.objects.get(id=showtime.organizer_id)
        event = Event.objects.get(id=showtime.event_id)
        postitions = TicketPosition.objects.filter(ticket_id=purchased_id)

        # make list from event, event category and ticket
        ticket_event_type_list = []
        ticket_event_type_list.append((ticket, event, get_type(event.id), showtime, postitions, organizer))

        return render(request, 'ticket.html', {
            'pageTitle': " - بلیط",
            'ticket_event_type_list': ticket_event_type_list
        })
    else:
        return HttpResponseRedirect('/')


def num_to_month(date):

    if date == 13:
        date = 12

    return{
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }[date]


def add_months(sourcedate,months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12)
    month = month % 12 + 1
    day = calendar.monthrange(year, month)[1]
    return datetime(year, month, day)


def chart(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/')
    else:
        start = request.GET.get('start-date', None)
        end = request.GET.get('end-date', None)

        tickets = PurchasedTicket.objects.all().order_by('purchased_date')

        send_start_date = datetime.now()
        send_end_date = datetime.now()

        if tickets.last() is not None:
            send_start_date = tickets.first().purchased_date
            send_end_date = tickets.last().purchased_date

        if start is not None:
            send_start_date = datetime.strptime(start, "%Y-%m-%d")
        if end is not None:
            send_end_date = datetime.strptime(end, "%Y-%m-%d")

        months = []
        sales = []
        flag = True
        temp = send_start_date
        counter = 0

        while flag:
            if counter == 0:
                next_month = datetime(temp.year, temp.month, calendar.monthrange(temp.year, temp.month)[1])
            else:
                next_month = add_months(temp, 1)
            if next_month > send_end_date:
                next_month = send_end_date
                flag = False
            if counter == 0:
                months.append({"start": temp, "end": next_month, "str": num_to_month(temp.month)})
            else:
                months.append({"start": temp, "end": next_month, "str": num_to_month(temp.month+1)})
            counter += 1
            temp = next_month

        counter = 0

        for i in range(len(months)):
            sales.append(0)

        for ticket in tickets:
            if counter < len(months):
                flag = True
                while flag and counter < len(months):
                    if ticket.purchased_date >= months[counter]['start'] and ticket.purchased_date < months[counter]['end']:
                        flag = False
                        sales[counter] += ticket.price
                    else:
                        counter += 1
            else:
                break

        return render(
            request,
            'ticket-report.html',
            {
                'pageTitle': " - گزارش فروش ها",
                'start_date_day': send_start_date.day,
                'start_date_month': send_start_date.month,
                'start_date_year': send_start_date.year,
                'end_date_day': send_end_date.day,
                'end_date_month': send_end_date.month,
                'end_date_year': send_end_date.year,
                'sales': sales,
                'months': months
            })


def all_ticket(request, user_id):
    if int(user_id) == request.user.id:
        start = request.GET.get('start-date', None)
        end = request.GET.get('end-date', None)

        tickets_events = []
        tickets = PurchasedTicket.objects.filter(user_id=request.user.id).order_by('-purchased_date')

        send_start_date = datetime.now()
        send_end_date = datetime.now()

        if tickets.last() is not None:
            send_start_date = tickets.last().purchased_date
            send_end_date = tickets.first().purchased_date

        input_start_date = None
        input_end_date = None

        if start is not None:
            input_start_date = datetime.strptime(start, "%Y-%m-%d")
            send_start_date = input_start_date
        if end is not None:
            input_end_date = datetime.strptime(end, "%Y-%m-%d")
            send_end_date = input_end_date

        for ticket in tickets:
            show_time = Showtime.objects.get(id=ticket.showtime_id)
            event = Event.objects.get(id=show_time.event_id)
            flag = True
            if input_start_date is not None and ticket.purchased_date < input_start_date:
                flag = False
            if input_end_date is not None and ticket.purchased_date > input_end_date:
                flag = False
            if flag:
                tickets_events.append((ticket, event, get_category(event)))
        return render(request, 'all-ticket.html', {
            'pageTitle': " - تمام بلیط‌ها",
            'tickets': tickets_events,
            'start_date_day': send_start_date.day,
            'start_date_month': send_start_date.month,
            'start_date_year': send_start_date.year,
            'end_date_day': send_end_date.day,
            'end_date_month': send_end_date.month,
            'end_date_year': send_end_date.year,
        })
    else:
        return HttpResponseRedirect('/')
