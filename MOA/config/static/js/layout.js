const toggleBtn = document.querySelector(".navbar__toggleBtn");
const toggleBtnImg = document.querySelector( ".navbar__toggleBtn > img" );
const menu = document.querySelector( ".navbar__menu" );
const icons = document.querySelector(".navbar__icons");

toggleBtn.addEventListener("click", () => {
  menu.classList.toggle( "active" );
  if ( "rotate__true".includes( toggleBtn.classList ) ) {
    toggleBtnImg.classList.toggle("rotate__true");

  } else {
    toggleBtnImg.classList.toggle( "rotate__true" );
  }
});