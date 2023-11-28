let ageinfo = document.querySelector("#age-second-page");
let course = document.querySelectorAll('.custom-r');
let course_input = document.querySelector("#course_input");
let ed_step = document.querySelector("#id_ed_step");

let age = window.localStorage.getItem("age");
console.log(window.localStorage)
console.log(age)
ageinfo.innerHTML = age;

let course_output = 1;
let step = 'bachelor'

function output(){
    if (String(course_output) == String(course[6].value)){
        course_input.innerHTML = "Уже окончил вышку";
    }else{
        if(step == 'bachelor')
            course_input.innerHTML = course_output + " курс бакалавриата ВШБ ИБ";
        if(step == 'magistracy')
            course_input.innerHTML = course_output + " курс магистратуры ВШБ ИБ";
        if(step == 'postgraduate')
            course_input.innerHTML = course_output + " курс аспирантуры ВШБ ИБ";
    }
}




for(const button of course){
    console.log(button)
    button.addEventListener("change", (evt) => {
        evt.preventDefault();
        let selectedSize;
        for (const radioButton of course) {
            if (radioButton.checked) {
                selectedSize = radioButton.value;
                break;
            }
        }
        course_output = selectedSize;
        output();
    });
}


ed_step.addEventListener("change", (evt) =>{
    evt.preventDefault();
    step = ed_step.value
    console.log(step)
    output();
})


let newImg = document.querySelector(".photomini");
let newImgcss = document.querySelector(".photomini img");
newImg.style.cssText ="width: 140px; height: 140px; overflow: hidden; border-radius: 16px; border: 1px solid #EBEBEB; background: #FFFFFF 50% / cover no-repeat;" ;
newImgcss.style.cssText = " width: 140px; height: 140px; object-position: 0 0; object-fit: cover;" ;

// localStorage.clear()




