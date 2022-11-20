var input = document.querySelector('.input_text');
var input2 = document.querySelector('.input_text2');
var main = document.querySelector('#name');
var temp = document.querySelector('.temp');
var desc = document.querySelector('.desc');
var clouds = document.querySelector('.clouds');
var button= document.querySelector('.submit');

var url = "https://8lskb7ulb0.execute-api.us-east-1.amazonaws.com/dev/textgen";   //here add your api endpoint

button.addEventListener('click', addPost)



function addPost(e){
  e.preventDefault();

  let text_data = document.getElementById('context').value;
  let max_length =parseInt(document.getElementById('question').value);
  console.log(max_length)
  var raw = JSON.stringify({
  "prompt": text_data,
  "max_length": max_length
  });
  fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
      'Content-Type': 'application/json',
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: raw
  })
  .then(response => response.json())

  .then((data) => {
    var final = data['answer'];
    main.innerHTML = final;

  })
  .then(data => console.log(data))

  .catch(err => alert("Server error!"));
  }
