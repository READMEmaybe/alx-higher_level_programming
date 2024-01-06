#!/usr/bin/node
const request = require('request');

async function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (err, response, body) {
      if (err) {
        reject(err);
      } else {
        const json = JSON.parse(body);
        resolve(json.name);
      }
    });
  });
}

async function fetchData () {
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

  try {
    const body = await new Promise((resolve, reject) => {
      request(url, function (err, response, body) {
        if (err) {
          reject(err);
        } else {
          resolve(body);
        }
      });
    });

    const json = JSON.parse(body);

    for (const character of json.characters) {
      const characterName = await getCharacterName(character);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();
