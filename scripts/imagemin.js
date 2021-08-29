// https://github.com/manaten/manaten.net/blob/1ee1f9cb8d1dabae56f0e3d9fe7cf0cb295535ab/scripts/imagemin.js
'use strict';
const fs = require('fs');

(async () => {
  const imagemin = (await import('imagemin')).default;
  const input = process.argv.filter(arg => /(png|jpe?g|gif|svg)/.test(arg));
  const plugins = [
    'gifsicle',
    'jpegtran',
    'optipng',
    'svgo'
  ].map(x => require(`imagemin-${x}`)());

  for (const inputPath of input) {
    const outputData = (await imagemin([inputPath], {plugins}))[0].data;
    console.log(`${inputPath}: ${fs.statSync(inputPath).size} byte -> ${outputData.length} byte.`);
    fs.writeFileSync(inputPath, outputData);
  }
})().catch(e => {
  console.log(e.message, e);
  process.exit(1);
});
