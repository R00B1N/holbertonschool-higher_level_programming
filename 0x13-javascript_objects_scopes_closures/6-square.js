#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    let letter;
    if (c === undefined) {
      letter = 'X';
    } else {
      letter = c;
    }
    let i;
    let l = '';
    for (i = 0; i < this.width; i++) {
      l += letter;
    }
    for (i = 0; i < this.height; i++) {
      console.log(l);
    }
  }
}
module.exports = Square;
