const header = document.querySelector("header");

window.addEventListener("scroll", function(){
    header.classList.toggle("sticky", this.window.scrollY > 0)
})

let menu = document.querySelector('#menu-icon');
let navmenu = document.querySelector('.navmenu');

//화면창 좁을 때만 오른쪽에 list나옴
menu.onclick = () =>{
    menu.classList.toggle('bx-x');
    navmenu.classList.toggle('open');
}