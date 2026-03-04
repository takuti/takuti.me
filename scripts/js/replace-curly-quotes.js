#!/usr/bin/env node
const fs = require('fs');

const replaceCurlyQuotes = (filePath) => {
  const content = fs.readFileSync(filePath, 'utf8');
  const replaced = content
    .replace(/[‘’]/g, "'")
    .replace(/[“”]/g, '"');
  if (content !== replaced) {
    fs.writeFileSync(filePath, replaced, 'utf8');
    console.log(`Replaced curly quotes in: ${filePath}`);
  }
};

const files = process.argv.slice(2);
files.forEach(replaceCurlyQuotes);
