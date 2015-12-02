var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('compile-sass', function() {
  gulp.src('_scss/*.scss')
      .pipe(sass())
      .pipe(gulp.dest('static/style/'));
});

gulp.task('watch', function(){
  gulp.watch('_scss/*.scss', ['compile-sass']);
});

gulp.task('default', ['compile-sass']);
