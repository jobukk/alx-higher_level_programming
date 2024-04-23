#!/usr/bin/node

const args = process.argv.slice(2);
const str = 'x';
if (args[0] === undefined || isNaN(args[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log(str.repeat(args[0]));
  }
}
