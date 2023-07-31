const burger = document.querySelector('nav.navbar .burger')
const navigations = document.querySelector('nav.navbar .navigations')  


// Membuat navbar togle
burger.addEventListener('click', function () {
    navigations.classList.toggle('active')
})


// Klik diluar navbar dan burger untuk close
document.addEventListener('click', function (e) {
    if (!burger.contains(e.target) && !navigations.contains(e.target)) {
        navigations.classList.remove('active')
    }
}
)
