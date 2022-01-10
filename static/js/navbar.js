current();
let list = document.querySelectorAll('.list');

function current() {
    if (document.URL.includes("stopwatch")) {
        let timer = document.getElementById("timer")
        timer.classList.add("active");
    }
    if (document.URL.includes("team")) {
        let team = document.getElementById("team")
        team.classList.add("active");
    }
    if (document.URL.includes("results")) {
        let results = document.getElementById("results")
        results.classList.add("active");
    }
    if (document.URL.includes("settings")) {
        let settings = document.getElementById("settings")
        settings.classList.add("active");
    }
}

function activeLink() {
    list.forEach((item) =>
        item.classList.remove('active'));
    this.classList.add('active');
}

list.forEach((item) =>
    item.addEventListener('mouseover', activeLink));

function remove() {
    list.forEach((item) =>
        item.classList.remove('active'));
    current();
}

list.forEach((item) =>
    item.addEventListener('mouseout', remove));

if (!document.getElementById("navigation")) {
    document.getElementById("home-bar").classList.add('border-bottom')
}