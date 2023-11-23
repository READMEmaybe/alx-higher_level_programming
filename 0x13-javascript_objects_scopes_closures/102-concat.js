#!/usr/bin/node
const fs = require('fs');

function concatFiles (file1Path, file2Path, destinationPath) {
  const file1Content = fs.readFileSync(file1Path, 'utf-8');

  const file2Content = fs.readFileSync(file2Path, 'utf-8');

  fs.writeFileSync(destinationPath, file1Content + file2Content, 'utf-8');
}

concatFiles(process.argv[2], process.argv[3], process.argv[4]);
