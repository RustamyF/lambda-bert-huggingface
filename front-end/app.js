var input = document.querySelector('.input_text');
var input2 = document.querySelector('.input_text2');
var main = document.querySelector('#name');
var temp = document.querySelector('.temp');
var desc = document.querySelector('.desc');
var clouds = document.querySelector('.clouds');
var button= document.querySelector('.submit');

var url = "https://0rl8ayu0t3.execute-api.us-east-1.amazonaws.com/dev/qa";   //here add your api endpoint

button.addEventListener('click', addPost)



function addPost(e){
  e.preventDefault();

  let context = document.getElementById('context').value;
  let question = document.getElementById('question').value;

  fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
      'Content-Type': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: JSON.stringify({context:context,question:question})
  })
  .then(response => response.json())

  .then((data) => {
    var final = data['answer'];
    main.innerHTML = final;

  })
  .then(data => console.log(data))



  .catch(err => alert("Wrong city name!"));
  }
