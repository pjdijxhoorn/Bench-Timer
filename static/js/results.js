let x = document.getElementById('overall-time').innerHTML;
var y = x.split(':');
let overall = (+y[0]) * 60 * 60 + (+y[1]) * 60 + (+y[2]);
console.log(overall)

for (let i = 0; i < 16; i++) {
    document.getElementById('bench' + i).innerHTML = stripTime(document.getElementById('field' + i).innerHTML);
}

function stripTime(string) {
    var a = string.split(':');
    var b = (+a[0]) * 60 * 60 + (+a[1]) * 60 + (+a[2]);
    sec = overall - b;
    return convertTime(sec)

    function convertTime(sec) {
        var hours = Math.floor(sec / 3600);
        (hours >= 1) ? sec = sec - (hours * 3600): hours = '00';
        var min = Math.floor(sec / 60);
        (min >= 1) ? sec = sec - (min * 60): min = '00';
        (sec < 1) ? sec = '00': void 0;

        (min.toString().length == 1) ? min = '0' + min: void 0;
        (sec.toString().length == 1) ? sec = '0' + sec: void 0;

        return hours + ':' + min + ':' + sec;
    }
}