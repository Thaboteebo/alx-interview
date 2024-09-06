#!/usr/bin/node


const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieID}/`;


request(url, (error, response, body) => {
	if (error) {
		console.error('error:', error);
		return;
	}

	const film = JSON.parse(body);const characters = film.characters;
	characters.forEach((character) => {
		request(character, (error, response, body) => {
			if (error) {
				console.error('error:', error);
				return;
			}

			const characterData = JSON.parse(body);
			console.log(characterData.name);
		});
	});
});
