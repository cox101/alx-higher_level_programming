#!/usr/bin/node

const fs = require('fs');

const contentA = fs.readFileSync(process.argv[2], 'utf8');
const contentB = fs.readFileSync(process.argv[3], 'utf8');

const contentC = contentA.concat(contentB);

fs.writeFile(process.argv[4], contentC, 'utf8', function (err) {
  if (err) {
    console.error('Error writing file:', err);
  } else {
    console.log('Concatenation complete!');
  }
});

