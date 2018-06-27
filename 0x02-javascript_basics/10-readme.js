#!/usr/bin/node
let fs = require('fs');
let fileName = process.argv[2];
fs.readFile(fileName, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
