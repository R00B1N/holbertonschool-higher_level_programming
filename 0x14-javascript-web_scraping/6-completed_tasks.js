#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  else if (response.statusCode === 200) {
    const dict = {};
    for (let i = 0; i < JSON.parse(body).length; i++) {
      const user = JSON.parse(body)[i];
      if (user.userId in dict && user.completed === true) {
        dict[user.userId] += 1;
      } else if (!(user.userId in dict) && user.completed === true) {
        dict[user.userId] = 1;
      }
    }
    console.log(dict);
  }
});
