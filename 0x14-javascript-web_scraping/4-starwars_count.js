#!/usr/bin/node

const req = require('request');
const epNum = 18;
const URL_API = process.argv[2];

req(URL_API, function (error, response, body) {
  if (!error) {
    const result = JSON.parse(body).results;
    console.log(result.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith(`/${epNum}/`))
        ? count + 1
        : count;
    }, 0));
  }
});
