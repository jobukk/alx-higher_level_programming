#!/usr/bin/node
// Maximum

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const max = Math.max(...args);
  args.splice(args.indexOf(max), 1); // splice remove the first maximum value from args
  const secondMax = Math.max(...args);
  console.log(secondMax);
}
