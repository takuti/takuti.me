const { src, dest, watch, series, parallel } = require('gulp');
const plumber = require('gulp-plumber');
const sass = require('gulp-sass');
const data = require('gulp-data');
const kramdown = require('gulp-kramdown');
const wrapper = require('gulp-wrapper');

const request = require('sync-request');
const del = require('del');
const { highlight, highlightAuto, getLanguage } = require('highlight.js');
const { execSync } = require('child_process');
const browserSync = require('browser-sync');

const { Renderer } = require('kramed');
const renderer = new Renderer();
renderer.table = (header, body) =>
  // table container + original renderer
  // https://github.com/GitbookIO/kramed/blob/9d96b7ac9e063b94d51423d8cd450f4a7c7eb1f3/lib/renderer.js#L96-L105
  '<div class="table-container">\n'
    + '<table>\n'
    + '<thead>\n'
    + header
    + '</thead>\n'
    + '<tbody>\n'
    + body
    + '</tbody>\n'
    + '</table>\n'
    + '</div>\n';

let watching = false;
const turnWatchingOn = () => {
  watching = true;
};

const cleanContent = () => del(['content/**/*']);

const compileSass = () =>
  src('_scss/*.scss')
    .pipe(plumber())
    .pipe(sass({ outputStyle: 'compressed' }))
    .pipe(dest('static/css/'));

const compileContent = () =>
  src('_content/**/*.{md,html}')
    // extract front matter as a string
    .pipe(data((file) => {
      const contents = file.contents.toString();
      let content = contents.replace(/(---[\s\S]*?\n---\n)/m, ($1) => {
        file.frontMatter = $1;
        return '';
      });

      if (!watching) {
        const tweetUrls = content.match(/(https?:\/\/twitter\.com\/[a-zA-Z0-9_]+\/status(es)?\/([0-9]+)\/?)/g);

        // convert all tweet urls into tweet cards
        if (tweetUrls !== null) {
          for (let url of tweetUrls) {
            const id = /\/([0-9]+)\/?/g.exec(url)[1];
            const res = request('GET', 'https://api.twitter.com/1/statuses/oembed.json?id=' + id);

            const tweetCard = JSON.parse(res.getBody('utf8')).html;
            content = content.replace(url, tweetCard);
          }
        }
      }

      file.contents = new Buffer.from(content);
    }))

    // convert markdown content into html (except for the front matter)
    .pipe(kramdown({
      highlight: (code, lang) => {
        try {
          const f = getLanguage(lang) ? highlight : highlightAuto;
          return f(lang, code).value;
        } catch (TypeError) {
          return code;
        }
      },
      renderer: renderer
    }))

    // insert the extracted front matter at the head of the converted html
    .pipe(wrapper({ header: (file) => file.frontMatter + '\n' }))

    .pipe(dest('content/'));

const buildHugo = (done) => {
  const res = execSync(
    watching ? 'hugo -D -b="http://localhost:3000"' : 'hugo -v',
    { encoding: 'utf-8' }
  );
  console.log(res);
  done();
};

const watchFiles = () => {
  turnWatchingOn();

  browserSync.init({
    files: ['public/**/*'],
    server: {
      baseDir: 'public/'
    },
    port: 3000,
    open: true
  });

  watch('_scss/*.scss', { ignoreInitial: false }, compileSass);
  watch('_content/**/*.{md,html}', { ignoreInitial: false }, series(compileContent, buildHugo));
};

exports.watch = series(cleanContent, watchFiles);
exports.default = parallel(
  compileSass,
  series(cleanContent, compileContent, buildHugo)
);
