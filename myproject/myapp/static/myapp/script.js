const images = document.querySelectorAll("#icon img");
console.log(images);

document.addEventListener("DOMContentLoaded", () => {
    const images = document.querySelectorAll(".Book");
});


images.forEach((image) => {
    image.addEventListener("mouseenter", () =>{
        image.style.transform = "scale(1.5)";
        image.style.transition = "all 0.5s";
    
    });
    
    image.addEventListener("mouseleave", () =>{
        image.style.transform = "scale(1.1)";
        image.style.transition = "all 0.5s";
    })

});

image.addEventListener('click', () => {
    window.location.href = 'http://127.0.0.1:8000/book/';
})

const image = document.querySelector("#hotel-gio");
image.addEventListener("mouseenter", () =>{
    image.style.transform = "scale(1.5)";
    image.style.transition = "all 0.5s";
});

image.addEventListener("mouseleave", () =>{
    image.style.transform = "scale(1.1)";
    image.style.transition = "all 0.5s";
});


const button = document.createElement("button");
document.body.appendChild(button);
button.innerHTML = `<i class="fa-solid fa-arrow-up-long"></i>`;
button.style.backgroundColor = "black";
button.style.color = "white";
button.style.border = "none";
button.style.position = "fixed";
button.style.bottom = "20px";
button.style.right = "20px";
button.style.display = "none";

button.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
    
});

window.addEventListener("scroll", () => {
    if(window.scrollY > 100){
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
});

button.addEventListener("mouseenter", () => {
    button.style.backgroundColor = "white";
    button.style.color = "black";
    button.style.transform = "scale(1.1)";
});

button.addEventListener("mouseleave", () => {
    button.style.backgroundColor = "black";
    button.style.color = "white";
    button.style.transform = "scale(1)";
});

const nav = document.querySelector("nav");
nav.style.backgroundColor = "black";
nav.style.color = "white";
nav.style.display = "flex";
nav.style.justifyContent = "space-between";
nav.style.padding = "20px";
nav.style.position = "fixed";
nav.style.width = "100%";
nav.style.zIndex = "1000";
