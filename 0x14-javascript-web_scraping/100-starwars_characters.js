#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const datad = data.characters;
  for (const i of datad) {
    req.get(i, function (err, res, body1) {
      if (err) {
        console.log(err);
      }
      const datadd = JSON.parse(body1);
      console.log(datadd.name);
    });
  }
});
