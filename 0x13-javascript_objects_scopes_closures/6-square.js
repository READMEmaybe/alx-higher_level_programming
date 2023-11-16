#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      console.log((c === undefined ? 'X' : c).repeat(this.width));
    }
  }
}
module.exports = Square;
