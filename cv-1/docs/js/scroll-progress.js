document.addEventListener("DOMContentLoaded", function () {
  var bar = document.createElement("div");
  bar.id = "scroll-progress-bar";
  document.body.appendChild(bar);

  window.addEventListener("scroll", function () {
    var scrollTop = window.scrollY || document.documentElement.scrollTop;
    var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = progress + "%";
  });
});
