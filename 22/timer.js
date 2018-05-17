const leftTime = document.querySelector('.display__time-left');
const endTimeTag = document.querySelector('.display__end-time');
const buttons = document.querySelectorAll('.timer__button');
const minuteText = document.customForm;

let now = 0;
let then = 0;

// Buttons functionality
buttons.forEach(button => button.addEventListener('click', addTime));

function addTime(e) {
  timer(e.target.dataset.time);
}

// Manual Input
minuteText.addEventListener('submit', addMinutes);

function addMinutes(e) {
  e.preventDefault();
  timer(e.srcElement["0"].value * 60);
  // e.srcElement["0"].value = '';
  minuteText.reset();
}

// Zero training number
function addZero(num) {
  return num < 10 ? '0' : '';
}
// Print time
function showTime(left) {

  const leftMin = Math.floor(left / 60);
  const leftSec = left % 60;

  const timeText = `${addZero(leftMin)}${leftMin}:${addZero(leftSec)}${leftSec}`;
  leftTime.textContent = timeText;
  document.title = timeText;
}

// Main Timer Logic
function timer(sec) {
  now = Date.now();
  then = now + (sec * 1000);

  // End time
  const endTime = new Date(then);
  const endHour = endTime.getHours();
  const endMin = endTime.getMinutes();
  endTimeTag.textContent = `${addZero(endHour)}${endHour}:${addZero(endMin)}${endMin}`;


  // Show first time remaining
  showTime(sec);

  // Next time remaining
  const timerHandle = setInterval(() => {
    const left = Math.round((then - Date.now()) / 1000);

    if (left < 0) {
      clearInterval(timerHandle);
    } else {
      showTime(left);
    }

  }, 1000);
}


