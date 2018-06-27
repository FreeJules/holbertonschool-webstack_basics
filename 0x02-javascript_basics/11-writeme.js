#!/usr/bin/node
let fs = require('fs');
let fileName = process.argv[2];
let content = process.argv[3];
if (!content) {
  content = '';
}
fs.writeFile(fileName, content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
