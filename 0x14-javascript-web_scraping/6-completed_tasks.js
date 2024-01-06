#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    const dict = {};
    for (const task of json) {
      if (task.completed === true) {
        if (dict[task.userId] === undefined) {
          dict[task.userId] = 0;
        }
        dict[task.userId] += 1;
      }
    }
    console.log(dict);
  }
});
