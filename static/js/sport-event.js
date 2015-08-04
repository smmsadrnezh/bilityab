(function ($) {
    var stop = false;
    var r_days = $('#day');
    var r_hours = $('#hour');
    var r_minutes = $('#minute');
    var r_seconds = $('#second');
    var r_days_int, r_hours_int, r_minutes_int, r_seconds_int;
    $.fn.countDown = function () {
        var time_difference = parseInt($(this).attr('time-difference-milli-seconds'));
        time_difference = Math.floor(time_difference / 1000); // remove milli-seconds
        r_days_int = Math.floor(time_difference / 86400);
        r_days.text(r_days_int);
        time_difference = time_difference % 86400;
        r_hours_int = Math.floor(time_difference / 3600);
        r_hours.text(r_hours_int);
        time_difference = time_difference % 3600;
        r_minutes_int = Math.floor(time_difference / 60);
        r_minutes.text(r_minutes_int);
        time_difference = time_difference % 60;
        r_seconds_int = Math.floor(time_difference);
        r_seconds.text(r_seconds_int);
        setTimeout(decrease_time, 1000);
    };
    function decrease_time() {
        if (!stop)
            setTimeout(decrease_time, 1000);
        if (r_seconds_int == 0) {
            if (r_minutes_int == 0) {
                if (r_hours_int == 0) {
                    if (r_days_int == 0) {
                        stop = true;
                    }
                    else {
                        r_seconds.text(r_seconds_int = 59);
                        r_minutes.text(r_minutes_int = 59);
                        r_hours.text(r_hours_int = 23);
                        r_days.text(--r_days_int);
                    }
                }
                else {
                    r_seconds.text(r_seconds_int = 59);
                    r_minutes.text(r_minutes_int = 59);
                    r_hours.text(--r_hours_int);
                }
            }
            else {
                r_seconds.text(r_seconds_int = 59);
                r_minutes.text(--r_minutes_int);
            }
        }
        else {
            r_seconds.text(--r_seconds_int);
        }
    }

    $('#remaining-time').countDown();
    $('[data-toggle="tooltip"]').tooltip();
    var fixture_ticket = $('#ticket');
    var user_comments = $('#comments');
    var more_info = $('#more-info');
    var active_panel = fixture_ticket;
    $('#for-ticket').on('click', function () {
        if (fixture_ticket.css('display') != 'block') {
            active_panel.fadeOut(function () {
                fixture_ticket.fadeIn();
                active_panel = fixture_ticket;
            });
        }
    });
    $('#for-comments').on('click', function () {
        if (user_comments.css('display') != 'block') {
            active_panel.fadeOut(function () {
                user_comments.fadeIn();
                active_panel = user_comments;
            });
        }
    });
    $('#for-more-info').on('click', function () {
        if (more_info.css('display') != 'block') {
            active_panel.fadeOut(function () {
                more_info.fadeIn();
                active_panel = more_info;
            });
        }
    });
    var your_comment = $('#your-comment');
    $('#submit-comment').on('click', function () {
        var comment = $('<div class="comment col col-md-12"><div class="col col-md-11">' +
        '<div class="name">کاربر ثبت نامی</div><div class="date">۲۵ خرداد ۱۳۹۴، ۲:۱۱ عصر</div>' +
        '<div class="text"></div></div><div class="col col-md-1 image"></div></div>');
        comment.find('.text').text(your_comment.find('textarea').val());
        comment.find('.image').css('background-image', your_comment.find('.image').css('background-image'));
        $('#comments').append(comment);
        your_comment.find('textarea').val('');
    });

    var seat_progress = $('#seat-select .progress');
    var step1 = seat_progress.find('div:nth-of-type(1)');
    var step2 = seat_progress.find('div:nth-of-type(2)');
    var step3 = seat_progress.find('div:nth-of-type(3)');
    var positions = $('#positions');
    var stations = $('#stations');
    var seat_maps = $('#seat-maps');
    var current_step = step1;
    var current_select = positions;
    var _href, _href2;

    step1.on('click', function () {
        if (current_step == step1)
            return false;
        current_step = step1;
        current_select.fadeOut(function () {
            positions.fadeIn();
            current_select = positions;
        });

        step1.removeClass('done').addClass('active');
        step1.next().removeClass('done').addClass('active');

        step2.removeClass('done').removeClass('active');
        step2.next().removeClass('done').removeClass('active');

        step3.removeClass('active');
    });

    step2.on('click', function () {
        if (current_step == step2 || current_step == step1)
            return false;
        current_step = step2;
        current_select.fadeOut(function () {
            $(_href).fadeIn();
            current_select = $(_href);
        });

        step2.removeClass('done').addClass('active');
        step2.next().removeClass('done').addClass('active');

        step3.removeClass('active');
    });

    $('.seat').on('click', function () {
        if ($(this).hasClass('free-seat'))
            $(this).fadeOut(function () {
                $(this).css('background-image', 'url("http://127.0.0.1:8000/static/img/seat_selected.png")')
                    .removeClass('free-seat').addClass('selected-seat').fadeIn();
            });
        else if ($(this).hasClass('selected-seat'))
            $(this).fadeOut(function () {
                $(this).css('background-image', 'url("http://127.0.0.1:8000/static/img/seat_available.png")')
                    .removeClass('selected-seat').addClass('free-seat').fadeIn();
            });
    });

    $('.seat').each(function () {
        $(this).attr({
            'data-toggle': 'tooltip',
            'data-placement': 'top',
            'data-template': '<div class="tooltip" role="tooltip"><div class="tooltip-arrow"></div><div style="font-family:BYekan" class="tooltip-inner"></div></div>"',
            'title': ''
        });
        if ($(this).hasClass('no-internet-sale'))
            $(this).attr('data-original-title', 'فروش اینترنتی ندارد');
        else if ($(this).hasClass('sold-seat'))
            $(this).attr('data-original-title', 'فروخته شده');
        $(this).tooltip();
    });

    var price = null;

    $('#seat-maps > div').each(function () {
        var counter = 1;
        $(this).children().each(function () {
            if ($(this).hasClass('free-seat')) {
                price = parseInt($(this).parent().attr('price'));
                $(this).attr('data-original-title', 'شماره '+counter+'  ،  '+parseInt($(this).parent().attr('price'))+' تومان');
                counter++;
            }
            else if ($(this).hasClass('sold-seat'))
                counter++;
            else if ($(this).hasClass('seat-row'))
                counter = 1;
        });
    });

    $('img[usemap]').maphilight({
        fill: true,
        fillColor: '000000',
        fillOpacity: 0.2,
        stroke: true,
        strokeColor: 'fff',
        strokeOpacity: 0,
        strokeWidth: 0.01,
        fade: true,
        alwaysOn: false,
        neverOn: false,
        groupBy: false,
        wrapClass: true,
        shadow: false,
        shadowX: 0,
        shadowY: 0,
        shadowRadius: 6,
        shadowColor: '000000',
        shadowOpacity: 0.8,
        shadowPosition: 'outside',
        shadowFrom: false
    });

    $('map').each(function () {
        var areas = $(this).find('area');
        areas.each(function () {
            $(this).on('click', function (e) {
                if (!$(this).hasClass('no-internet-sale')) {
                    var parent_id = $(this).parent().parent().attr('id');
                    var grand_pa_id = $(this).parent().parent().parent().attr('id');
                    if (parent_id == 'positions') {
                        step1.removeClass('active').addClass('done');
                        step1.next().removeClass('active').addClass('done');
                        step2.next().addClass('active');
                        step2.addClass('active');
                        current_step = step2;
                        _href = $(this).attr('href');
                        positions.fadeOut(function () {
                            $(_href).fadeIn();
                            current_select = $(_href);
                        });
                    }
                    else {
                        if (grand_pa_id == 'stations') {
                            step2.removeClass('active').addClass('done');
                            step2.next().removeClass('active').addClass('done');
                            step3.addClass('active');
                            current_step = step3;
                            _href2 = $(this).attr('href');
                            $(_href).fadeOut(function () {
                                $(_href2).fadeIn();
                                current_select = $(_href2);
                            });
                        }
                    }
                }
                return false;
            });
        });
    });

    function getCookie(name){
        var cooki=null;
        if(document.cookie && String(document.cookie)!=""){
            var cookies = document.cookie.split(';');
            for(var i=0;i<cookies.length;i++){
                var temp = cookies[i].trim();
                if(temp.substring(0,name.length+1) == (name + '=')){
                    cooki = decodeURIComponent(temp.substring(name.length +1));
                    break;
                }
            }
        }
        return cooki;
    }

    /* Ajax-Code */

    function send_ajax_request($url, $params, $callback){
        var request = new XMLHttpRequest();
        request.open('POST', $url, true);
        request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        request.onreadystatechange = function () {
            if(request.readyState == 4 && request.status == 200){
                $callback(request.responseText);
            }
        };
        request.send($params);
    }

    function getIndicesOf(searchStr, str, caseSensitive) {
        var startIndex = 0, searchStrLen = searchStr.length;
        var index, indices = [];
        if (!caseSensitive) {
            str = str.toLowerCase();
            searchStr = searchStr.toLowerCase();
        }
        while ((index = str.indexOf(searchStr, startIndex)) > -1) {
            indices.push(index);
            startIndex = index + searchStrLen;
        }
        return indices;
    }

    function set_sold_seats(data) {
        var indexes = getIndicesOf("section", data, false);
        var column, seat, info, seat_str;
        for(var i = 0 ; i < indexes.length ; i++){
            if(i != indexes.length-1)
                seat_str = data.substring(indexes[i], indexes[i+1]);
            else
                seat_str = data.substring(indexes[i]);
            info = seat_str.split(' ');
            seat = $('#'+info[1]).find('.seat-row.'+info[3]);
            column = parseInt(info[5]);
            for(var j = 1 ; j <= column ; ) {
                seat = seat.next();
                if(seat.hasClass('free-seat') || seat.hasClass('sold-seat'))
                    j++;
            }
            seat.removeClass('free-seat').addClass('sold-seat');
        }
    }
    send_ajax_request('/events/sold_seats/', 'event_id='+$('#ticket').attr('event_id'), set_sold_seats);

    $.fn.find_prev_element = function ($class) {
        var result = null;
        var help = $(this);
        var column = 0;
        for(var i = 0 ; i < 100 ; i++){
            help = help.prev();
            if(!help.hasClass('disabled-seat'))
                column++;
            if(help.hasClass($class)) {
                result = help;
                break;
            }
        }
        return [result, column];
    };

    $('#seat-maps .add-to-cart').on('click', function () {
        var seats = '', seat, quantity = 0;
        $(this).parent().parent().find('.selected-seat').each(function () {
            quantity++;
            var section = $(this).parent().attr('id');
            var row_column = $(this).find_prev_element('seat-row');
            var row = row_column[0].text();
            var column = row_column[1];
            var seat = "A"+section+','+row+','+column+'A';
            seats += seat;
        });
        $('#price').val(price);
        $('#show_time_id').val($('#ticket').attr('show_time'));
        $('#quantity').val(quantity);
        $('#seats').val(seats);
    });

})(jQuery);