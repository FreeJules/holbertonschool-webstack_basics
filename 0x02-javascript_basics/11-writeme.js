#!/usr/bin/node
let fs = require('fs');
let fileName = process.argv[2];
let content;
if (process.argv.length < 4) {
  content = '';
} else {
  content = process.argv[3];
}
fs.writeFile(fileName, content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
