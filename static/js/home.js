(function ($) {

    $('.widget .small-event').hover(function () {
        if($(this).find('.date span').attr('discount'))
            $(this).find('.date span').fadeOut(200, function () {
                $(this).text($(this).attr('discount')).css('color', '#D6134E').fadeIn();
            });
    }, function () {
        if($(this).find('.date span').attr('discount'))
            $(this).find('.date span').fadeOut(200, function () {
                $(this).text($(this).attr('date')).css('color', '#337ab7').fadeIn();
            });
    });

    $('.small-event .date .inner-text').each(function () {
        $(this).attr('date', $(this).text());
    });

    var nav_tabs_length = $('#events .nav-tabs').children().length;

    $('#events .nav-tabs > li').css('width', 100/nav_tabs_length+'%');

    var cinema_events = $('.cinema').closest('.event');
    cinema_events.on('click', function () {
        window.location.href = "events/cinema/" + $(this).attr('event_id');
    });

    var sport_events = $('.sport').closest('.event');
    sport_events.on('click', function () {
        window.location.href = "events/sport/" + $(this).attr('event_id');
    });

    var tourism_events = $('.tourism').closest('.event');
    tourism_events.on('click', function () {
        window.location.href = "events/tourism/" + $(this).attr('event_id');
    });

    var music_events = $('.music').closest('.event');
    music_events.on('click', function () {
        window.location.href = "events/music/" + $(this).attr('event_id');
    });
    
})(jQuery);