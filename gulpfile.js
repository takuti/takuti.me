var gulp = require('gulp');
var plumber = require('gulp-plumber');
var sass = require('gulp-sass');
var data = require('gulp-data');
var kramdown = require('gulp-kramdown');
var wrapper = require('gulp-wrapper');
var request = require('sync-request');
var del = require('del');
var hjs = require('highlight.js');

var kramed = require('kramed');
var renderer = new kramed.Renderer();
renderer.table = function (header, body) {
  // table container + original renderer
  // https://github.com/GitbookIO/kramed/blob/9d96b7ac9e063b94d51423d8cd450f4a7c7eb1f3/lib/renderer.js#L96-L105
  return '<div class="table-container">\n'
    + '<table>\n'
    + '<thead>\n'
    + header
    + '</thead>\n'
    + '<tbody>\n'
    + body
    + '</tbody>\n'
    + '</table>\n'
    + '</div>\n';
};

function cleanContent() {
  return del(['content/**/*']);
}

function compileSass() {
  return gulp.src('_scss/*.scss')
      .pipe(plumber())
      .pipe(sass({outputStyle: 'compressed'}))
      .pipe(gulp.dest('static/css/'));
}

function compileMd() {
  return gulp.src('_content/**/*.{md,html}')
      // extract front matter as a string
      .pipe(data(function(file) {
        var contents = file.contents.toString();
        var content = contents.replace(/(---[\s\S]*?\n---\n)/m, function($1) {
          file.frontMatter = $1;
          return '';
        });

        var tweetUrls = content.match(/(https?:\/\/twitter\.com\/[a-zA-Z0-9_]+\/status(es)?\/([0-9]+)\/?)/g);

        // convert all tweet urls into tweet cards
        if (tweetUrls !== null) {
          for (var url of tweetUrls) {
            var id = /\/([0-9]+)\/?/g.exec(url)[1];
            var res = request('GET', 'https://api.twitter.com/1/statuses/oembed.json?id=' + id);

            var tweetCard = JSON.parse(res.getBody('utf8')).html;
            content = content.replace(url, tweetCard);
          }
        }

        file.contents = new Buffer.from(content);
      }))

      // convert markdown content into html (except for the front matter)
      .pipe(kramdown({
        highlight: function (code, lang) {
          try {
            return hjs.highlight(lang, code).value;
          } catch (TypeError) {
            return code;
          }
        },
        renderer: renderer
      }))

      // insert the extracted front matter at the head of the converted html
      .pipe(wrapper({ header: function(file){ return file.frontMatter + '\n'; } }))

      .pipe(gulp.dest('content/'));
}

function compileMdPreview() {
  // 'compile-md' task without tweet card embedding for efficiency
  return gulp.src('_content/**/*.{md,html}')
      .pipe(data(function(file) {
        var contents = file.contents.toString();
        var content = contents.replace(/(---[\s\S]*?\n---\n)/m, function($1) {
          file.frontMatter = $1;
          return '';
        });

        file.contents = new Buffer.from(content);
      }))
      .pipe(kramdown({
        highlight: function (code, lang) {
          try {
            return hjs.highlight(lang, code).value;
          } catch (TypeError) {
            return code;
          }
        },
        renderer: renderer
      }))
      .pipe(wrapper({ header: function(file){ return file.frontMatter + '\n'; } }))
      .pipe(gulp.dest('content/'));
}

const buildPreview = gulp.parallel(compileSass, gulp.series(cleanContent, compileMdPreview));

function watchFiles() {
  gulp.watch('_scss/*.scss', compileSass);
  gulp.watch('_content/**/*.{md,html}', compileMdPreview);
}

const watch = gulp.series(buildPreview, watchFiles);

const build = gulp.parallel(compileSass, gulp.series(cleanContent, compileMd));

exports.watch = watch;
exports.default = build;
