jQuery(document).ready(function ($) {
    $('#edit-event').find('input[type="submit"]').on('click', function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: $("#edit-event-form").serialize(), // serializes the form's elements.
            success: function (data) {
                if (parseInt(data)) {
                    alert("test");
                    window.location.replace("/events");
                } else {
                    alert("error")
                    $('#edit-event').find('input[type="text"]').toggleClass('has-error').next('span').toggleClass('is-visible');
                }
            }
        });

    });
});