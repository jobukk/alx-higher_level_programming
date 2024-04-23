#!/usr/bin/node
//factorial

const args = process.argv.slice(2);
let value = Number(args[0]);

function fact(value) {
    if (value === 0 || isNaN(value)) {
        return 1;
    } else {
        return value * fact(value - 1);
    }
}

console.log(fact(value));
