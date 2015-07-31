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
    var cinemas = $('#cinemas');
    var show_times = $('#show-times');
    var plans = $('#plans');
    var current_step = step1;
    var current_select = cinemas;

    $('#cinemas .item').on('click', function () {
        step1.removeClass('active').addClass('done');
        step1.next().removeClass('active').addClass('done');
        step2.next().addClass('active');
        step2.addClass('active');
        current_step = step2;
        cinemas.fadeOut(function () {
            show_times.fadeIn();
            current_select = show_times;
        });
    });

    $('.show-time').on('click', function(){
        step2.removeClass('active').addClass('done');
        step2.next().removeClass('active').addClass('done');
        step3.addClass('active');
        current_step = step3;
        show_times.fadeOut(function () {
            plans.fadeIn();
            current_select = plans;
        });
    });

    step1.on('click', function () {
        if(current_step == step1)
            return false;
        current_step = step1;
        current_select.fadeOut(function () {
            cinemas.fadeIn();
            current_select = cinemas;
        });

        step1.removeClass('done').addClass('active');
        step1.next().removeClass('done').addClass('active');

        step2.removeClass('done').removeClass('active');
        step2.next().removeClass('done').removeClass('active');

        step3.removeClass('active');
    });

    step2.on('click', function () {
        if(current_step == step2 || current_step == step1)
            return false;
        current_step = step2;
        current_select.fadeOut(function () {
            show_times.fadeIn();
            current_select = show_times;
        });

        step2.removeClass('done').addClass('active');
        step2.next().removeClass('done').addClass('active');

        step3.removeClass('active');
    });

    $('.seat').on('click', function () {
        if($(this).hasClass('free-seat'))
            $(this).fadeOut(function () {
                $(this).css('background-image', 'url("http://127.0.0.1:8000/static/img/seat_selected.png")')
                    .removeClass('free-seat').addClass('selected-seat').fadeIn();
            });
        else
            if($(this).hasClass('selected-seat'))
                $(this).fadeOut(function () {
                    $(this).css('background-image', 'url("http://127.0.0.1:8000/static/img/seat_available.png")')
                        .removeClass('selected-seat').addClass('free-seat').fadeIn();
                });
    });

    $('.seat').each(function () {
        $(this).attr({ 'data-toggle': 'tooltip',
            'data-placement': 'top',
            'data-template': '<div class="tooltip" role="tooltip"><div class="tooltip-arrow"></div><div style="font-family:BYekan" class="tooltip-inner"></div></div>"',
            'title': ''});
        if($(this).hasClass('no-internet-sale'))
            $(this).attr('data-original-title', 'فروش اینترنتی ندارد');
        else
            if($(this).hasClass('sold-seat'))
                $(this).attr('data-original-title', 'فروخته شده');
        $(this).tooltip();
    });
    var counter = 1;
    $('#plan-azadi').children().each(function () {
        if($(this).hasClass('free-seat')){
            $(this).attr('data-original-title', counter);
            counter++;
        }
        else
            if($(this).hasClass('sold-seat'))
                counter++;
            else
                if($(this).hasClass('seat-row'))
                    counter = 1;
    });
})(jQuery);