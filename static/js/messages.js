function closeMessage(el) {
    el.classList.add('is-hidden');
    document.getElementById('closed').classList.add('white-block')
}

document.querySelectorAll('.js-messageClose').forEach(item => {
    item.addEventListener('click', function(e) {
        closeMessage(this.closest('.message'))
    })
})