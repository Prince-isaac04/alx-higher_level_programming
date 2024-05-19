#!/usr/bin/node
const process = require('process');
let message = "not a number";
let num;
if(process.argv.length > 2){
    num = parseInt(process.argv[2]);
    if(!isNaN(num)){
        num = String(num);
        message = `My number : ${num};`
    }
}
console.log(message);

