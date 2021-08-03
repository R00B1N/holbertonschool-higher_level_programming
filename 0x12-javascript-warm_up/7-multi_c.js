#!/usr/bin/node
const x = Number(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
