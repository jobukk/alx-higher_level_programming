#!/usr/bin/node

const args = process.argv.slice(2);
let value = Number(args[0]);

function fact(value) {
    if (value === 0 || value === 1) {
        return 1;
    } else {
        return value * fact(value - 1);
    }
}

console.log(fact(value));
