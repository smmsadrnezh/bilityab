$('#film-info').css('height', parseFloat($('#film-trailer').css('height')));

$('#film-info > div:last-of-type').css('height', parseFloat($('#film-info').css('height')) - parseFloat($('#film-info > div:first-of-type').css('height')));

$(window).load(function () {
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

    $('.show-time').on('click', function () {
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
        if (current_step == step1)
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
        if (current_step == step2 || current_step == step1)
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
    var counter = 1;
    $('#plan-azadi').children().each(function () {
        if ($(this).hasClass('free-seat')) {
            $(this).attr('data-original-title', counter);
            counter++;
        }
        else if ($(this).hasClass('sold-seat'))
            counter++;
        else if ($(this).hasClass('seat-row'))
            counter = 1;
    });

    // user rating

    $('.star-ratings-sprite').mousemove(function (event) {
        if (!$(this).hasClass('not-rated'))
            return false;
        $(this).find('span').css('width', parseInt(((event.pageX - $(this).offset().left) / parseFloat($(this).css('width')) * 100)/10)*10 + 10 + '%');
    }).hover(function () {
    }, function () {
        if (!$(this).hasClass('not-rated'))
            return false;
        $(this).fadeOut(200, function () {
            $(this).find('span').css('width', $(this).attr('initial-rate')).end().fadeIn(200);
        });
    }).on('click', function () {
        if (!$(this).hasClass('not-rated'))
            return false;
        $(this).removeClass('not-rated');
        var user_rate = parseFloat($(this).find('span')[0].style.width);
        var initial_rate = parseFloat($(this).attr('initial-rate'));
        var num_of_voters = $(this).next();
        var num = parseInt(num_of_voters.find('span').text());
        num_of_voters.find('span').fadeOut(200, function () {
            $(this).text(num + 1).fadeIn(200);
        });
        $(this).find('span').css('width', (user_rate + initial_rate * num) / (num + 1) + '%');

        console.log(user_rate/20)

    });
});
