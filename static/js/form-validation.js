let username = document.getElementById("username")
let password = document.getElementById("password")
let confirm = document.getElementById("passwordconfirm")

let char_5 = document.getElementById('char_5')
let number = document.getElementById('number')
let letter = document.getElementById('letter')
let char_6 = document.getElementById('char_6')
let match = document.getElementById('match')

username.addEventListener('input', () => {
    let user = username.value;
    if (user.length >= 5) {
        char_5.classList.add("item__active");
    } else {
        char_5.classList.remove("item__active");
    }
})

password.addEventListener('input', () => {
    let pass = password.value;
    let conf = confirm.value;
    if (pass.length >= 6) {
        char_6.classList.add("item__active");
    } else {
        char_6.classList.remove("item__active");
    }

    if (/[0-9]/.test(pass)) {
        number.classList.add('item__active')
    } else {
        number.classList.remove('item__active');
    }

    if (/[A-Za-z]/.test(pass)) {
        letter.classList.add('item__active')
    } else {
        letter.classList.remove('item__active');
    }
    if (conf == pass) {
        match.classList.add("item__active");
    } else {
        match.classList.remove("item__active");
    }
})

confirm.addEventListener('input', () => {
    let conf = confirm.value;
    let pass = password.value;
    console.log(conf)
    console.log(pass)
    if (conf == pass) {
        match.classList.add("item__active");
    } else {
        match.classList.remove("item__active");
    }
})