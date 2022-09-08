---
categories: [Programming]
date: 2020-11-28
images: [/images/resume-in-html/resume-latex.png, /images/resume-in-html/resume-html.png]
lang: en
title: Are You Still Writing a Resume in Word/LaTeX?
lastmod: '2022-09-02'
keywords: [resume, html, latex, writing, web, pdf, website, customizability, tex,
  font]
recommendations: [/note/why-job-title-matters/, /note/hugo-kramdown-and-katex/, /note/new-year-resolution-2017/]
---

Over the past few years, I have been using LaTeX for writing a resume. 

![resume-latex](/images/resume-in-html/resume-latex.png)

While it *looks* so professional especially in the academic world, there is a space for improvement in terms of maintainability, flexibility, and customizability.

Thus, I have started writing a resume in HTML and publishing it in the form of both PDF file and static website:

- **[takuti.me/cv](https://takuti.me/cv)**
- [GitHub repository](https://github.com/takuti/cv)

![resume-latex](/images/resume-in-html/resume-html.png)

Notice that the implementation is fully based on **[lucas-clemente/cv](https://github.com/lucas-clemente/cv)**. The template builds a static resume website by using [Broccoli.js](https://broccoli.build/), and a PDF version is dynamically rendered via [Screen Capture with PhantomJS](https://phantomjs.org/screen-capture.html). In fact, the code is slightly out of date, but it's fine and I can further tune and tweak as much as I want because it's just a simple HTML and JavaScript stuff.

### Pros

Most importantly, I don't necessarily have to install TeX on my laptop anymore. After I graduated from the master's program and joined a company as an engineer, I have had a very limited opportunity to write an academic paper in LaTeX (only twice in the last 3-4 years[^1][^2]). That is, resume writing was the only reason why I install the TeX environment every time I set up a laptop. It was so frustrating for me as it keeps causing problems and requires spending quite a bit of time on resolving them. HTML and JavaScript, on the other hand, are straightforward that make the situation a lot easier and simpler.

Second, I can make my resume as much descriptive as I want by fully leveraging the markup language for creating bullet/numbered lists and inserting links into the texts. Since I'm not good at LaTeX, to be honest, I needed to keep my LaTeX-based resume as simple as possible so that it doesn't depend on any advanced macros. Consequently, the use of web technology enables me to flexibly customize the contents arbitrarily.

Additionally, in terms of customizability, web-based resume writing unlocks new possibilities such as adding visually stimulating icons with [Font Awesome](https://fontawesome.com/). It means that we can be more creative and make the resume unique and attractive for the readers; it is important to note that a resume is ultimately delivered to a certain reader (e.g., hiring manager, business partner), and hence readability, attractiveness, and uniqueness are the key factors that define a good resume.

### Cons

Overall, I prefer creating a resume in HTML to taking the traditional options such as LaTeX and Word. However, at the same time, I can imagine some potential drawbacks.

First, the web-based ones may bring a less professional look and feel. I believe it's okay in most cases, but someone could think your resume is not serious when they look at the icons and web-safe fonts. We'd then need to spend more time on designing the website and carefully choosing a layout and font. In my case though, I have already submitted a PDF version of **[takuti.me/cv](https://takuti.me/cv)** to a couple of different organizations, and there have been no problems so far.

Meanwhile, your excessive creativity & familiarity with web technology may be harmful if you over-decorate a resume. We should not forget the fundamental purpose of a resume, which gives an accurate description of your career in a readable way so that you can proceed to an interview process and/or establish a good relationship with collaborators. Just let resume do the job.

### Bottom line

I have recreated my resume in HTML and stopped using LaTeX. The change makes the resume more maintainable, and it motivates me to keep the content updated. A resume is a "portfolio" of your life that must be read by someone else, and hence choosing the most comfortable way of writing is highly important for each of us to properly convey the information.

That's how I see resume writing, and I hope my case inspires you to rethink how to create/structure yours.

[^1]: [Query-Based Simple and Scalable Recommender Systems with Apache Hivemall](https://dl.acm.org/doi/10.1145/3240323.3241592)
[^2]: [Zero-Coding UMAP in Marketing: A Scalable Platform for Profiling and Predicting Customer Behavior by Just Clicking on the Screen](https://dl.acm.org/doi/10.1145/3314183.3324970)