const scrollProgress = document.getElementById('scroll-progress');
const height =
  document.documentElement.scrollHeight - document.documentElement.clientHeight;

window.addEventListener('scroll', () => {
  const scrollTop =
    document.body.scrollTop || document.documentElement.scrollTop;
    scrollProgress.style.width = `${(scrollTop / height) * 100}%`;

  const scrollPercent = 
  Math.round((scrollTop / height) * 100);
  scrollProgress.style.width = `${scrollPercent}%`;
  scrollProgress.setAttribute('data-scroll-percent', scrollPercent);
});