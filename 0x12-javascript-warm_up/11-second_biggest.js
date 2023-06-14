#!/usr/bin/node
let firstVar = process.argv.slice(2);
const secondVar = process.argv.length;

if (secondVar <= 3) {
  console.log('0');
} else {
  firstVar = firstVar.map(Number);
  const thirVar = firstVar.sort(
    function (x, y) {
      return y - x;
    })[1];
  console.log(thirVar);
}
