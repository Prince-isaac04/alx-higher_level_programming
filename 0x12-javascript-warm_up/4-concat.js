#!/usr/bin/node
const process = require('process');
const args2 = process.argv[2];
const args3 = process.argv[3];
if(args2 === undefined || args3 === undefined){
	console.log("invald input");
}
else
{
	console.log(`${args2} is ${args3}`);
}
