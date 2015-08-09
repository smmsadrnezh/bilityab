jQuery(document).ready(function ($) {
    $('#add-category').find('input[type="submit"]').on('click', function (event) {
        event.preventDefault();

        $.ajax({
            type: "POST",
            url: "/categories/add/",
            data: $("#add-category-form").serialize(), // serializes the form's elements.
            success: function (data) {
                if (parseInt(data)) {
                    window.location.replace("/categories");
                } else {
                    $('#add-category').find('input[type="text"]').toggleClass('has-error').next('span').toggleClass('is-visible');
                }
            }
        });

    });

    $('#add-sub-category').find('input[type="submit"]').on('click', function (event) {
        event.preventDefault();

        $.ajax({
            type: "POST",
            url: "/categories/add/",
            data: $("#add-sub-category-form").serialize(), // serializes the form's elements.
            success: function (data) {
                if (parseInt(data)) {
                    window.location.replace("/categories");
                } else {
                    $('#add-sub-category').find('input[type="text"]').toggleClass('has-error').next('span').toggleClass('is-visible');
                }
            }
        });

    });

    $('#edit-category').find('input[type="submit"]').on('click', function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: $("#edit-category-form").serialize(), // serializes the form's elements.
            success: function (data) {
                if (parseInt(data)) {
                    window.location.replace("/categories");
                } else {
                    $('#edit-category').find('input[type="text"]').toggleClass('has-error').next('span').toggleClass('is-visible');
                }
            }
        });

    });
});