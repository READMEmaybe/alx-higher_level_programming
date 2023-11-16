#!/usr/bin/node
exports.esrever = function (list) {
  const out = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    out[j] = list[i];
  }
  return out;
};
