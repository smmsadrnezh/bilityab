$('#left-info').css('height', parseFloat($('#film-trailer').css('width'))*9/16);

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
        current_select.fadeOut(function () {
            show_times.fadeIn();
            current_select = show_times;
        });

        step2.removeClass('done').addClass('active');
        step2.next().removeClass('done').addClass('active');

        step3.removeClass('active');
    });

});
