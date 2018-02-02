var gulp = require('gulp');
var plumber = require('gulp-plumber');
var sass = require('gulp-sass');
var data = require('gulp-data');
var kramdown = require('gulp-kramdown');
var wrapper = require('gulp-wrapper');
var request = require('sync-request');
var del = require('del');

gulp.task('clean-content', function() {
  return del(['content/**/*']);
});

gulp.task('compile-sass', function() {
  gulp.src('_scss/*.scss')
      .pipe(plumber())
      .pipe(sass())
      .pipe(gulp.dest('static/css/'));
});

gulp.task('compile-md', function() {
  gulp.src('_content/**/*.{md,html}')
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

        file.contents = new Buffer(content);
      }))

      // convert markdown content into html (except for the front matter)
      .pipe(kramdown())

      // insert the extracted front matter at the head of the converted html
      .pipe(wrapper({ header: function(file){ return file.frontMatter + '\n'; } }))

      .pipe(gulp.dest('content/'));
});

gulp.task('compile-md-preview', function() {
  // 'compile-md' task without tweet card embedding for efficiency
  gulp.src('_content/**/*.{md,html}')
      .pipe(data(function(file) {
        var contents = file.contents.toString();
        var content = contents.replace(/(---[\s\S]*?\n---\n)/m, function($1) {
          file.frontMatter = $1;
          return '';
        });

        file.contents = new Buffer(content);
      }))
      .pipe(kramdown())
      .pipe(wrapper({ header: function(file){ return file.frontMatter + '\n'; } }))
      .pipe(gulp.dest('content/'));
});

gulp.task('watch', ['clean-content', 'compile-sass', 'compile-md-preview'], function(){
  gulp.watch('_scss/*.scss', ['compile-sass']);
  gulp.watch('_content/**/*.{md,html}', ['compile-md-preview']);
});

gulp.task('default', ['clean-content', 'compile-sass', 'compile-md']);
