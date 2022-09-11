#!/usr/bin/node

const requestOld = require('request');
const util = require('util');

const request = util.promisify(requestOld);

const args = process.argv.slice(2);

if (args.length !== 1) {
  process.exit(1);
}

const film = args[0];

async function main () {
  const rawData = await request(`https://swapi-api.hbtn.io/api/films/${film}/`);

  const data = JSON.parse(rawData.body);

  const characters = [];

  for (let i = 0; i < data.characters.length; i++) {
    characters.push(request(data.characters[i]).then((result) =>
      JSON.parse(result.body)
    ));
  }

  const charactersResult = await Promise.all(characters);

  for (let i = 0; i < charactersResult.length; i++) {
    console.log(charactersResult[i].name);
  }
}

main();
