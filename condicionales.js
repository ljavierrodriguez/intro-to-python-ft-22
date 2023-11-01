// Condicionales
/* 

if (condicion) {
    sencencias
}

if (condicion) {
    sentencias
} else {
    sentencias
}

if (condicion) {
    sentencias
} else if (condicion) {
    sentencias
} else {
    sentencias
}

switch(value){
    case
    default
}

and = &&
or = ||
not = !

*/

let a = 5;
let b = 10;
let c = 4;

if (a > b){
    console.log("Info")
}


if ( b === c) {
    // sentencias
} else {
    // sentencias
}

if (a > b && a > c) {
    console.log("A")
} else if (b > c){
    console.log("B")
} else {
    console.log("C")
}

// ternario
let mayor = a > b ? "A" : "B"