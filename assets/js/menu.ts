const header = document.getElementsByTagName("header")[0];

const hH = header.clientHeight;
const winH = window.innerHeight;
const docH = document.documentElement.scrollHeight;
const windBtm = docH - winH;

let pos = 0;
let lastPos = 0;

const onScroll = () => {
  if (pos > hH && pos > lastPos) {
    header.classList.add('header-unpinned');
    const navToggler = document.getElementById('nav-input') as HTMLInputElement;
    if (navToggler.checked) {
      navToggler.checked = false;
    }
  }
  if (pos < hH || pos < lastPos || windBtm <= pos) {
    header.classList.remove('header-unpinned');
  }

  lastPos = pos;
};

window.addEventListener("scroll", () => {
  pos = window.scrollY;
  onScroll();
});

window.addEventListener("hashchange", function () {
  // hide the header when jumping from one pos to the other by a hash link e.g., footnote
  header.classList.add('header-unpinned');
  // remove a hash in URL (window.location) so the hashchange event is fired even if the same hash is clicked twice
  history.pushState("", document.title, window.location.pathname + window.location.search);
});
