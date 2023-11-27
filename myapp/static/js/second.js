let ageinfo = document.querySelector("#ageinfo");
let course_1 = document.querySelector("#c1");
let course_2 = document.querySelector("#c2");
let course_3 = document.querySelector("#c3");
let course_4 = document.querySelector("#c4");
let course_5 = document.querySelector("#c5");
let course_6 = document.querySelector("#c6");

let age = window.localStorage.getItem("years");

if (age != null){
    ageinfo.innerHTML = age;
}




