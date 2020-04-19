let box = document.querySelector('.box')
let input = document.querySelector('.todo_class')
function addItem(){
    if(input.value != ''){
    // console.log(input.value)
    let li = document.createElement('li')
    li.innerHTML = input.value
    box.appendChild(li)
    input.value = ''}
    else{
        alert('error')
    }
}