// console.log('hello');
console.log(typeof(1.5))
console.log(typeof(hello))
console.log(typeof("hello"))
console.log(typeof('hello'))
console.log(typeof(true))
console.log(typeof(undefined))
console.log(typeof({"a":2}))
console.log(typeof([1,2,3]))
console.log(typeof(function(){}))

console.log(2 == 2)
console.log("2" == 2) /*-->* переводит воторе значение в стринг*/
console.log("2" == "2") /* <-- */
console.log("2.0" == 2)
console.log(2+2)
console.log("2" === 2)
console.log("2"==="2")
console.log("2"!== 2)

a = {"a":1}

b = {"a":1}
console.log(a === b)

a["c"] = 1
console.log(a)


a = 2; //its same as var a = 2, its global i can use it everywhere
var b = 2; //ts global

let f = 3; //its local variable , i can use on only in scope in class in block

const c = 3; // constant

/*c+=2*/ // false

f+=3;
console.log(f);

for (i = 0 ; i<5 ; i++){
    console.log(i) 
}
/* 1
2
3
4
*/

/* console.log(i) */
/* 5  */
//so here it 5 because after ending for it becomes 5

for (var i=0 ; i<5; i++){
    console.log(i)
}
/* 1
2
3
4
*/

for (let h=0;h<5;h++){
    console.log(h)
}
/* 0
1
2
3
4
*/

/*   console.log(h) WROMNG WRONG cannot find h because h in the scope of for */


// for(const j=0;j<6;j++){
//     console.log(j)
// } WRONG WRONG beacuse of const it cannot change
