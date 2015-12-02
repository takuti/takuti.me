var gulp = require('gulp');
var sass = require('gulp-sass');
var data = require('gulp-data');
var kramdown = require('gulp-kramdown');
var wrapper = require('gulp-wrapper');

gulp.task('compile-sass', function() {
  gulp.src('_scss/*.scss')
      .pipe(sass())
      .pipe(gulp.dest('static/style/'));
});

gulp.task('compile-md', function() {
  gulp.src('_content/**/*.md')
      // extract front matter as a string
      .pipe(data(function(file) {
        var contents = file.contents.toString();
        var content = contents.replace(/(---[\s\S]*?\n---\n)/m, function($1) {
          file.frontMatter = $1;
          return '';
        });
        file.contents = new Buffer(content);
      }))

      // convert markdown content into html (except for the front matter)
      .pipe(kramdown())

      // insert the extracted front matter at the head of the converted html
      .pipe(wrapper({ header: function(file){ return file.frontMatter + '\n'; } }))

      .pipe(gulp.dest('content/'));
});

gulp.task('copy-html', function() {
  gulp.src('_content/**/*.html')
      .pipe(gulp.dest('content/'));
});

gulp.task('watch', function(){
  gulp.watch('_scss/*.scss', ['compile-sass']);
  gulp.watch('_content/**/*.md', ['compile-md']);
  gulp.watch('_content/**/*.html', ['copy-html']);
});

gulp.task('default', ['compile-sass', 'compile-md', 'copy-html']);
