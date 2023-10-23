let topButton = document.getElementById('demo');
// document.getElementById('demo').style.fontSize = "35px";

// topButton.style.fontSize = "35px";
// topButton.innerHTML =  "Hi";
// document.write(topButton);

let message = document.getElementsByClassName('.neighbourinfo');
let form = document.getElementsByClassName('.get-info');
let input = document.getElementsByName('Name');

message.textContent = 'check';

// let paragraph = ' ';
// paragraph.textContent = input.value;

form.onsubmit = function(evt) {
    evt.preventDefault();
    // Измените значение textContent на следующей строке
    console.log(input.value);
    message.textContent = input.value;
  };