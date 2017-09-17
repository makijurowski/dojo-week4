$(document).ready(function () {
    $(".childshow").click(function (e) {
        e.stopPropagation();
        if ($(this).children('.childshow').is(':visible')) {
            $(this).children('.childshow').hide();
        }
        else {
            $(this).children('.childshow').show();
        }
    });
});