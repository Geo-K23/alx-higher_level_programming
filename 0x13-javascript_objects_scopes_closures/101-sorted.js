#!/usr/bin/node
const dict = require('./101-data').dict;
const dctKeys = Object.keys(dict);
const values = Object.values(dict);
let sorted;
const result = {};
// loop over the value
for (let i = 0; i < values.length; i++) {
  result[JSON.stringify(values[i])] = [];
  sorted = dctKeys.filter(key => dict[key] === values[i]);
  sorted.forEach(item => result[JSON.stringify(values[i])].push(item));
}
console.log(result);
