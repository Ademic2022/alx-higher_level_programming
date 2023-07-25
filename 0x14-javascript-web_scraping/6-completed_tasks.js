#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  const data = JSON.parse(body);
  const completedTasks = {};

  data.forEach((task) => {
    if (task.completed) {
      const userId = task.userId;
      completedTasks[userId] = (completedTasks[userId] || 0) + 1;
    }
  });

  console.log(completedTasks);
});
