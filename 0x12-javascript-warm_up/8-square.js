#!/usr/bin/node
const process = require('process');

const times = parseInt(process.argv[2], 10);

if (isNaN(times)) {
    console.log("Missing size");
} else {
    let i = 0;
    while (i < times) {
        console.log('X'.repeat(times));
        i++;
    }
}

