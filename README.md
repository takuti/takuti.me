[takuti.me](http://takuti.me) [![Build Status](https://travis-ci.org/takuti/takuti.me.svg?branch=master)](https://travis-ci.org/takuti/takuti.me)
===

## Dependancies

### System

Hugo and direnv can be installed from homebrew:

```
$ brew install hugo
$ brew install direnv
```

### Gulp

We will use gulp tasks to compile sass files, so required npm modules are:

```
$ npm install --g gulp
$ npm install
```

### Pre-commit hook

[recommend.py](./scripts/recommend.py) depends on MeCab Japanese morphological analyzer:

```sh
brew install mecab
brew install mecab-ipadic
git clone --depth 1 git@github.com:neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n
```

## Usage

I should create new contents in *_content/* directory and sass files in *_scss/* directory both for `gulp` command.

### Generate css and html contents

```
$ gulp
```

Note that this task takes long time to get JSON from twitter, for each twitter URL.

If you want to track file modification in real-time, run

```
$ gulp watch
```

and

```
$ hugo server --watch
```

at the same time.

## License

MIT