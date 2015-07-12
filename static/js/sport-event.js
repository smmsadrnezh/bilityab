(function($){
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
    function decrease_time(){
        if(!stop)
            setTimeout(decrease_time, 1000);
        if(r_seconds_int == 0)
        {
            if(r_minutes_int == 0)
            {
                if(r_hours_int == 0)
                {
                    if(r_days_int == 0)
                    {
                        stop = true;
                    }
                    else
                    {
                        r_seconds.text(r_seconds_int = 59);
                        r_minutes.text(r_minutes_int = 59);
                        r_hours.text(r_hours_int = 23);
                        r_days.text(--r_days_int);
                    }
                }
                else
                {
                    r_seconds.text(r_seconds_int = 59);
                    r_minutes.text(r_minutes_int = 59);
                    r_hours.text(--r_hours_int);
                }
            }
            else
            {
                r_seconds.text(r_seconds_int = 59);
                r_minutes.text(--r_minutes_int);
            }
        }
        else
        {
            r_seconds.text(--r_seconds_int);
        }
    }
    $('#remaining-time').countDown();
    var body_height = parseFloat($('body').css('height'));
    var header_plus_info_height = parseFloat($('#top-header').css('height')) + parseFloat($('#ticket-info').css('height')) + parseFloat($('#ticket-info').css('margin-top'))*2;
    $('#seat-select').css('height', body_height - header_plus_info_height + 'px');
    $('[data-toggle="tooltip"]').tooltip();
    var fixture_ticket = $('#ticket');
    var user_comments = $('#comments');
    var more_info = $('#more-info');
    var active_panel = fixture_ticket;
    $('#for-ticket').on('click', function () {
        if(fixture_ticket.css('display') != 'block'){
            active_panel.fadeOut(function () {
                fixture_ticket.fadeIn();
                active_panel = fixture_ticket;
            });
        }
    });
    $('#for-comments').on('click', function () {
        if(user_comments.css('display') != 'block'){
            active_panel.fadeOut(function () {
                user_comments.fadeIn();
                active_panel = user_comments;
            });
        }
    });
    $('#for-more-info').on('click', function () {
        if(more_info.css('display') != 'block'){
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
})(jQuery);