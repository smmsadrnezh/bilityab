(function ($) {
    var your_comment = $('#your-comment');
    var user_comments = $('#comments');
    var more_info = $('#more-info');
    var fixture_ticket = $('#ticket');
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

    $('#submit-comment').on('click', function () {
        $.ajax({
            type: "POST",
            url: "/add-comment/",
            data: $("#comment-form").serialize(), // serializes the form's elements.
            success: function (data) {
                var comment = $('<div class="comment col col-md-12"><div class="col col-md-11">' +
                '<div class="name">' + data + '</div><div class="date">۲۵ خرداد ۱۳۹۴، ۲:۱۱ عصر</div>' +
                '<div class="text"></div></div><div class="col col-md-1 image"></div></div>');
                comment.find('.text').text(your_comment.find('textarea').val());
                comment.find('.image').css('background-image', your_comment.find('.image').css('background-image'));
                $('#comments').append(comment);
                your_comment.find('textarea').val('');
            }
        });
    });
})(jQuery);