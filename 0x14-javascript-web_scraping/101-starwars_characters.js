#!/usr/bin/node

const request = require('request');
const apiUrl = 'http://swapi.co/api/films/';
let id = parseInt(process.argv[2], 10);

request(apiUrl, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    
    // Adjusting the id to fit within available film IDs (1 to 6)
    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }

    const film = films.find(film => film.episode_id === id);
    if (film) {
      const characters = film.characters;

      characters.forEach(characterUrl => {
        request(characterUrl, (err, response, body) => {
          if (!err && response.statusCode === 200) {
            console.log(JSON.parse(body).name);
          }
        });
      });
    } else {
      console.error('Film not found.');
    }
  } else {
    console.error('Failed to fetch data from SWAPI:', err);
  }
});

