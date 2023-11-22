let topButton = document.getElementById("demo");
let imgButton = document.querySelector(".center-left-ava-download-button");


let input = document.querySelectorAll("input");
let surName = document.querySelector('.name');
let tg = document.querySelectorAll(".sex");
let nextPageButton = document.querySelector(".big-button");
let dateControl = document.querySelector('input[type="date"]');
let parent = document.querySelector('.prof');
let topChild = document.querySelector('.top');
let centerChild = document.querySelector('.center');
let bottomChild = document.querySelector('.bottom');






document.querySelector('.center-left-ava-download-button-input').onchange = function (event) {
    let target = event.target;

    if (!FileReader) {
        alert('FileReader не поддерживается — облом');
        return;
    }

    if (!target.files.length) {
        alert('Ничего не загружено');
        return;
    }

    let fileReader = new FileReader();
    fileReader.onload = function() {
        profileImg.src = fileReader.result;
    }
    fileReader.readAsDataURL(target.files[0]);
    let newImg = document.querySelector(".photomini");
    let newImgcss = document.querySelector(".photomini img");
    newImg.style.cssText ="width: 140px; height: 140px; overflow: hidden; border-radius: 16px; border: 1px solid #EBEBEB; background: #FFFFFF 50% / cover no-repeat;" ;
    newImgcss.style.cssText = " width: 140px; height: 140px; object-position: 0 0; object-fit: cover;" ;
}


input[3].addEventListener('change', (evt) =>{
    evt.preventDefault();
    let apart = String(input[3].value);
    let sep = apart.split([" "]);
    surName.textContent = sep[0] + " " + sep[1];
})


let inp = document.querySelectorAll('.custom-radio');

for(const button of inp){
    button.addEventListener("change", (evt) => {
        evt.preventDefault();
        let selectedSize;
        for (const radioButton of inp) {
            if (radioButton.checked) {
                selectedSize = radioButton.value;
                break;
            }
        }
        tg[0].textContent = selectedSize;
    });
}


let ageinfo = document.querySelector("#ageinfo");

function get_current_age(date) {
    return ((new Date().getTime() - new Date(date)) / (24 * 3600 * 365.25 * 1000)); //функция вычисления возраста
}

function ageMath(dateBirth) {
    return Math.floor(get_current_age(dateBirth));
}

input[6].addEventListener('change', () => {
    let output = ageMath(input[6].value);
    if (output < 100){
        ageinfo.innerHTML = (output) + ' лет';
        ageinfo.style.cssText = 'color: #040013; font-weight:400; font-size: 9px; background-color: #FFF; width: auto;';
        //window.localStorage.setItem('age', ageinfo.innerHTML);
    }
});



input[8].addEventListener('change', (evt) =>{
    evt.preventDefault();
    tg[2].textContent = String(input[8].value);
})


// document.addEventListener('DOMContentLoaded', function () {
//     if (window.jQuery){console.log("Yes")}
//     else{console.log("No")}
//     nextPageButton.addEventListener('click', (evt) =>{
//         evt.preventDefault();
//         parent.removeChild(topChild);
//         parent.removeChild(centerChild);
//         parent.removeChild(bottomChild);
        
//         jQuery("main").load("myapp/templates/myapp/index2.html #container");
//     })
// })


