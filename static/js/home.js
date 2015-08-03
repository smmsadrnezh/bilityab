(function ($) {

    //var eventImage = $("#event_id");
    //eventImage.on('click', function () {
    //    window.location.href = "events/cinema/";
    //});

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

    //var sportImage = $(".sport");
    //sportImage.on('click', function () {
    //    window.location.href = "events/sport/1";
    //});
    //
    //var tourismImage = $(".tourism");
    //tourismImage.on('click', function () {
    //    window.location.href = "events/tourism/1";
    //});
    //
    //var musicImage = $(".music");
    //musicImage.on('click', function () {
    //    window.location.href = "events/music/1";
    //});

})(jQuery);