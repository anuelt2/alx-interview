#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const fetchCharacter = (index) => {
    if (index >= characters.length) {
      return;
    }
    request(characters[index], (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(body);
        console.log(character.name);
      } else {
        console.error('Error:', error);
      }
      fetchCharacter(index + 1);
    });
  };
  fetchCharacter(0);
});
