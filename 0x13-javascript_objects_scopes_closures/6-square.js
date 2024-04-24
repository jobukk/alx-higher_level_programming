#!/usr/bin/node
class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
