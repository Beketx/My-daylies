function plus(a,b){
    return a+b;
}
console.log(plus(1,2))





let mult = function (a,b){
    return a*b;
}

console.log(mult(4,5));






function hello(a){
    console.log(a);
}

hello(mult(5,5));

function privet(a){
    console.log(a(2,4))
}

privet(mult)





function kosu(){
    if(kosu.inc == undefined)
        kosu.inc = 0;
        kosu.inc += 1;
    
}

kosu()
console.log(kosu.inc)
//answer 1
kosu()
console.log(kosu.inc)
//answer 2


function bolu(){
    let aa = 2; //local its not changes from 12
    aa+=10;
    if(bolu.inc == undefined)
        bolu.inc = 0;
        bolu.inc+=1;

}

bolu()
console.log(bolu.inc)

// аттрибуты через точкы изменяются после вызова функции , а `Let остается такой же








//PROTOTYPE

function Rectangle (width, height){
    this.height = height;
    this.width = width;

}

Rectangle.prototype.area = function(){
    return this.width*this.height;
}

var r = new Rectangle(26,14);

var v =r.area();

//ECASCIPRT 6


class Rectangle extends Shape {
    constructor(height, width){
        this.width = width;
        this.height = height;

    }
    area(){
        return this.width*this.height;

    }

    static conutRects(){

    }
}

var r = new Rectangle(20,14);











//Functional porgramming 
//1 - imperative


//2 - funcitonal



//ECMASCIPTR 6 extendison
//2 - funcitonal







//JSON is th standart format for sending to and from browser


//JSON from object to string STRINGIFY

//MESSAGE FROM BACKEND AS IT CANNOT SEND OBJECT IT SENDS STRING WITH JSON
a = {"a":18}

JSON.stringify(a)

//answer  "{"a":19}"



//HERE FRONT END TAKES AND PARSE IT

"{"a":19}"

JSON.parse(a)

{"a":18}

