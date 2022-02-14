---
categories: [Conference]
date: 2015-10-13
images: [/images/jekyll/2015-10-13-pycon-entrance.jpg, /images/jekyll/2015-10-13-pycon-closing.png]
lang: en
title: 'PyCon JP 2015 #pyconjp'
keywords: [python, talk, pycon, pandas, possibilities, grpc, talks, programming, 範囲,
  morphological]
recommendations: [/note/hello-faust/, /note/hivemall-events-2018-autumn/, /note/hivemall-pyspark/]
---

Following [phpcon2015](http://phpcon.php.gr.jp/2015/), I have attended [PyCon JP 2015](https://pycon.jp/2015/en/) at the end of last week.

![pycon-entrance](/images/jekyll/2015-10-13-pycon-entrance.jpg)

Although I have more than 8-year programming experience, I first write Python code only a year ago. However, despite the really short-term experience, now Python is definitely one of my most favorite programming languages. I use Python in many different purposes such as research, private projects, part-time job, and competitive programming.

My usage scenes of Python is really wide-ranging, right? Actually, the theme of PyCon JP 2015 was ***Possibilities of Python***, and everyone agrees with its possibilities. Also, [the conference schedule](https://pycon.jp/2015/en/schedule/) clearly illustrates possibilities of Python; we can see a wide variety of talks: hardware-related (robotics, FPGA), web development, data science and machine learning.

Due to too much conference contents, summarizing them one-by-one is hard for me. So, I just list some GitHub repositories based on my stars during the conference:

- [getsentry / sentry](https://github.com/getsentry/sentry)
	- Keynote talk focused on Python technologies around error/crash reporting.
	- Highly practical and interesting keynote.
- [JukkaL / mypy](https://github.com/JukkaL/mypy)
- [python / typeshed](https://github.com/python/typeshed)
	- Talk about Python 3.x and type hints (from 3.5).
	- I still use Python 2.7, but this talk made me want to use 3.x.
- [google / protobuf](https://github.com/google/protobuf)
- [grpc / grpc](https://github.com/grpc/grpc)
	- Talk about gRPC and Kubernetes by Googler.
	- Good introduction to modern infrastructure, including concepts of containers.
- [mocobeta / janome](https://github.com/mocobeta/janome)
	- Japanese morphological analyzer in Python.
	- Easy to follow the talk about how Japanese morphological analyzer works.
- [renyuanL / pythonTurtleInChinese](https://github.com/renyuanL/pythonTurtleInChinese)
	- Translate Python code into Chinese like *for i in 範囲(100):* ("範囲" means "range" in English)
	- Thought-provoking talk on programming education.
- [c-bata / pandas-validator](https://github.com/c-bata/pandas-validator)
- [blaze / dask](https://github.com/blaze/dask)
- [fabric / fabric](https://github.com/fabric/fabric)
- [mitsuhiko / click](https://github.com/mitsuhiko/click)
- [airtoxin / pysqldf](https://github.com/airtoxin/pysqldf)
	- Lightning talks by 10 speakers.
	- Some of them introduced very useful tools.
	- Especially, since I became curious about command-line tool development with [Click](https://github.com/mitsuhiko/click), I have tried it by creating [tiny twitter client](https://github.com/takuti/hiss) after the talk.	

Of course, there were many other interesting talks. In particular, presentations about [tweet analysis](http://www.youtube.com/watch?v=wO5qvjAFMyg), [semantic web](http://intro2libsys.info/pycon-jp-2015), [pandas internals](https://speakerdeck.com/sinhrks/pyconjp-2015-pandas-internals) and [ad science](http://www.slideshare.net/hagino_3000/ss-53786917) were good because these topics were very close to my current interests.

Since I am working on data science and machine learning research, one of the most impressive things is that several talks mentioned [pandas](http://pandas.pydata.org/), Python data analysis library. I have realized how pandas (and IPython notebooks) are important tools for data scientists.

![pycon-closing](/images/jekyll/2015-10-13-pycon-closing.png)

PyCon JP 2015 was really stimulating, and this was great opportunity to see **possibilities of Python**. I like to learn more about Python and use this language and related tools more effectively. And, importantly, I will use Python 3.x starting today :)