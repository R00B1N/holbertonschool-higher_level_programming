#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request.get(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  else if (response.statusCode === 200) fs.writeFile(process.argv[3], body, 'utf8', (err) => { if (err) throw err; });
});
