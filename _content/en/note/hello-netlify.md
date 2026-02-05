---
categories: [Engineering]
date: 2019-08-31
images: [/images/hello-netlify/netlify-republished.png, /images/hello-netlify/netlify-git-lfs-enabled.png]
lang: en
title: Hello Netrify for Hosting a Static Site
lastmod: '2022-01-23'
keywords: [netlify, lfs, pages, git, github, site, scripts, travis, hugo, publishing]
recommendations: [/note/travis-gh-pages-deployment/, /note/move-to-gh-pages/, /note/hugo-markdown-and-mathjax/]
---

For the recent two years, I have used GitHub Pages to publish my [takuti.me](/) site built by Hugo:

- [Moving to GitHub Pages](/note/move-to-gh-pages)
- [Deploying Static Site to GitHub Pages via Travis CI](/note/travis-gh-pages-deployment)

Meanwhile, this article you are reading is distributed by [Netlify](https://netlify.com) as of Aug 31, 2019.

The motivation of this change is simply based on my interests; while I have no strong complaints to GitHub Pages, Netlify looks nicer and fitting my use case for the following reasons.

### Auto publishing

First of all, synchronization with a GitHub repository and setting up auto-publishing are super easy. It has been completed in a couple of clicks on a Netlify's configuration view.

In the case of GitHub Pages + Hugo, I needed to configure extra things like [CI/CD using Travis](/note/travis-gh-pages-deployment). It is technically stimulating, but I like to stay focus more on writing articles itself rather than spending a long time for implementing and managing the build & deploy scripts. Plus, site deployment on Netlify finishes much faster than the CI scripts.

Importantly, Netlify allows the sites to easily fall back into a specific release (i.e., GitHub commit); if you crash your web site as a result of updating configurations, the only thing you need to immediately do is just manually re-publishing the previous version on Netlify:

![netlify-republished](/images/hello-netlify/netlify-republished.png)

### Git LFS support

Second, Netlify works with [Git LFS](https://git-lfs.github.com). Even though it significantly simplifies your source repository by uploading multimedia contents to third-party places, unfortunately, [GitHub Pages does not support the functionality](https://github.com/git-lfs/git-lfs/issues/3498). 

In fact, [Netlify Large Media](https://www.netlify.com/docs/large-media/) is Nelify's hosted Git LFS environment, but Hugo has no way to work with it, while there is [ongoing discussion in the community](https://github.com/gohugoio/hugo/issues/5749). Alternatively, you can simply use GitHub's native capability to store your large files with Git LFS.

Installation is minimal and straightforward:

```sh
brew install git-lfs
```

Currently, my repository is tracking the following static files:

```sh
git lfs track "static/docs/**" "static/images/**/*.jpg" "static/images/**/*.jpeg" "static/images/**/*.png"
```

```
$ cat .gitattributes
static/docs/** filter=lfs diff=lfs merge=lfs -text
static/images/**/*.jpg filter=lfs diff=lfs merge=lfs -text
static/images/**/*.jpeg filter=lfs diff=lfs merge=lfs -text
static/images/**/*.png filter=lfs diff=lfs merge=lfs -text
```

```sh
git add .gitattributes
```

That's it. The raw static files do not make your repository huge any more.  

It should be noted that we need to set an environment variable `GIT_LFS_ENABLED=true` for Netlify build script, so that Netlify clones the actual files from Git LFS before building a Hugo site:

![netlify-git-lfs-enabled](/images/hello-netlify/netlify-git-lfs-enabled.png)

### Asset optimization

Finally, their asset optimization capability potentially replaces what my site is explicitly doing in the [build script](https://github.com/takuti/takuti.me/blob/a17154d08254e0d70056becff59f5507e711f814/gulpfile.js#L18) and [Git pre-commit hook](https://github.com/takuti/takuti.me/blob/535d3bc828c6deea280df826a4588edca364cbe4/scripts/imagemin.js). Now, I may be able to delete these scripts because, if we configure properly, Netlify automatically compresses CSS, JS, and image files for efficiency.

The consequence is similar to what I achieved as a result of auto-publishing. That is, the build scripts become simpler and easier to manage, and I can concentrate more on contents of the site.

For the reasons that I mentioned above, I decided to say goodbye to GitHub Pages and start using Netlify. Overall, I am really satisfied with its simplicity and efficiency. 

I heard that deploying a single-page application is another popular use case of Netlify. Looking forward to having a chance to test it soon.