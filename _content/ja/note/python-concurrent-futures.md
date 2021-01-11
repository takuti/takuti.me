---
aliases: [/note/python-concurrent-futures/]
categories: [プログラミング, コンピュータシステム]
date: 2017-10-01
keywords: [並列化, futures, マルチスレッド, concurrent, プロセス, 処理, pool, multiprocessing, loky,
  レッド]
lang: ja
recommendations: [/ja/note/euroscipy-2017/, /ja/note/acroquest-javabook/, /ja/note/coursera-scala-specialization/]
title: Pythonのconcurrent.futuresを試す
---

[EuroScipy 2017](/note/euroscipy-2017) でPythonの [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) についての話を聞いたので、改めて調べてみた。

2系まではPythonの並列処理といえば標準の `multiprocessing.Pool` が定番だったけど、3系からは新たなインタフェースとして `concurrent.futures` という選択肢もふえた。

Scalaなんかでおなじみの **Future** とは、並行処理の結果を参照する存在。Pythonの Future `f = concurrent.futures.Future()` は処理の『実行中 `f.running()` 』『キャンセル済み `f.canceled()` 』『完了 `f.done()` 』といった“状態”を参照するメソッドを提供している。そして `f.result()` を呼べば完了までブロッキング。

実際には、非同期処理は `Executor` オブジェクトによってスケジューリングされる。このときマルチスレッドなら `ThreadPoolExecutor`、マルチプロセスなら `ProcessPoolExecutor` を使う。

### マルチスレッド: `ThreadPoolExecutor`

スレッドプールを利用した並列化。

重要なのは、たとえ複数スレッドで処理を実行しても、**ワーカーたちは1つのインタプリタを共有している**点。これによりメモリオーバーヘッドが小さい、spawnが早い、ワーカー間の同期が不要といった意味で、処理の効率的な非同期呼び出しが期待できる。

しかし同時に、Pythonには **[Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock)** (GIL) という mutex があり、1つのインタプリタ上では同時に1スレッドからしかリソースにアクセスできないという制約がある。なので `ThreadPoolExecutor` による並列化は、CPU-boundedな処理に対しては必ずしも有効とは言えない。

これは過度な制約だという見方もあり、numpy, pandas, sklearn といった有名ライブラリは `with nogil` を付与したコンパイルによってGILフリーなマルチスレッド処理を（部分的に）行っていたりするらしい。

### マルチプロセス: `ProcessPoolExecutor`

一方で、プロセスレベルの並列化では各ワーカーが自分だけのインタプリタを持つ。

これによりマルチスレッドと比較するとspawnが遅く、メモリオーバーヘッドが大きく、プロセス間で同期をとる必要が生じてしまうが、GILに縛られない並列化が可能となる。

従来 `multiprocessing.Pool()` でプロセスプールを作って実現していた並列化はこちらに相当する。

### 試す

では、1秒wait()×2回をシングルスレッド、マルチスレッド、マルチプロセスそれぞれで試してみよう：

```py
import time
from concurrent import futures


def wait():
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    wait()
    wait()
    end = time.time()
    print('Single: elapsed time = {}'.format(end - start))

    start = time.time()
    with futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(wait)
        f2 = executor.submit(wait)
        f1.result()
        f2.result()
    end = time.time()
    print('Multi-thread: elapsed time = {}'.format(end - start))

    start = time.time()
    with futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(wait)
        f2 = executor.submit(wait)
        f1.result()
        f2.result()
    end = time.time()
    print('Multi-process: elapsed time = {}'.format(end - start))
```

`executor.submit()` でタスクのスケジューリングをして、返ってきた `Future` オブジェクトが完了するまで `result()` で処理をブロックする。

結果：

```
$ python wait.py
Single:        elapsed time = 2.0102460384368896
Multi-thread:  elapsed time = 1.0070040225982666
Multi-process: elapsed time = 1.0193650722503662
```

並列処理のパワーを感じる。

次に、[大きい数の素数判定を並列に行う公式ドキュメントの例](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor-example)を試してみる：

```py
import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    import time

    start = time.time()
    for number, prime in zip(PRIMES, map(is_prime, PRIMES)):
        print('%d is prime: %s' % (number, prime))
    end = time.time()
    print('Single:        elapsed time = {}'.format(end - start))

    start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    end = time.time()
    print('Multi-thread:  elapsed time = {}'.format(end - start))

    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    end = time.time()
    print('Multi-process: elapsed time = {}'.format(end - start))
```

判定対象の数を `is_prime()` に `executor.map` して呼ぶ。使い方は通常の `map` や `multiprocessing.Pool.map` と同じ。

```
$ python prime.py
112272535095293 is prime: True
112582705942171 is prime: True
112272535095293 is prime: True
115280095190773 is prime: True
115797848077099 is prime: True
1099726899285419 is prime: False
Single:        elapsed time = 2.9173738956451416
...
Multi-thread:  elapsed time = 3.619951009750366
...
Multi-process: elapsed time = 1.7795209884643555
```

結果は、シングルスレッド vs マルチプロセスでは処理時間が期待通り短縮されているが、マルチスレッドはむしろシングルスレッドよりも遅い。これがGILの罠。CPU-boundedな処理の `ThreadPoolExecutor` による並列化は期待を裏切る。

### Q. 結局どれを使って並列化すべきなのか

（僕の観測範囲では）機械学習系の論文の~~割と雑な~~コードがGitHubで公開されていると、それはたいてい `multiprocessing.Pool` を使っている気がするけど、それで本当に良いのだろうか。

`concurrent.futures` を紹介してくれた EuroScipy 2017 のトークの本題は、`concurrent.futures` をロバストにした Executor **[loky](https://github.com/tomMoral/loky)** の紹介だった [^1]。というわけで、この先は loky と `concurrent.futures` の違いを知った上で、未だに広く使われている `multiprocessing.Pool` も含めて、「結局どれを使うべきなのか」ということを考える必要がある [^2]。

というわけで、続きます。

[^1]: なんと [`joblib.Parallel` の正体は loky らしい](https://github.com/joblib/joblib/blob/master/joblib/parallel.py#L47)。知らなかった…。
[^2]: まぁなんとなく、「joblibを使おう」みたいな結論になりそうな気がする。