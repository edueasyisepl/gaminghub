const typedText = document.querySelector(".typed-text");
const cursor = document.querySelector(".cursor");

const textArray = ["Play", "Win", "&", "Conquer"];

let textArrayIndex = 0;
let charIndex = 0;

const erase = () => {
  if (charIndex > 0) {
    cursor.classList.remove('blink');
    typedText.textContent = textArray[textArrayIndex].slice(0, charIndex - 1);
    charIndex--;
    setTimeout(erase, 80);
  } else {
    cursor.classList.add('blink');
    textArrayIndex++;
    if (textArrayIndex > textArray.length - 1) {
      textArrayIndex = 0;
    }
    setTimeout(type, 1000);
  }
}

const type = () => {
  if (charIndex <= textArray[textArrayIndex].length - 1) {
    cursor.classList.remove('blink');
    typedText.textContent += textArray[textArrayIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, 120);
  } else {
    cursor.classList.add('blink');
    setTimeout(erase, 1000);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  type();
})

function cformslide() {
  var cform = document.getElementById('cform')
  var scrollval2 = window.scrollY;
  if (scrollval2 > 1200) {
    cform.style.left = '-5%';
    cform.style.transition = 'left 2.2s';
  }
}
window.addEventListener('scroll', cformslide);

function slidingtext() {
  var scrollval = window.scrollY;
  if (scrollval <= 200) {
    document.getElementById("landing-page-text-box").style.animation = "slidingheadings 1.4s ease-in-out";
    document.getElementById("landing-page-text-box").style.animationDelay = "3.7s";
  }
}

window.addEventListener('load', slidingtext);

// let signupclose = document.getElementById('signupclose');
// let form_cont = document.getElementById('form-cont');
// signupclose.addEventListener('click', function() {
//   form_cont.style.top = '-100%';
//   form_cont.style.transition = 'top .6s ease-in-out';
// })