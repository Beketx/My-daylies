// console.log(typeof([1,2,3]))
let title = document.getElementById('title')
console.log(title)
title.innerHTML = 'changed title';

let box = document.querySelector('.box');
console.log(box);

let item = document.createElement('li')
item.innerHTML = 'item';


box.appendChild(item)
//li in ul






//button showAlertConsole
let i = 0;
function showAlertConsole(){
    console.log(`item: ${i++}`)
}
//button showAlert
let b = 0;
function showAlert(){
    alert(`item: ${b++}`)
}
//button addItem
let box2 = document.querySelector('.box2')
console.log(box2)
let c = 0;
function addItem(){
let link = document.createElement('li')
link.innerHTML = `item: ${c++}`
box2.appendChild(link)
}


// button of input 
let g = 0;
let inBox = document.querySelector('.inBox')
let todo_input = document.querySelector('.todo_input')
function addInput(){
    if(todo_input.value.length != 0 ){
    let li = document.createElement('li')
    li.innerHTML = todo_input.value
    inBox.appendChild(li)
    todo_input.value = ''}
    else{
        alert('error')
    }
}
//отступ от парента лефт райт топ ботттом
console.log(todo_input.offsetTop,todo_input.offsetLeft)//отступ от парента









///ADDEVENTLISTENER

document.addEventListener("click", function(){
    console.log(1)
})







//
let time = document.querySelector('.time')
time.innerHTML = new Date();

// обновляет секунду то естьвызывает эту функцию в интервале 1000
//function showCurTime(){
//     time.innerHTML = new Date();
// }
// setInterval(showCurTime, 1000);

function show(){
    console.log('show method')
}
setTimeout(show,3000) //показывает функцию после 3 секунда на консоли
setTimeout(function () {
    console.log('afetr second it will show')
}, 1000);

//setinterval
t = 0;
setInterval(function(){
    console.log(`item: ${t++}`)
}, 100000);
//settimeout
k=0;
setTimeout(function(){
    console.log('Kiko')
},3000)