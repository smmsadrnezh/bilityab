jQuery(document).ready(function ($) {
    $('#add-event').find('input[type="submit"]').on('click', function (event) {
        event.preventDefault();

        $.ajax({
            type: "POST",
            url: "/events/edit/",
            data: $("#edit-event-form").serialize(), // serializes the form's elements.
            success: function (data) {
                if (parseInt(data)) {
                    window.location.replace(window.location.pathname);
                } else {
                    $('#add-event').find('input[type="text"]').toggleClass('has-error').next('span').toggleClass('is-visible');
                }
            }
        });

    });
});