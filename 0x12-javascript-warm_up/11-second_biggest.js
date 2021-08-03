#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2).map(Number);
  const m = Math.max(...list);
  const i = list.indexOf(m);
  list.splice(i, 1);
  console.log(Math.max(...list));
}
