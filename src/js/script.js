let topButton = document.getElementById("demo");
let imgButton = document.querySelector(".center-left-ava-download-button");
// document.getElementById('demo').style.fontSize = "35px";

// topButton.style.fontSize = "35px";
// topButton.innerHTML =  "Hi";
// document.write(topButton);

let input = document.querySelectorAll("input");
let surName = document.querySelector('.name');
let tg = document.querySelectorAll(".sex");
var dateControl = document.querySelector('input[type="date"]');



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


input[1].addEventListener('change', (evt) =>{
    evt.preventDefault();
    let apart = String(input[1].value);
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

// console.log(input);

input[4].addEventListener('change', (evt) =>{
    evt.preventDefault();
    let currentDate = new Date();
    dateformat
    let apart = input[4].value;
    let year, day, month = apart.split(["-"]);
    year = currentDate.getFullYear() - year;
    day = currentDate.getDay;
    month = currentDate.getMonth;
})



input[5].addEventListener('change', (evt) =>{
    evt.preventDefault();
    let apart = String(input[4].value);
    let sep = apart.split([" "]);
    tg[2].textContent = sep[0];
})


