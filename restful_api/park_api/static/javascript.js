let display = document.getElementById('display');

function appendToDisplay(input){
    display.value += input;
}

function calculate() {
  try {
    display.value = eval(display.value);
  } catch (error) {
    display.value = 'Error';
  }
}

function clearDisplay() {
  display.value = '';
}

function showSidebar(){
    const sidebar = document.querySelector('.sidebar');
        sidebar.style.display = 'flex';
    }

function hideSidebar(){
    const sidebar = document.querySelector('.sidebar');
       sidebar.style.display = 'none';
    }

function showToolbar(){
    const toolbar = document.querySelector('.toolbar');
        toolbar.style.display = 'flex';
    }

function hideToolbar(){
    const toolbar = document.querySelector('.toolbar');
       toolbar.style.display = 'none';
    }

let response = document.getElementById('response')
function clearResponse() {
  response.innerHTML = '';
}
