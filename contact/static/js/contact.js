function TimerFoo(timeInSec, urlDest) {

    var start = new Date;

    setInterval(function () {
        var time = Math.round((start - new Date) / 1000 + timeInSec);
        if (time >= -0.5) {
            $('#timer').text(time);
        } else {
            Redirect(urlDest);
        }
    }, 1000);
}
function Redirect(urlDest){
    location.href = urlDest;
}
