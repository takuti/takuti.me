const header = document.getElementsByTagName("header")[0];
console.log(header);

const hH = header.clientHeight;
const winH = window.innerHeight;
const docH = document.documentElement.scrollHeight;
const windBtm = docH - winH;

let pos = 0;
let lastPos = 0;

const onScroll = () => {
  if(pos > hH && pos > lastPos) {
    header.classList.add('header-unpinned');
  }
  if(pos < hH || pos < lastPos || windBtm <= pos) {
    header.classList.remove('header-unpinned');
  }

  lastPos = pos;
};

window.addEventListener("scroll", () => {
  pos = window.scrollY;
  onScroll();
});
