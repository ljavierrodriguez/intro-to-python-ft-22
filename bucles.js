// Bucles
/* 

for (contador; condicion; incremento){
    sentencias
}

for (indice in coleccion){
    sentencias
}

for (valor of coleccion){
    sentencias    
}

while (condicion){
    sentencias
}

do {
    sentencias
} while(condicion)


*/

for(let i = 1; i <= 10; i++){
    console.log(i)
}

let nombres = ["Hugo", "Paco", "Luis"]

for(let indice in nombres){
    console.log(nombres[indice])
}

for (let nombre of nombres){
    console.log(nombre)
}

let i = 1;
while (i <= 10){
    console.log(i)
    i++
}