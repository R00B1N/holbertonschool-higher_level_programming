#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
