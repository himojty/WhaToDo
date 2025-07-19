window.addEventListener('scroll', function() {
  const header = document.querySelector('.header');
  if (window.scrollY > 50) { // 50 - это порог скролла, можно изменить
    header.classList.add('sticky');
  } else {
    header.classList.remove('sticky');
  }
});