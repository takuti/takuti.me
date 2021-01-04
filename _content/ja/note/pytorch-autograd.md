---
aliases: [/note/pytorch-autograd/]
categories: [プログラミング, 機械学習]
date: 2017-09-23
keywords: [pytorch, autograd, euroscipy, 損失, 変数, パラメータ, ステップ, 気持ち, 更新, soumith]
lang: ja
recommendations: [/ja/note/pytorch-mf/, /ja/note/euroscipy-2017/, /ja/note/adjusting-for-oversampling-and-undersampling/]
title: PyTorchのautogradと仲良くなりたい
---

（希望）

せっかく[EuroScipy 2017](/note/euroscipy-2017)でFacebook AI researchの[Soumith Chintala](https://twitter.com/soumithchintala)氏から直に **[PyTorch](https://github.com/pytorch/pytorch)** のお話を聞いたので、触ってみるしかないぞ！と思いました。

特に、PyTorchのウリだと言っていた **autograd**（自動微分）が気になるので、まずは[公式チュートリアル](http://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)から入門してみる。

`x` という変数を `requires_grad=True` オプション付きで定義する。値は1：

```py
import torch
from torch.autograd import Variable
```

```py
# [x1, x2; x3, x4] = [1, 1; 1, 1]
x = Variable(torch.ones(2, 2), requires_grad=True)
```

"PyTorch is numpy alternative" と言うだけあって、配列（テンソル）操作は困らない。

そして一次関数 `y = x + 1` を定義：

```py
# [y1, y2; y3, y4] = [x+2, x+2; x+2, x+2]
y = x + 2
```

さらに `y` を使って二次関数をつくる：

```py
# zi = 3 * (xi + 2)^2
z = y * y * 3
```

コメントの通り、`z = y * y * 3` を展開すれば `z = (x + 2) * (x + 2) * 3` です。

関数の出力値 `out` を適当な値 `z.mean()` とする。`z` の各要素が `zi = 3 * (xi + 2)^2` だったので、 その平均値は：

```py
# out = 1/4 * (z1 + z2 + z3 + z4)
#     = 1/4 * (3 * y1^2 + 3 * y2^2 + 3 * y3^2 + 3 * y4^2)
#     = 1/4 * (3 * (x1 + 2)^2 + 3 * (x2 + 2)^2 + 3 * (x3 + 2)^2 + 3 * (x4 + 2)^2)
out = z.mean()
```

`out` の勾配：

```py
# d(out)
out.backward()
```

`x` について：

```py
# d(out) / d(xi) = 1/4 * 2 * 3 * (xi + 2) = 3/2 * (xi + 2)
print(x.grad)  # => [4.5, 4.5; 4.5, 4.5]
```

最初に `xi = 1` としていたので、 `xi.grad = 3/2 * (xi + 2) = 3/2 * (1 + 2) = 4.5` ということになる。

なるほど、`autograd.Variable.backward()` がキモらしい。そしてこのチュートリアルだけでも、PyTorchの『線形なコードフローを推奨する』という思想が強く実感できる。

ここでもうひとつ、実践的な例として[ロジスティック回帰による Bag-of-Words の二値分類](http://pytorch.org/tutorials/beginner/nlp/deep_learning_tutorial.html#example-logistic-regression-bag-of-words-classifier)を試してみる。

詳細は割愛しつつ、肝心のSGDによる学習の部分のコードを抜き出してみる：

```py
# this classifier outputs log probs for input Bag-of-Words vector
model = BoWClassifier(NUM_LABELS, VOCAB_SIZE)

# negative log likelihood loss
# input will be a pair of &lt;log probs computed by model, target label&gt;
loss_function = nn.NLLLoss()

# SGD optimizer for model parameters
optimizer = optim.SGD(model.parameters(), lr=0.1)

for epoch in range(100):
    for sentence, label in train:
        # clear accumulated gradients
        model.zero_grad()

        # create input BoW vector and target variable as torch.autograd.Variable
        bow_vec = autograd.Variable(make_bow_vector(sentence))
        target = autograd.Variable(make_target(label))

        # run forward pass (i.e., prediction)
        log_probs = model(bow_vec)

        # compute loss
        loss = loss_function(log_probs, target)

        # gradient of loss
        loss.backward()

        # update model parameters
        optimizer.step()
```

（変数名、コメントなど少し変えたり簡略化したりした）

- BoWベクトルの入力に対して log Softmax を予測値として返す分類モデル `model` を、
- 負の対数尤度 `nn.NLLLoss()` を損失関数として、
- 確率的勾配降下法 `optim.SGD()` によって学習している。

勾配降下法なので、パラメータは損失 `loss` の偏微分に基づいて毎ステップ更新される。これが27行目 `loss.backward()` の仕事ということに。わかってきた。

しかし線形なコードフロー、気持ちはとてもよく分かるんだけど、`optimizer` に `loss` を渡したわけでもないのに `loss.backward()` => `optimizer.step()` でパラメータが更新されるのが気持ち悪い…。

EuroSciPy 2017のKeynoteで語られていたことの背景はここまでの内容で十分つかめるけど [^1]、autogradと仲良くなれる日はまだまだ遠そうだなぁと思うのでした。

次のステップはなんだろう。PyTorch + autograd で [Matrix Factorization](/note/coursera-recommender-systems/) でも実装してみましょうか。

[^1]: PyTorchの思想や、高階微分の実装といった今後の計画など、実際に触ってみて「確かにそうだよね」という気持ちになった。