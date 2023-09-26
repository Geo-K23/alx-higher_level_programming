#!/usr/bin/node

// Importing the fs (file system) module
const fs = require('fs');

// Get the file path from the command line argument
const filepath = process.argv[2];

// Read the content of the file in utf-8 encoding
fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurred during reading, print the error object
    console.log(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
