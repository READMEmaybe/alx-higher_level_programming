#!/usr/bin/node
const dict = require('./101-data.js').dict;

function groupDictByValue (sourceDict) {
  const result = {};

  for (const key in sourceDict) {
    const value = sourceDict[key];

    if (result[value]) {
      result[value].push(key.toString());
    } else {
      result[value] = [key.toString()];
    }
  }

  return result;
}

console.log(groupDictByValue(dict));
