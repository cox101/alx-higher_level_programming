#!/usr/bin/node

const request = require('request');

const baseUrl = 'https://swapi-api.hbtn.io/api/films/';

function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error || new Error(`Failed to fetch data from ${url}`));
      }
    });
  });
}

async function fetchCharacters(movieId) {
  try {
    const movieData = await makeRequest(baseUrl + movieId);
    const characters = JSON.parse(movieData).characters;

    for (const characterUrl of characters) {
      try {
        const characterData = await makeRequest(characterUrl);
        const characterName = JSON.parse(characterData).name;
        console.log(characterName);
      } catch (error) {
        console.error(`Failed to fetch character data: ${error.message}`);
      }
    }
  } catch (error) {
    console.error(`Failed to fetch movie data: ${error.message}`);
  }
}

const movieId = process.argv[2];
fetchCharacters(movieId);

