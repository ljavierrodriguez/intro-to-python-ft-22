// Variables 
/* 
Definir Variables

var, let y const

Data Types:

String
Number
Boolean
Undefined

Object:
    Null
    Literal Object
    Array

function

*/

let nombre = "";
let apellido = '';
let direccion = ` texto 
sadsd
asdasd
asd

`;

let nombreCompleto = `${nombre} ${apellido}`;

let edad = 30; // number

let precio = 10.50; // number

let activo = false;

let open = true;

let postalCode; // undefined
let piso = null;


let persona = { // object
    nombre: 'John',
    apellido: 'Doe'
}

persona.nombre
persona["nombre"]

let nombres = ["Hugo", "Paco", "Luis"]
nombres[1]


function sumar(a, b){ // function
    return a + b;
}