// OOP (Object Oriented Programming)
/*
1. Clases y Objetos
2. Abstraccion
3. Encapsulamiento (public, protected, private)
4. Herencia
5. Polimorfismo

*/

class Persona {
    nombre;
    apellido;
    rut;

    constructor(nombre, apellido, rut){
        this.nombre = nombre;
        this.apellido = apellido;
        this.rut = rut;
    }

    comer(){}
    caminar(){}
    saludar(){
        return `Hola, Soy ${this.nombre} ${this.apellido}`
    }
}

let per1 = new Persona("John", "Doe", "123456789")
let per2 = new Persona("Jane", "Doe", "123456780")
console.log(per1)
console.log(per2)

console.log(per1.saludar())
console.log(per2.saludar())


class Estudiante extends Persona {
    grado;
    facultad;

    constructor(nombre, apellido, rut, grado, facultad){
        super(nombre, apellido, rut)
        this.grado = grado;
        this.facultad = facultad;
    }

    saludar(){
        return `Hola, Soy el estudiante ${this.nombre} ${this.apellido} de la facultad de ${this.facultad}` 
    }

}

let est1 = new Estudiante("John", "Doe", "123456789", "1ro", "Ingenieria")
let est2 = new Estudiante("Jane", "Doe", "123456780", "4to", "Medicina")

console.log(est1.saludar())
console.log(est2.saludar())

/* function saludar(){
    return "Saludar 1"
}

function saludar(){
    return "Saludar 2"
}

console.log(saludar()) */