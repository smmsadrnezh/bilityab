(function($){
    $('#categories > ul > li').each(function () {
        if($(this).find('ul.child').length)
            $('<i class="fa fa-plus-circle has-child"></i>').insertBefore($(this).find('ul.child'));
    });

    var active_category = $('#categories > ul > li:first-of-type');
    active_category.addClass('active');
    $('#categories > ul > li').on('click', function () {
        if($(this).hasClass('active'))
            return false;
        var children = $(this).find('.child');
        if(children.length) {
            $(this).css('padding-bottom', '0');
            children.slideDown();
            $(this).find('.has-child').removeClass('fa-plus-circle').addClass('fa-caret-down');
        }
        children = active_category.find('.child');
        if(children.length){
            active_category.css('padding-bottom', '0.5em');
            children.slideUp();
            active_category.find('.has-child').removeClass('fa-caret-down').addClass('fa-plus-circle');
        }
        active_category.removeClass('active');
        $(this).addClass('active');
        active_category = $(this);
    });

    var active_sub_category = undefined;
    $('#categories ul.child li').on('click', function () {
        if($(this).hasClass('active'))
            return false;
        $(this).addClass('active');
        if(active_sub_category)
            active_sub_category.removeClass('active');
        active_sub_category = $(this);
    });

})(jQuery);