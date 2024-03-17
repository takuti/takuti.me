[takuti.me](http://takuti.me)
===

[![Build Status](https://travis-ci.org/takuti/takuti.me.svg?branch=master)](https://travis-ci.org/takuti/takuti.me)

## Dependancies

### System

Hugo and direnv can be installed from homebrew:

```
$ brew install hugo direnv git-lfs nodenv
$ nodenv install
$ nodenv rehash
```

### Gulp

We will use gulp tasks to compile sass files, so required npm modules are:

```
$ npm install -g gulp-cli textlint
$ npm install
```

### Pre-commit hook

Husky helps setting up custom pre-commit hooks:

```sh
npm run prepare
```

[recommend.py](./scripts/py/recommend.py) depends on [prelims](https://github.com/takuti/prelims) and MeCab Japanese morphological analyzer:

```sh
brew install mecab mecab-ipadic
git clone --depth 1 git@github.com:neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n
pip install -r scripts/py/requirements.txt
```

## Usage

I should create new contents in *_content/* directory and sass files in *_scss/* directory both for `gulp` command.

### Generate css and html contents

```
$ npm run build
```

Note that this task takes long time to get JSON from twitter, for each twitter URL.

If you want to track file modification in real-time, run

```
$ npm run watch
```

## License

MIT
