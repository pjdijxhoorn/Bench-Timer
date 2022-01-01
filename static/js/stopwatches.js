// the code below is for the toggle buttons to switch between bench and field timers

document.addEventListener('DOMContentLoaded', function() {

    let checkbox = document.querySelectorAll('input[type="checkbox"]');
    let start = document.querySelectorAll("a[href='#start']");
    let stop = document.querySelectorAll("a[href='#stop']");
    let reset = document.querySelectorAll("a[href='#reset']");

    document.getElementById("start").addEventListener("click", startBtn);

    function startBtn() {
        trueCheck = true;
        start[32].click();
        check0();
        check1();
        check2();
        check3();
        check4();
        check5();
        check6();
        check7();
        check8();
        check9();
        check10();
        check11();
        check12();
        check13();
        check14();
        check15();

    }

    checkbox[0].addEventListener('change', check0);
    checkbox[1].addEventListener('change', check1);
    checkbox[2].addEventListener('change', check2);
    checkbox[3].addEventListener('change', check3);
    checkbox[4].addEventListener('change', check4);
    checkbox[5].addEventListener('change', check5);
    checkbox[6].addEventListener('change', check6);
    checkbox[7].addEventListener('change', check7);
    checkbox[8].addEventListener('change', check8);
    checkbox[9].addEventListener('change', check9);
    checkbox[10].addEventListener('change', check10);
    checkbox[11].addEventListener('change', check11);
    checkbox[12].addEventListener('change', check12);
    checkbox[13].addEventListener('change', check13);
    checkbox[14].addEventListener('change', check14);
    checkbox[15].addEventListener('change', check15);

    function check0() {
        if (checkbox[0].checked && trueCheck === true) {
            start[1].click();
            stop[0].click();
            reset[0].click();

        } else if (trueCheck === true) {
            start[0].click();
            stop[1].click();

        }
    }

    function check1() {
        if (checkbox[1].checked && trueCheck === true) {
            start[3].click();
            stop[2].click();
            reset[2].click();

        } else if (trueCheck === true) {
            start[2].click();
            stop[3].click();

        }
    }

    function check2() {
        if (checkbox[2].checked && trueCheck === true) {
            start[5].click();
            stop[4].click();
            reset[4].click();

        } else if (trueCheck === true) {
            start[4].click();
            stop[5].click();

        }
    }

    function check3() {

        if (checkbox[3].checked && trueCheck === true) {
            start[7].click();
            stop[6].click();
            reset[6].click();

        } else if (trueCheck === true) {
            start[6].click();
            stop[7].click();

        }
    }

    function check4() {

        if (checkbox[4].checked && trueCheck === true) {
            start[9].click();
            stop[8].click();
            reset[8].click();

        } else if (trueCheck === true) {
            start[8].click();
            stop[9].click();

        }
    }

    function check5() {

        if (checkbox[5].checked && trueCheck === true) {
            start[11].click();
            stop[10].click();
            reset[10].click();

        } else if (trueCheck === true) {
            start[10].click();
            stop[11].click();

        }
    }

    function check6() {
        if (checkbox[6].checked && trueCheck === true) {
            start[13].click();
            stop[12].click();
            reset[12].click();

        } else if (trueCheck === true) {
            start[12].click();
            stop[13].click();

        }
    }

    function check7() {

        if (checkbox[7].checked && trueCheck === true) {
            start[15].click();
            stop[14].click();
            reset[14].click();

        } else if (trueCheck === true) {
            start[14].click();
            stop[15].click();

        }
    }

    function check8() {

        if (checkbox[8].checked && trueCheck === true) {
            start[17].click();
            stop[16].click();
            reset[16].click();

        } else if (trueCheck === true) {
            start[16].click();
            stop[17].click();

        }
    }

    function check9() {

        if (checkbox[9].checked && trueCheck === true) {
            start[19].click();
            stop[18].click();
            reset[18].click();

        } else if (trueCheck === true) {
            start[18].click();
            stop[19].click();

        }
    }

    function check10() {

        if (checkbox[10].checked && trueCheck === true) {
            start[21].click();
            stop[20].click();
            reset[20].click();

        } else if (trueCheck === true) {
            start[20].click();
            stop[21].click();

        }
    }

    function check11() {

        if (checkbox[11].checked && trueCheck === true) {
            start[23].click();
            stop[22].click();
            reset[22].click();

        } else if (trueCheck === true) {
            start[22].click();
            stop[23].click();

        }
    }

    function check12() {

        if (checkbox[12].checked && trueCheck === true) {
            start[25].click();
            stop[24].click();
            reset[24].click();

        } else if (trueCheck === true) {
            start[24].click();
            stop[25].click();

        }
    }

    function check13() {

        if (checkbox[13].checked && trueCheck === true) {
            start[27].click();
            stop[26].click();
            reset[26].click();

        } else if (trueCheck === true) {
            start[26].click();
            stop[27].click();

        }
    }

    function check14() {

        if (checkbox[14].checked && trueCheck === true) {
            start[29].click();
            stop[28].click();
            reset[28].click();

        } else if (trueCheck === true) {
            start[28].click();
            stop[29].click();

        }
    }

    function check15() {

        if (checkbox[15].checked && trueCheck === true) {
            start[31].click();
            stop[30].click();
            reset[30].click();

        } else if (trueCheck === true) {
            start[30].click();
            stop[31].click();

        }
    }
});

// code under this comment is to build the stopwatches

let Stopwatch = function(elem, options) {
    let timer = createTimer(),
        startButton = createButton("start", start),
        stopButton = createButton("stop", stop),
        resetButton = createButton("reset", reset),
        offset,
        clock,
        interval;

    // default options
    options = options || {};
    options.delay = options.delay || 1;

    // append elements
    elem.appendChild(timer);
    elem.appendChild(startButton);
    elem.appendChild(stopButton);
    elem.appendChild(resetButton);

    // initialize
    reset();

    // private functions
    function createTimer() {
        return document.createElement("span");
    }

    function createButton(action, handler) {
        let a = document.createElement("a");
        a.href = "#" + action;
        a.innerHTML = action;
        a.addEventListener("click", function(event) {
            handler();
            event.preventDefault();
        });
        return a;
    }

    function start() {
        if (!interval) {
            offset = Date.now();
            interval = setInterval(update, options.delay);
        }
    }

    function stop() {
        if (interval) {
            clearInterval(interval);
            interval = null;
        }
    }

    function reset() {
        clock = 0;
        render(0);
    }

    function update() {
        clock += delta();
        render();
    }

    function render() {
        let h = Math.floor(clock / (1000 * 60 * 60)) % 24;
        let m = Math.floor(clock / (1000 * 60)) % 60;
        let s = Math.floor(clock / 1000) % 60;

        if (h < 10) {
            h = "0" + h;
        }
        if (m < 10) {
            m = "0" + m;
        }
        if (s < 10) {
            s = "0" + s;
        }

        timer.innerHTML = h + ':' + m + ':' + s + '';

    }

    function delta() {
        let now = Date.now(),
            d = now - offset;

        offset = now;
        return d;
    }

    this.start = start;
    this.stop = stop;
    this.reset = reset;
};

let elems = document.getElementsByClassName("basic");
for (let i = 0, len = elems.length; i < len; i++) {
    Stopwatch(elems[i]);
}

// code under this comment is for the stop and reset functions
document.getElementById("stop").addEventListener("click", stopBtn);

function stopBtn() {
    trueCheck = false;
    let stopBtn = document.querySelectorAll("a[href='#stop']");
    for (let i = 0; i < stopBtn.length; i++)
        stopBtn[i].click();
}

document.getElementById("reset").addEventListener("click", resetBtn);

function resetBtn() {
    let resetBtn = document.querySelectorAll("a[href='#reset']");
    for (let i = 0; i < resetBtn.length; i++)
        resetBtn[i].click();
}