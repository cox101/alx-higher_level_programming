#!/usr/bin/node

const { dict } = require('./101-data');

const myValue = Object.entries(dict).reduce((acc, [key, value]) => {
  if (!acc[value]) {
    acc[value] = [key];
  } else {
    acc[value].push(key);
  }
  return acc;
}, {});

console.log(myValue);

