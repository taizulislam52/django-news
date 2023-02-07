const primaryNav = document.querySelector('.header__primary-nav');
const toggleBar  = document.querySelector('.header__toggle');
const dropdownMenuItems   = document.querySelectorAll('.header__primary-menu__item--dropdown')

toggleBar.addEventListener( 'click', openNavigation )


function openNavigation () {
    toggleBar.classList.toggle('header__toggle--open')
    primaryNav.classList.toggle('header__primary-nav--open')
}

dropdownMenuItems.forEach(el => {
    el.addEventListener('click', (e) => {
      e.currentTarget.classList.toggle('header__primary-menu__item--open'); // works correctly
    });
});