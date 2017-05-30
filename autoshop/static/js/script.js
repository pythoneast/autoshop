$(document).ready(function() {
    $('.slide_show').slick({
        autoplay: true,
        autoplaySpeed: 5000,
        speed: 800,
        controlMode: true,
        dots: true,
        arrows: false,
    });

    // Set the date we're counting down to
    var expire_date = $('#expire_date').data('expire');
    var countDownDate = new Date(expire_date).getTime();
    var x;
    // Update the count down every 1 second
    x = setInterval(function() {

        // Get todays date and time
        var now = new Date().getTime();

        // Find the distance between now an the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="demo"
        $("#demo").html(days + "d " + hours + "h " + minutes + "m " + seconds + "s ");

        // If the count down is finished, write some text
        if (distance < 0 && x) {
                clearInterval(x);
                $("#demo").html("EXPIRED");
                x = null;
        }
    }, 1000);

    $('#order_by').change(function () {
        $('#form-order-by').submit();

    });
});
