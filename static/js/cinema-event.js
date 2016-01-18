$('#film-info').css('height', parseFloat($('#film-trailer').css('height')));

$('#film-info > div:last-of-type').css('height', parseFloat($('#film-info').css('height')) - parseFloat($('#film-info > div:first-of-type').css('height')));

$(window).load(function () {

    $(document).ajaxSend(function (event, xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        function sameOrigin(url) {
            // url could be relative or scheme relative or absolute
            var host = document.location.host; // host + port
            var protocol = document.location.protocol;
            var sr_origin = '//' + host;
            var origin = protocol + sr_origin;
            // Allow absolute or scheme relative URLs to same origin
            return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                    // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
        }

        function safeMethod(method) {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    });

    var seat_progress = $('#seat-select .progress');
    var step1 = seat_progress.find('div:nth-of-type(1)');
    var step2 = seat_progress.find('div:nth-of-type(2)');
    var step3 = seat_progress.find('div:nth-of-type(3)');
    var step4 = seat_progress.find('div:nth-of-type(4)');
    var dates = $('#dates');
    var current_step = step1;
    var current_select = [dates];
    var organizer_ids = [];
    var show_time_ids = [];
    var selected_organizer_id = $('#ticket').attr('organizer_id');
    var selected_show_time = $('#ticket').attr('show_time_id');
    var selected_discount = 0;
    if($('#ticket').attr('discount'))
        selected_discount = parseInt($('#ticket').attr('discount'));
    var selected_cinemas = [];
    var selected_show_times = [];
    var bought_tickets = $('#bought-tickets');
    var roll_back_seats = [];

    $.fn.find_prev_element = function ($class) {
        var result = null;
        var help = $(this);
        var column = 0;
        for (var i = 0; i < 100; i++) {
            help = help.prev();
            if (!help.hasClass('disabled-seat'))
                column++;
            if (help.hasClass($class)) {
                result = help;
                break;
            }
        }
        return [result, column];
    };

    var music_page = false;

    if (selected_show_time)
        music_page = true;

    if (music_page)
        set_sold_seats();

    function set_sold_seats() {
        var tickets = bought_tickets.find('div[show-time-id="' + selected_show_time + '"][organizer-id="' + selected_organizer_id + '"]');
        var seats = tickets.text().split('/');
        var row, column, temp;
        var map = $('.map[organizer-id="' + selected_organizer_id + '"]');
        for (var i = 0; i < seats.length; i++) {
            if (parseInt(seats[i])) {
                row = seats[i].split(',')[0];
                column = parseInt(seats[i].split(',')[1]);
                temp = map.find('.seat-row.' + row);
                for (var j = 1; j <= column;) {
                    temp = temp.next();
                    if (!temp.hasClass('disabled-seat'))
                        j++;
                }
                temp.removeClass('free-seat').addClass('sold-seat');
                roll_back_seats.push(temp);
            }
        }
    }

    function roll_back_changes() {
        for (var i in roll_back_seats)
            roll_back_seats[i].removeClass('sold-seat').addClass('free-seat');
        roll_back_seats = [];
    }

    $('.add-to-cart').on('click', function () {
        var seats = '', seat, quantity = 0;
        $(this).closest('.map').find('.selected-seat').each(function () {
            quantity++;
            var row_column = $(this).find_prev_element('seat-row');
            var row = row_column[0].text();
            var column = row_column[1];
            seats += "C" + row + ',' + column + 'C';
        });
        var parent = $(this).parent();
        var actual_price = parseInt($(this).closest('.map').attr('price')) * quantity;
        parent.find('input[name="price"]').val(parseInt((actual_price*(100-parseInt(selected_discount)))/100));
        parent.find('input[name="show_time_id"]').val(selected_show_time);
        parent.find('input[name="quantity"]').val(quantity);
        parent.find('input[name="seats"]').val(seats);
    });
    $('.show-time-date').on('click', function () {
        step1.removeClass('active').addClass('done');
        step1.next().removeClass('active').addClass('done');
        step2.addClass('active').next().addClass('active');
        current_step = step2;
        var cinemas_id = $(this).attr('organizer-id').split('-');
        organizer_ids = $(this).attr('organizer-id').split('-');
        show_time_ids = $(this).attr('show-time-id').split('-');
        for (var i = 0; i < current_select.length; i++) {
            if (i == current_select.length - 1)
                current_select[i].fadeOut(function () {
                    current_select = [];
                    selected_cinemas = [];
                    var temp = null;
                    for (var j = 0; j < cinemas_id.length; j++) {
                        temp = $('.cinema[cinema-id="' + cinemas_id[j] + '"');
                        current_select.push(temp);
                        selected_cinemas.push(temp);
                        temp.css({
                            opacity: 0,
                            display: 'inline-block'
                        }).animate({opacity: 1}, 600);
                    }
                });
            else
                current_select[i].fadeOut();
        }
    });
    $('.cinema').on('click', function () {
        step2.removeClass('active').addClass('done');
        step2.next().removeClass('active').addClass('done');
        step3.addClass('active').next().addClass('active');
        current_step = step3;
        selected_organizer_id = $(this).attr('cinema-id');
        for (var j = 0; j < current_select.length; j++) {
            if (j == current_select.length - 1) {
                current_select[j].fadeOut(function () {
                    var temp = null;
                    current_select = [];
                    selected_show_times = [];
                    for (var i = 0; i < organizer_ids.length; i++) {
                        if (organizer_ids[i] == selected_organizer_id) {
                            temp = $('.show-time[time-id="' + show_time_ids[i] + '"');
                            selected_show_times.push(temp);
                            current_select.push(temp);
                            temp.css({
                                opacity: 0,
                                display: 'inline-block'
                            }).animate({opacity: 1}, 100);
                        }
                    }
                });
            }
            else
                current_select[j].fadeOut();
        }
    });
    $('.show-time').on('click', function () {

        if ($('body').attr('data-logged-in') != 'true') {
            toastr.info("برای خرید بلیط وارد حساب کاربری خود شوید.", "ورود به سامانه");
        }

        step3.removeClass('active').addClass('done');
        step3.next().removeClass('active').addClass('done');
        step4.addClass('active');
        current_step = step4;
        selected_show_time = $(this).attr('time-id');
        if($(this).attr('discount'))
            selected_discount = parseInt($(this).attr('discount'));
        for (var i = 0; i < current_select.length; i++) {
            if (i == current_select.length - 1) {
                current_select[i].fadeOut(function () {
                    current_select = [];
                    var temp = $('.map[organizer-id="' + selected_organizer_id + '"]');
                    set_map_prices(temp);
                    set_sold_seats();
                    temp.fadeIn();
                    current_select.push(temp);
                });
            }
            else
                current_select[i].fadeOut();
        }
    });

    step1.on('click', function () {
        if (current_step == step1)
            return false;
        roll_back_changes();
        current_step = step1;
        for (var i = 0; i < current_select.length; i++) {
            if (i == current_select.length - 1) {
                current_select[i].fadeOut(function () {
                    current_select = [];
                    current_select.push(dates);
                    dates.fadeIn();
                });
            }
            else
                current_select[i].fadeOut();
        }
        step1.removeClass('done').addClass('active').next().removeClass('done').addClass('active');
        step2.removeClass('done').removeClass('active').next().removeClass('done').removeClass('active');
        step3.removeClass('done').removeClass('active').next().removeClass('done').removeClass('active');
        step4.removeClass('active');
    });
    step2.on('click', function () {
        if (current_step == step2 || current_step == step1)
            return false;
        roll_back_changes();
        current_step = step2;
        for (var i = 0; i < current_select.length; i++) {
            if (i == current_select.length - 1) {
                current_select[i].fadeOut(function () {
                    current_select = [];
                    for (var j = 0; j < selected_cinemas.length; j++) {
                        current_select.push(selected_cinemas[j]);
                        selected_cinemas[j].fadeIn();
                    }
                });
            }
            else
                current_select[i].fadeOut();
        }
        step2.removeClass('done').addClass('active');
        step3.removeClass('active').removeClass('done').next().removeClass('done').removeClass('active');
        step4.removeClass('active');
    });
    step3.on('click', function () {
        if (current_step != step4)
            return false;
        roll_back_changes();
        current_step = step3;
        for (var i = 0; i < current_select.length; i++) {
            if (i == current_select.length - 1) {
                current_select[i].fadeOut(function () {
                    current_select = [];
                    for (var j = 0; j < selected_show_times.length; j++) {
                        current_select.push(selected_show_times[j]);
                        selected_show_times[j].fadeIn();
                    }
                });
            }
            else
                current_select[i].fadeOut();
        }
        step3.removeClass('done').addClass('active').next().removeClass('done').addClass('active');
        step4.removeClass('active');
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
    $('.map').each(function () {
        set_map_prices($(this));
    });

    function set_map_prices(map) {
        var counter = 1;
        var main_str = '';
        var price = map.attr('price');
        map.children().each(function () {
            if ($(this).hasClass('free-seat')) {
                main_str = 'صندلی ' + counter + '، ' + price + ' تومان';
                if(parseInt(selected_discount))
                    main_str += '/ با تخفیف' + parseInt((parseInt(price) * (100 - parseInt(selected_discount))) / 100) + 'تومان';
                $(this).attr('data-original-title', main_str);
                counter++;
            }
            else if ($(this).hasClass('sold-seat'))
                counter++;
            else if ($(this).hasClass('seat-row'))
                counter = 1;
        });
    }

    // user rating

    $('.star-ratings-sprite').mousemove(function (event) {
        if (!$(this).hasClass('not-rated'))
            return false;
        $(this).find('span').css('width', parseInt(((event.pageX - $(this).offset().left) / parseFloat($(this).css('width')) * 100) / 10) * 10 + 10 + '%');
    }).hover(function () {
    }, function () {
        if (!$(this).hasClass('not-rated'))
            return false;
        $(this).fadeOut(200, function () {
            $(this).find('span').css('width', $(this).attr('initial-rate')).end().fadeIn(200);
        });
    }).on('click', function () {
        if (!$(this).hasClass('not-rated')) {

            if ($('body').attr('data-logged-in') == 'true') {
                toastr.info("امتیاز شما به این رویداد قبلا ثبت شده است", "امتیازدهی");
            }
            else {
                toastr.error("برای ثبت امتیاز، وارد حساب کاربری خود شوید.", "امتیازدهی");
            }

            return false;
        }
        $(this).removeClass('not-rated');
        var user_rate = parseFloat($(this).find('span')[0].style.width);
        var initial_rate = parseFloat($(this).attr('initial-rate'));
        var num_of_voters = $(this).next();
        var num = parseInt(num_of_voters.find('span').text());
        num_of_voters.find('span').fadeOut(200, function () {
            $(this).text(num + 1).fadeIn(200);
        });
        $(this).find('span').css('width', (user_rate + initial_rate * num) / (num + 1) + '%');
        var event_id = $(this).closest('#ticket').attr('event_id');
        toastr.success("امتیازشما با موفقیت ثبت شد.", "امتیازدهی");
        $.ajax('/events/rate/', {
            type: 'POST', data: {
                rate: user_rate / 20, event_id: event_id
            }, dataType: 'json'
        })
            .done(function (data) {
            })
            .fail(function () {
            });

    });

    if ($('body').attr('data-logged-in') == 'true') {

    }
    else {

        toastr.info("برای خرید بلیط باید ابتدا وارد سامانه شوید.", "ورود به سامانه");

    }



});
