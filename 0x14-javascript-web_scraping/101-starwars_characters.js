#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

req(url, function (err, respon, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});


function printCharacters (characters, index) {
  req(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) (
        printCharacters(characters, index + 1)
      )
    }
  });
}
