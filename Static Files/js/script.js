document.getElementById("bars").onclick = function () {
  this.classList.toggle("change");
  document.getElementById("nav").classList.toggle("show");
};

window.onscroll = function () {
  if (document.documentElement.scrollTop > 5) {
    document.getElementById("header").classList.add("nav-strict");
  } else {
    document.getElementById("header").classList.remove("nav-strict");
  }
};

const sections = document.querySelectorAll(
  "div.landing,div.about-me ,div.services ,div.exper-edu , div.portofolio ,div.blog , div.contact"
);
const navLi = document.querySelectorAll(".nav ul li a");
window.addEventListener("scroll", () => {
  current = "";
  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (window.pageYOffset > sectionTop - sectionHeight / 3) {
      current = section.getAttribute("id");
    }
  });
  navLi.forEach((a) => {
    a.classList.remove("active");
    if (a.classList.contains(current)) {
      a.classList.add("active");
    }
  });
});


let switcherLis = document.querySelectorAll(".portofolio .shuffle li");
let boxs = document.querySelectorAll(".portofolio .boxs .box");

switcherLis.forEach(li => {
  li.addEventListener("click",removeActive);
  li.addEventListener("click", manageImgs);

});

function removeActive() {
  switcherLis.forEach((li) => {
   li.classList.remove("active");
   this.classList.add("active");
  });

}

function manageImgs() {
  boxs.forEach(box => {
    box.classList.add("d-none");
  });
  document.querySelectorAll(this.dataset.work).forEach(el => {
    el.classList.remove("d-none");
  });
}


let option = document.getElementById("pet-select");

// function selected() {
//   console.log(option.options[option.onselect].text); 
// }

function manageImgsSelected() {
  boxs.forEach((box) => {
    box.classList.add("d-none");
  });
  document
    .querySelectorAll(option.options[option.selectedIndex].value)
    .forEach((el) => {
      el.classList.remove("d-none");
    });
}

option.addEventListener("click", manageImgsSelected);