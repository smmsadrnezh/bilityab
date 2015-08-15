(function ($) {

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