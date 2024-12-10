document.addEventListener("DOMContentLoaded", function () {
  let mybutton = document.getElementById("back-to-top");

  window.onscroll = function () {
    scrollFunction();
  };

  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }

  function topFunction() {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }

  mybutton.addEventListener("click", topFunction);
});

document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".btn-edit");

  editButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Scroll to the comment form smoothly
      const commentForm = document.getElementById("commentForm");
      commentForm.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
});
