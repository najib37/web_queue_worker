
const progressBar = document.getElementById('progress-bar');
const socket = new WebSocket('ws://' + window.location.host + '/progress/');
const saveButton = document.getElementById('save-button');

socket.onopen = function () {
  console.log('Connection established');
};

socket.onmessage = function (event) {
  const data = JSON.parse(event.data);
  progressBar.style.width = data.progress + '%';
  progressBar.textContent = data.progress.toFixed() + '%';
  if (data.progress >= 99) {
    saveButton.style.display = 'block';
    saveButton.onclick = function () {
      window.location.href = '/download/';
    };
  }
};
