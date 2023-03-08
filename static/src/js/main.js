const primaryNav = document.querySelector('.header__primary-nav');
const toggleBar  = document.querySelector('.header__toggle');
const totalTrendingNews = JSON.parse(document.getElementById('total-trending-news').textContent);
const trendingAjaxURl = JSON.parse(document.getElementById('ajax_url').textContent);
const trendingLoadMoreButton = document.querySelector('.home-trending-button__button')
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

function loadMoreTrendingNews(e) {
  e.preventDefault()
  const _trending_news_container = $('.home-trending__news')
  const _current_trending_news = $('.home-trending__news .card-top-image').length
  const _limit = 3;
  $.ajax({
    url: trendingAjaxURl,
    type: 'POST',
    data: {
      'offset': _current_trending_news,
      'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
    },
    beforeSend: function () {
      
    },
    success: function (response) {
        const data = response.trending_news
        _trending_news_container.append(data)
        if( $('.home-trending__news .card-top-image').length == totalTrendingNews ) {
          trendingLoadMoreButton.style.display='none'
        }
    },
    error: function (err) {
        console.log(err);
    },
  });
}
// Home trending load more news
trendingLoadMoreButton.addEventListener('click', (e)=> loadMoreTrendingNews(e))

;(function($) {
  $('.home-features-news').slick({
    dots: false,
    infinite: false,
    arrows: false,
    slidesToShow: 3,
    slidesToScroll: 3,
    responsive: [
      {
        breakpoint: 991,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      },
    ]
  });
  $('.home-features-top-arrows__arrow--left').click(function(){
    $('.home-features-news').slick('slickPrev');
  })
  
  $('.home-features-top-arrows__arrow--right').click(function(){
    $('.home-features-news').slick('slickNext');
  })
}(jQuery));