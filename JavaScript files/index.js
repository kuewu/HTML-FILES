console.log(`hello`);
//> window.alert(`this is an alert`);
let me = " rakiya";
let you = " aunty"

console.log(`hello world`);
document.getElementById("myh1").textContent = `hello ${me}`;

document.getElementById("myp").textContent = `hello pretty ${you}`;
let age = 67;
let price = 10.9;
let gpa = 3.555;
console.log(`you are ${age} years old`);
console.log(`the pice of the good is ${price} ghc`);
console.log(`my current gpa is ${gpa}`);
console.log(typeof age)
console.log(typeof price)
console.log(typeof gpa)



// lets do strings
let firstname = `sis`;
let favoritefood = `pizza`;
console.log(typeof firstname);
console.log(`your first name is ${firstname}`);
console.log(`my favorite food is ${favoritefood}`);

//let do bolean
let online = false;
console.log(`bro is online: ${online}`);



// lets do operands and their various operators
let students = 31;
students = students + 1;
students = students - 1;
students = students * 2;
students = students / 2;
students = students ** 2;
let extrastudent = students % 3;
console.log(students);
console.log(extrastudent);

//> how to accept user input
//> let usernames;
//>usernames = window.prompt(`what is your username? `)
//>console.log(usernames);


//> professional way
let username;
document.getElementById("mysubmit").onclick = function() {
    username = document.getElementById("mytext").value;
    console.log(`your name is ${username}`)
    document.getElementById("myh11").textContent = `hello ${username}`
}



//> let do type conversion
let pamela = window.prompt("how old are you? ");
pamela = Number(pamela);
pamela += 10;
console.log(pamela);

let x = 'pizza';
let y = "pizza";
let z = "pizza";

x = Number(x);
y = String(y);
z = Boolean(z);

console.log(x, typeof x);
console.log(y, typeof y);
console.log(z, typeof z);



//> moving to the use of constant
const PI = 3.14159;
let circumference;
5

let radius;
document.getElementById("myresults").onclick = function() {
    radius = document.getElementById("myrnum").value;
    radius = Number(radius);

    circumference = 2 * PI * radius;
    console.log(circumference);
    document.getElementById("myh3").textContent = circumference + "cm";
}