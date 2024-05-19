#!/usr/bin/node
const process = require('process');
  function factorial(n) {
        if (n <= 1 || isNaN(n)) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    const m = parseInt(process.argv[2], 10);
    console.log(factorial(m))
