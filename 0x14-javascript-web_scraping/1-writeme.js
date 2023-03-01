#!/usr/bin/node
const files = require('fs');
files.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
