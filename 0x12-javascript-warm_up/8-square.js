#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < size; j++) {
    let length = '';
    for (let k = 0; k < size; k++) length += 'x';
    console.log(length);
  }
}
