//VARIABLESS
let thumbnails = document.getElementsByClassName("thumbnail");
let slider = document.getElementById("slider");
let buttonRight = document.getElementById("slid-right");
let buttonLeft = document.getElementById("slid-left");

buttonLeft.addEventListener("click", () => {
    slider.scrollLeft -= 360;
});

buttonRight.addEventListener("click", () => {
    slider.scrollLeft += 360;
});

const maxScrollLeft = slider.scrollWidth - slider.clientWidth;



function autoPlay() {
    if (slider.scrollLeft > (maxScrollLeft - 1)) {
        slider.scrollLeft -= maxScrollLeft;
    }
    else {
        slider.scrollLeft += 1;
    }
}

let play = setInterval(autoPlay, 100);

for (let i = 0; i < thumbnails.length; i++) {
    thumbnails[i].addEventListener("mouseover", () => {
        clearInterval(play)
    })
    thumbnails[i].addEventListener("mouseout", () => {
        return play = setInterval(autoPlay, 100);
    })
}