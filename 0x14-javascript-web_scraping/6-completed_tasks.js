#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

const completedTasks = {};
request.get(url, (err, res, body) => {
  if (err) throw err;
  const todos = JSON.parse(body);
  for (let k = 0; k < todos.length; k++) {
    const key = todos[k].userId;
    if (todos[k].completed) {
      if (!(key in completedTasks)) {
        completedTasks[key] = 1;
      } else {
        completedTasks[key] += 1;
      }
    }
  }
  console.log(completedTasks);
});
