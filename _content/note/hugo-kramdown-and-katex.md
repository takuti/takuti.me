---
date: 2017-05-28
lang: en
recommendations: [/note/hugo-markdown-and-mathjax/, /note/travis-gh-pages-deployment/,
  /note/normal-equation/]
title: 'Hugo meets kramdown + KaTeX #gohugo'
---

Recently, math rendering library in this page, **takuti.me**, has been switched from MathJax to KaTex to improve performance. You can check KaTeX's fast, beautiful rendering in the following articles:

- [How to Derive the Normal Equation](/note/normal-equation/)
- (Japanese)
  - [Poisson Image Editingでいい感じの画像合成ができるやつを作る on Web](/note/poisson-image-blending)
  - [TF-IDFで文書内の単語の重み付け](/note/tf-idf)
  - ["SLIM: Sparse Linear Methods for Top-N Recommender Systems"を読んだ](/note/slim)

This article describes how I have accomplished the modification.

### The Markdown + LaTeX syntax issue

I started using [Hugo](https://gohugo.io/) 1+ years ago, and ever since then, this blog has utilized [kramdown](https://kramdown.gettalong.org/index.html) & [MathJax](https://www.mathjax.org/), one of the best combinations that allows us to naturally integrate Markdown and LaTeX syntax. Following article describes the details of motivation behind the choice: [Migrate to Hugo from Jekyll: Another Solution for the MathJax+Markdown Issue](/note/hugo-markdown-and-mathjax).

As I discussed in the article, integrating Markdown and LaTeX syntax is essentially hard problem for static site generators, because `_` (underscore) plays an important role on the both syntax; many Markdown parsers (including Hugo's default Markdown processor [Blackfriday](https://github.com/russross/blackfriday)) mistakenly understand LaTeX's `_` (for subscripts) as an indicator of *italic*.

In order to work around the issue, my previous article introduced how I utilized alternative Markdown processor, namely **kramdown**.

Note that, while originally kramdown was called in my local `Rakefile`, currently the Markdown processing code has been moved to `gulpfile.js` by taking advantage of [gulp-kramdown](https://www.npmjs.com/package/gulp-kramdown):

```js
gulp.task('compile-md', function() {
  gulp.src('_content/**/*.{md,html}')
      // extract front matter as a string
      .pipe(data(function(file) {
        var contents = file.contents.toString();
        var content = contents.replace(/(---[\s\S]*?\n---\n)/m, function($1) {
          file.frontMatter = $1;
          return '';
        });

        var tweetUrls = content.match(/(https?:\/\/twitter\.com\/[a-zA-Z0-9_]+\/status\/([0-9]+)\/?)/g);

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
```

Eventually, running `$ hugo server --watch` and `$ gulp watch` simultaneously enables me to preview rendered Markdown + LaTeX contents.

### Replace MathJax with KaTeX

As many of you already noticed, math rendering of MathJax is surprisingly slow. Stressful "loading..." message always shows up on my browser! Thus, I decided to replace it with much faster alternative, [KaTeX](https://khan.github.io/KaTeX/).

Replacement itself was pretty easy; I just needed to replace MathJax's stylesheet and script definition in `<header>~</header>` (or `<footer>~</footer>`) with KaTeX's ones:

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.css" integrity="sha384-wITovz90syo1dJWVh32uuETPVEtGigN07tkttEqPv+uR2SE/mbQcG7ATL28aI9H0" crossorigin="anonymous">
```

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/katex.min.js" integrity="sha384-/y1Nn9+QQAipbNQWU65krzJralCnuOasHncUFXGkdwntGeSvQicrYkiUBwsgUqc1" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.7.1/contrib/auto-render.min.js" integrity="sha384-dq1/gEHSxPZQ7DdrM82ID4YVol9BYyU7GbWlIwnwyPzotpoc57wDw/guX8EaYGPx" crossorigin="anonymous"></script>
<script>
  renderMathInElement(document.body,
    {
        delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false},
        ]
    }
  );

  var inlineMathArray = document.querySelectorAll("script[type='math/tex']");
  for (var i = 0; i < inlineMathArray.length; i++) {
    var inlineMath = inlineMathArray[i];
    var tex = inlineMath.innerText || inlineMath.textContent;
    var replaced = document.createElement("span");
    replaced.innerHTML = katex.renderToString(tex, {displayMode: false});
    inlineMath.parentNode.replaceChild(replaced, inlineMath);
  }

  var displayMathArray = document.querySelectorAll("script[type='math/tex; mode=display']");
  for (var i = 0; i < displayMathArray.length; i++) {
    var displayMath = displayMathArray[i];
    var tex = displayMath.innerHTML;
    var replaced = document.createElement("span");
    replaced.innerHTML = katex.renderToString(tex.replace(/%.*/g, ''), {displayMode: true});
    displayMath.parentNode.replaceChild(replaced, displayMath);
  }
</script>
```

Here, `var inlineMathArray = ...` and `var displayMathArray = ...` are the magic!

For the reasons that I mentioned above, I like to use kramdown, but the Markdown processor is strongly optimized for MathJax. That is, all `$` or `$$` in article are automatically converted into `<script[type='math/tex']>` or `<script[type='math/tex; mode=display']>` by kramdown, and hence KaTeX cannot find any LaTeX statements.

In order to tackle the problem, [KaTeX officially provides workaround](https://kramdown.gettalong.org/math_engine/mathjax.html) which requires us to insert auxiliary JavaScript (jQuery) code after KaTeX itself is loaded. In my case, `var inlineMathArray = ...` and `var displayMathArray = ...` are modified version of the workaround code which does not depend on jQuery.

### Limitation

Now, the entire content rendering flow works well with:

- Static site generator **Hugo**
- External Markdown processor **kramdown** for Markdown & LaTeX syntax compatibility
- Fast math renderer **KaTeX**

However, one thing I have noticed is that, available LaTeX command in KaTeX is limited compared to MathJax. For example, previously I used `$\boldsymbol{\phi}$` in "[How to Derive the Normal Equation](/note/normal-equation/)", but KaTeX does not support the `\boldsymbol{}` command. So, for now, it has just been replaced the unsupported command with plain `\phi`.

Anyway, even though KaTeX has some limitations that MathJax does support, its performance is definitely attractive. In particular, we frequently put a lot of equations in an article in a context of machine learning and data science, choosing "better" math rendering library is important. Therefore, I strongly recommend you to use KaTeX regardless of a way to create your website (e.g., Wordpress, Jekyll, Hexo).