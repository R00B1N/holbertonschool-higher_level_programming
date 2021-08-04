#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let l = '';
    for (i = 0; i < this.width; i++) {
      l += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(l);
    }
  }
}
module.exports = Rectangle;
