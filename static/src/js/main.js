if(document.location.pathname == '/') {
  const primaryNav = document.querySelector('.header__primary-nav');
  const toggleBar  = document.querySelector('.header__toggle');
  const totalTrendingNews = JSON.parse(document.getElementById('total-trending-news').textContent);
  const trendingAjaxURl = JSON.parse(document.getElementById('ajax_url').textContent);
  const subscribeNewsletterAjaxUrl = JSON.parse(document.getElementById('subscribe_newsletter_ajax_url').textContent);
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

    // Newsletter subscribtion
    $('body').on('submit', '#newsletter', function (e) {
      e.preventDefault()
      const $this = $(this)
      const $email = $('#email').val()
      if( ! isEmail( $email ) ) {
        $('.newsletter__message--error').show(100)
        return
      }
      $.ajax({
        url: subscribeNewsletterAjaxUrl,
        type: 'POST',
        data: {
          'email': $email,
          'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
        },
        beforeSend: function () {
          $('.newsletter-form__submit').val('Subscribe...')
        },
        success: function (response) {
            const {error, message} = response
            if(error) {
              $('.newsletter__message--error').show(100).text(message)
              setTimeout(function(){
                $('.newsletter__message--error').hide()
              }, 3000)
            } else {
              $this[0].reset()
              $('.newsletter__message--success').show(100).text(message)
              setTimeout(function(){
                $('.newsletter__message--success').hide()
              }, 3000)
            }
            $('.newsletter-form__submit').val('Subscribe')
        },
        error: function (err) {
            console.log(err);
        },
      });
    })
    // Hide email error message
    $('#email').keyup(function(){
      const $newsletterError = $('.newsletter__message--error')
      if( $newsletterError.length ) {
        $('.newsletter__message--error').hide(100)
      }
    })
  }(jQuery));

}
if(document.location.pathname == '/download-magazine') {
  ;(function($) {
    let selectedMagazine;
    // Newsletter subscribtion
    $('body').on('submit', '.magazine-form', function (e) {
      e.preventDefault()
      const $this = $(this)
      const email = $("input[name='email']");
      if( ! isEmail( email.val() ) ) {
        email.after(
          '<span class="magazine-form__error">Invalid Email Address</span>'
        )
        return
      }
      if( e.target.checkValidity() ) {
        selectedMagazine = $('select', $(this)).val();
        $(this)[0].reset()
        $(this).hide()
        $('.magazine-download').show()
        $('.magazine-download__msg').show()
        $('.magazine-download__msg--thanks').hide()
        $(`.magazine-download__link--${selectedMagazine.split(' ')[0].toLowerCase()}`).css({'display': 'inline-block' })
      }
     
    })
    // Hide email error message
    $("input[name='email']").keyup(function(){
        
      if( $(this).next().is('span')) {
        $(this).next().hide(100)
      }
    })
    $('.magazine-download__link').on('click', function(e){
      e.preventDefault()
      const pdfDocument = $(this).attr("href");
      const newTab = window.open(pdfDocument, '_blank');
      newTab.location;
      
      $('.magazine-download__msg').hide()
      $('.magazine-download__msg--thanks').show()
      $('.magazine-download__msg span').text(selectedMagazine)
      $('.magazine-download__link--home').css({'display': 'inline-block'})
      $(this).hide()

    })
  }(jQuery));
}
/* Check if email is valid */
const isEmail = (email) => {
  const regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
};