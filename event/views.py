# -*- coding: utf-8 -*-
import os
import datetime
from operator import itemgetter
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from bilityab.views import make_event_type_list1, make_event_type_list, get_type
from event.models import Categories, Sport, Movie, Concert, EventRating, EventOrganizer
from ticket.models import *


def events(request):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated(),
        'event_type_list': make_event_type_list1(Event.objects.all())

    })


def add_event(request):
    if request.user.is_authenticated() and request.user.is_organizer:
        if request.is_ajax():
            # insert event and it's additional information to database
            if (request.POST.get('event-title', '') != "" and request.POST.get('event-description',
                                                                               '') != "" and request.POST.get(
                    'event-type', '') != "" and request.POST.get('event-address', '') != ""):
                cat_id = int(request.POST.get('event-type', ''))
                category = Categories.objects.get(pk=cat_id)
                event = Event.objects.create(title=request.POST.get('event-title', ''),
                                             description=request.POST.get('event-description', ''),
                                             category=category, address=request.POST.get('event-address', ''))
                event.event_organizers.add(EventOrganizer.objects.get(user=request.user))
                if request.POST.get('event-home-team', '') != "" and request.POST.get('event-away-team', '') != "":
                    Sport(
                        event_id=event.id,
                        away_team=request.POST.get('event-home-team', ''),
                        home_team=request.POST.get('event-away-team', '')
                    ).save()
                elif (request.POST.get('event-director', '') != "" and request.POST.get('event-actors',
                                                                                        '') != "" and request.POST.get(
                        'event-year', '') != "" and request.POST.get('event-story-summary', '') != ""):
                    Movie(
                        event_id=event.id,
                        director=request.POST.get('event-director', ''),
                        actors=request.POST.get('event-actors', ''),
                        year=request.POST.get('event-year', ''),
                        story_summary=request.POST.get('event-story-summary', '')
                    ).save()
                elif (request.POST.get('event-vocalist', '') != "" and request.POST.get('event-musicians',
                                                                                        '') != "" and request.POST.get(
                        'event-music-group', '') != ""):
                    Concert(
                        event_id=event.id,
                        group_name=request.POST.get('event-music-group', ''),
                        vocalist=request.POST.get('event-vocalist', ''),
                        musicians=request.POST.get('event-musicians', '')
                    ).save()

                # redirect to site homepage
                return HttpResponse(1)
            else:
                # raise exception to user
                return HttpResponse(0)
        else:
            # add new event template for organizer
            return render(request, 'add-event.html', {
                'logged_in': request.user.is_authenticated(),
                'categories': Categories.objects.all().exclude(parent_id=0)
            })
    else:
        return HttpResponseRedirect('/')


def apply_event(request):
    if request.method == 'post':
        print('')


def edit_event(request, event_id):
    if request.user.is_authenticated() and request.user.is_organizer:
        if request.is_ajax():
            # insert event and it's additional information to database
            # if (request.POST.get('event-title', '') != "" and request.POST.get('event-description',
            #                                                                    '') != "" and request.POST.get(
            #         'event-type', '') != "" and request.POST.get('event-capacity', '') != "" and request.POST.get(
            #         'event-address', '') != ""):
            cat_id = int(request.POST.get('event-type', ''))
            category = Categories.objects.get(pk=cat_id)

            event = Event.objects.get(id = event_id)
            event.title = request.POST.get('event-title', '')
            event.description = request.POST.get('event-description', '')
            event.category = category
            event.address = request.POST.get('event-address', '')
            event.save()
            # event = Event.objects.create(title=request.POST.get('event-title', ''),
            #                                  description=request.POST.get('event-description', ''),
            #                                  category=category, capacity=int(request.POST.get('event-capacity', '')),
            #                                  address=request.POST.get('event-address', ''))
            # event.event_organizers.add(EventOrganizer.objects.get(user=request.user))
            if request.POST.get('event-home-team', '') != "" and request.POST.get('event-away-team', '') != "":
                sport_event = Sport.objects.get(event_id=event.id)
                sport_event.home_team = request.POST.get('event-home-team', '')
                sport_event.away_team = request.POST.get('event-away-team', '')
                sport_event.save()

                return HttpResponse(1)
            elif request.POST.get('event-director', '') != "" and request.POST.get('event-actors',
                                                                                        '') != "" and request.POST.get(
                        'event-year', '') != "" and request.POST.get('event-story-summary', '') != "":
                movie_event = Movie.objects.get(event_id=event_id)
                movie_event.director = request.POST.get('event-director', '')
                movie_event.actors = request.POST.get('event-actors', '')
                movie_event.year = int(request.POST.get('event-year', ''))
                movie_event.story_summary = request.POST.get('event-story-summary', '')
                movie_event.save()
                return HttpResponse(1)
            elif request.POST.get('event-vocalist', '') != "" and request.POST.get('event-musicians', '') != "" and request.POST.get('event-music-group', '') != "":
                concert_event = Concert.objects.get(event_id=event.id)
                concert_event.group_name = request.POST.get('event-music-group', ''),
                concert_event.vocalist = request.POST.get('event-vocalist', ''),
                concert_event.musicians = request.POST.get('event-musicians', '')
                concert_event.save()

                return HttpResponse(1)
            else:
                print("error")
                # raise exception to user
                return HttpResponse(0)
        else:
            event_type = get_type(Event.objects.get(id=event_id).id)
            if event_type == "music":
                return render(request, 'edit-event.html', {
                    'logged_in': request.user.is_authenticated(),
                    'categories': Categories.objects.all(),
                    'event': Event.objects.get(id=event_id),
                    'type': event_type,
                    'concert': Concert.objects.get(event_id=event_id),
                })
            elif event_type == "cinema":
                return render(request, 'edit-event.html', {
                    'logged_in': request.user.is_authenticated(),
                    'categories': Categories.objects.all(),
                    'event': Event.objects.get(id=event_id),
                    'type': event_type,
                    'movie': Movie.objects.get(event_id=event_id)
                })
            elif event_type == "sport":
                return render(request, 'edit-event.html', {
                    'logged_in': request.user.is_authenticated(),
                    'categories': Categories.objects.all(),
                    'event': Event.objects.get(id=event_id),
                    'type': event_type,
                    'sport': Sport.objects.get(event_id=event_id),
                })
            else:
                return render(request, 'edit-event.html', {
                    'logged_in': request.user.is_authenticated(),
                    'categories': Categories.objects.all(),
                    'event': Event.objects.get(id=event_id),
                    'type': event_type,
                })
    else:
        return HttpResponseRedirect('/')


def all_sport(request):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated()

    })


def all_music(request, event_id):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated()

    })


def all_cinema(request, event_id):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated()

    })


def all_tourism(request, event_id):
    return render(request, 'all-events.html', {
        'logged_in': request.user.is_authenticated()

    })


def sport(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        show_time = event.show_times.all()[0]
        event_date_time = datetime.datetime.combine(show_time.date, show_time.from_time)
    except Event.DoesNotExist:
        raise Http404("sport event does not exist!")
    return render(request, 'sport.html', {
        'event': event,
        'show_time': show_time,
        'remaining_time': int((event_date_time - datetime.datetime.now()).total_seconds() * 1000),
        'logged_in': request.user.is_authenticated(),
        'organizer': event.event_organizers.all()[0],
        'price': event.position_prices.all()[0],
        'user': request.user
    })


def tourism(request, event_id):
    return render(request, 'tourism.html', {
        'logged_in': request.user.is_authenticated()

    })


def cinema(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        event_rates = event.rates.all()
        can_rate = request.user.is_authenticated()
        rates_average = 0
        num_of_votes = len(event_rates)
        if num_of_votes:
            rates_sum = 0
            for rate in event_rates:
                rates_sum += rate.rate
                can_rate = can_rate and not (rate.user.id == request.user.id)
            rates_average = rates_sum / num_of_votes
        show_dates = []
        for i in event.show_times.all():
            added = False
            for j in show_dates:
                if i.date == j['date']:
                    j['org_id'] += '-' + str(i.organizer.id)
                    j['id'] += '-' + str(i.id)
                    added = True
            if not added:
                show_dates.append({'date': i.date, 'org_id': ''+str(i.organizer.id), 'id': ''+str(i.id)})
    except Event.DoesNotExist:
        raise Http404('cinema event does not exist!')
    return render(request, 'cinema.html', {
        'logged_in': request.user.is_authenticated(),
        'event': event,
        'num_of_votes': num_of_votes,
        'rates_average_percent': rates_average * 20,
        'can_rate': can_rate,
        'show_dates': show_dates,
        'user': request.user
    })


def music(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        event_organizer = event.event_organizers.all()[0]
        return render(request, 'music.html', {
            'logged_in': request.user.is_authenticated(),
            'event': event,
            'organizer': event_organizer,
            'show_time': event.show_times.all()[0]
        })
    except Event.DoesNotExist:
        return Http404('event not found!')


def all_organizer(request):
    return render(request, 'all-organizer.html', {
        'logged_in': request.user.is_authenticated()

    })


def organizer(request, organizer_id):
    return render(request, 'organizer.html', {
        'organizer': EventOrganizer.objects.get(id=organizer_id),
        'organizer_events': make_event_type_list1(Event.objects.filter(event_organizers__id=organizer_id)),
        'logged_in': request.user.is_authenticated()
    })


def report(request):
    return render(request, 'report.html', {'logged_in': request.user.is_authenticated()
    })


def rate_event(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if 'rate' in request.POST:
                rate = int(request.POST['rate'])
                if rate > 5 or rate < 0:
                    print('sada;dw')
                    return HttpResponseForbidden('invalid rate')
                event_id = request.POST['event_id']
                try:
                    event = Event.objects.get(pk=event_id)
                    EventRating.objects.get(event=event, user=request.user)
                    return HttpResponseForbidden('already rated')
                except Event.DoesNotExist:
                    return HttpResponseForbidden('invalid event id')
                except EventRating.DoesNotExist:
                    EventRating.objects.create(event=event, user=request.user, rate=rate)
                    return HttpResponse('success')
        else:
            return HttpResponseForbidden('post required')
    else:
        return HttpResponseForbidden('login required')


def get_sold_seats(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = Event.objects.get(pk=event_id)
        tickets = []
        for i in event.show_times.all()[0].tickets.all():
            tickets.extend(i.positions.all())
        return HttpResponse(tickets)
    else:
        return HttpResponseForbidden('post required')


def delete_event(request, event_id):
    Event.objects.get(id=event_id).delete()
    return HttpResponseRedirect('/events')


def buy_seats(request):
    if request.method == 'POST':
        seats = request.POST.get('seats')
        cinema_ticket = seats[0] == 'C'
        quantity = request.POST.get('quantity')
        show_time_id = request.POST.get('show_time_id')
        price = request.POST.get('price')
        show_time = Showtime.objects.get(pk=show_time_id)
        show_time.capacity -= 1
        show_time.save()
        ticket = PurchasedTicket.objects.create(user=request.user, quantity=int(quantity),
                                                purchased_date=datetime.datetime.now(),
                                                price=float(int(price)),
                                                receipt='123456789', showtime=show_time)
        if not cinema_ticket:
            register_seats(show_time.organizer.id, seats, ticket)
        else:
            seats = seats.split('C')
            for seat in seats:
                if seat:
                    info = seat.split(',')
                    row = int(info[0])
                    column = int(info[1])
                    TicketPosition.objects.create(ticket=ticket, row=row, column=column)
        return HttpResponseRedirect('/ticket/'+str(request.user.id)+'/'+str(ticket.id)+'/')
    else:
        return HttpResponseForbidden('post required')


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def register_seats(map_id, seats, ticket):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sections = []
    rows = []
    columns = []
    seats_num = 0
    seats = seats.split('A')
    for seat in seats:
        if seat:
            info = seat.split(',')
            section = int(info[0])
            sections.append(section)
            row = int(info[1])
            rows.append(row)
            column = int(info[2])
            columns.append(column)
            TicketPosition.objects.create(ticket=ticket, section=section, row=row, column=column)
            seats_num += 1
    with open(os.path.join(base_dir, "static/maps/templates/"+str(map_id)+'.html'), "r+") as sample:
        data = sample.readlines()
        sample.seek(0)
        sample.truncate()
        seat_stack = Stack()
        target_row = 0
        target_column = 0
        target_row_detected = False
        target_column_detected = False
        for line in data:
            if seat_stack.size() and not target_row and not target_column:
                target_seat = seat_stack.pop()
                target_row = target_seat['row']
                target_column = target_seat['column']
                print(target_column)
            if 'class="clear"' in line:
                target_row_detected = False
            if target_row and '>'+str(target_row)+'<' in line:
                target_row_detected = True
            if target_column and target_row_detected and 'col="'+str(target_column)+'"' in line:
                target_column_detected = True
            if target_row_detected and target_column_detected:
                target_column_detected = False
                target_row = 0
                target_column = 0
                line = line.replace('free-seat', 'sold-seat')
            elif 'class="section"' in line:
                first = line.index('id="')
                second = line.index('"', first+5)
                section_id = int(line[first+4:second])
                temp_rows_columns = []
                for i in range(0, len(sections)):
                    if sections[i] == section_id:
                        temp_rows_columns.append({'row': rows[i], 'column': columns[i]})
                for row_column in sorted(temp_rows_columns, key=itemgetter('row', 'column'), reverse=True):
                    seat_stack.push(row_column)
            sample.write(line)
        sample.close()


def categories(request):
    return render(request, 'all_categories.html', {
        'logged_in': request.user.is_authenticated(),
        'categories': Categories.objects.filter(parent_id=0),
        'sub_categories': Categories.objects.all().exclude(parent_id=0)
    })


def add_category(request):
    if request.user.is_authenticated() and request.user.is_organizer:
        if request.is_ajax():
            if request.POST.get('event-type', '') != "":
                # insert event and it's additional information to database
                if request.POST.get('sub-category-title', '') != "":
                    event = Categories(title=request.POST.get('sub-category-title', ''),
                                parent_id=request.POST.get('event-type', '')
                    ).save()

                    # redirect to site homepage
                    return HttpResponse(1)
                else:
                    # raise exception to user
                    print("raise1")
                    return HttpResponse(0)
            else:
                # insert event and it's additional information to database
                if request.POST.get('category-title', '') != "":
                    event = Categories(title=request.POST.get('category-title', ''),
                                  parent_id=0
                    ).save()

                    # redirect to site homepage
                    return HttpResponse(1)
                else:
                    print("raiese2")
                    # raise exception to user
                    return HttpResponse(0)
        else:
            # add new event template for organizer
            return render(request, 'add_category.html', {
                'categories': Categories.objects.filter(parent_id=0),
                'logged_in': request.user.is_authenticated(),
            })
    else:
        return HttpResponseRedirect('/')


def delete_category(request, category_id):
    Categories.objects.get(id=category_id).delete()
    return HttpResponseRedirect('/categories')


def edit_category(request, category_id):

    if request.user.is_authenticated() and request.user.is_organizer:
        if request.is_ajax():
                # insert event and it's additional information to database
                if request.POST.get('category-title', '') != "":
                    category = Categories.objects.get(id=category_id)
                    category.title = request.POST.get('category-title', '')
                    category.save()

                    return HttpResponse(1)
                else:
                    # raise exception to user
                    return HttpResponse(0)
        else:
            category = Categories.objects.get(id=category_id)
            return render(request, 'edit_category.html', {
                'category': category,
                'sub_categories':Categories.objects.filter(parent_id=category.id)
            })
    else:
        return HttpResponseRedirect('/')




