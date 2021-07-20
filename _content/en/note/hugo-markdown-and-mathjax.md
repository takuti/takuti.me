---
categories: [Programming]
date: 2015-10-19
keywords: [hugo, markdown, site, mathjax, kramdown, jekyll, issue, correctly, files,
  rake]
lang: en
recommendations: [/note/hugo-kramdown-and-katex/, /note/travis-gh-pages-deployment/,
  /note/move-to-gh-pages/]
title: 'Migrate to Hugo from Jekyll: Another Solution for the MathJax+Markdown Issue'
---

### Migrate to Hugo from Jekyll

I had used [Jekyll](https://github.com/jekyll/jekyll) to generate this site for 1+ years. However, recently generating site took more than 10 seconds due to increasing site contents; this was really stressful when I like to check the generated site continuously (e.g. style updating).

Hence, from this article, I have migrated to [Hugo](https://github.com/spf13/hugo), and this fast static site generator can build my site less than 1 second! Migrating to Hugo from Jekyll is not so difficult because there are many useful information on the Internet such as:

- [Migrating to Hugo From Octopress](https://gohugo.io/tutorials/migrate-from-jekyll/)
- [Migrate to Hugo from Jekyll](http://nathanleclaire.com/blog/2014/12/22/migrating-to-hugo-from-octopress/)
- [spf13/spf13.com](https://github.com/spf13/spf13.com)

In particular, [spf13/spf13.com](https://github.com/spf13/spf13.com), a repository of Hugo creator's website, is practically useful to understand what we have to do.

### MathJax+Markdwon issue

In the TeX syntax, we frequently use ```_``` (underline) to render subscripts. However, at the same time, underline also indicates *italic* font in Markdwon. This situation raises a mis-converting issue; when Markdown is first parsed, MathJax might not understand TeX formulas correctly.

One solution for the issue is introduced in Hugo official support page: [MathJax Support - Issues with Markdown](http://gohugo.io/tutorials/mathjax/#issues-with-markdown:d97e838dbdddd8f0d2665b07f195e51f)

OK, we can easily fix the issue, but I don't like this solution. Putting backticks (`````` ` ``````) at the head/tail of every TeX code is so annoying...

On that point, Jekyll is great; in Jekyll configuration, we can use [kramdown](http://kramdown.gettalong.org/) (pure-Ruby Markdown convertor) as a Markdown parser, and it can correctly handle MathJax+Markdown mixed files.

### Using kramdown as a Hugo Markdown convertor

Here, I have another solution. It just to use kramdown as a Hugo Markdown convertor. Usually, Hugo requires us to put articles in *content/* directory, and it automatically converts them to .html files. However, we now create a intermediate directory like *_content/*.

First, I create Rakefile and define a task as:

```rb
require "kramdown"

namespace :converter do
  task :content do
    Dir::glob("_content/*").each do |src|
      # destination path will be "content/{filename}.html"
      dst_path = src[1..-1].sub(/(.*)\.md/, '\1.html')

      open(dst_path, "w") do |dst|
        content = open(src) { |f| f.read }

        # keep front matter
        content = content.sub(/(---.*---\n)/m, "")

        content = embedding_tweet(content)

        # write with concatenating front matter
        dst.write($1 + Kramdown::Document.new(content).to_html)
      end
    end
  end
end
```

As I mentioned before, kramdown can correctly handle MathJax+Markdown mixed files in default setting, so it works.

Next, you just need to run converter before running Hugo server: ```rake converter:content```

After the rake command, we do not have to think about Hugo Markdown converter. Even if there are some mixed articles, ```hugo server``` will generate your site correctly based on html files obtained by the rake command.

Note that we can use this technique for the other preprocessing such as sass compiling. For more detail, you can see [my actual Rakefile](https://github.com/takuti/takuti.me/blob/master/Rakefile
).

### Conclusion

I have shown you another solution for the MathJax+Markdown issue. However, since my technique requires to run preprocessing, we cannot take advantage of fast incremental building from Hugo.

If we really want to fix the issue, we have to tackle Hugo original Markdown parser and develop Go implementation of kramdown.