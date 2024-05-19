#!/usr/bin/node
const process = require('process');
let message;
if(process.argv.lenght === 3){
	message = "argument found";
}
else if(process.argv.lenght < 3){
	message = "no argument";
}
else{
message = "argument found"
}
console.log(message);


