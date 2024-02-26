---
categories: [Recommender Systems, Programming]
date: 2019-01-14
images: [/images/recommender/incremental-recommendation.png]
lang: en
title: Feeding User-Item Interactions to Python-Based Streaming Recommendation Engine
  via Faust
lastmod: '2022-09-02'
keywords: [recommendation, incremental, flurs, engine, stream, faust, python, streams,
  items, user]
recommendations: [/note/flurs/, /note/cross-validation-julia-recommender/, /note/novelty-diversity-serendipity/]
---

*Streaming recommendation* is one of the most challenging topics in the field of recommender systems. The task requires recommendation engine to incrementally and promptly update recommendation model as new user-item interaction comes in to data streams (e.g., click, purchase, watch). I previously [studied such incremental recommendation techniques](https://arxiv.org/abs/1607.02858), and eventually published a Python library named **[FluRS](https://github.com/takuti/flurs)** to make their implementation and evaluation easier.

As I described in my research paper a couple of years ago, incremental recommender systems run in three steps:

![incremental-recommendation](/images/recommender/incremental-recommendation.png)

1. System recommends top-N items to a user by using a production recommendation model
2. User may interact with one or more recommended items
3. Recommendation model is incrementally updated based on the observed user-item interactions

In order to provide an implementation idea of the above recommender systems, this article examines **[Faust](https://faust.readthedocs.io)**, a handy stream and event processing engine for Python, in combination with FluRS. Faust allows our Python code to easily consume data streams and do something for incoming events.

```sh
pip install faust
```

### Updating FluRS recommender from a Faust processor

Assume that a dummy Kafka topic `flurs-events` continuously receives [MovieLens rating events](https://grouplens.org/datasets/movielens/) represented by pairs of `<user, item, rating, timestamp>`. In case that those events are JSON-serialized, a Faust event processor can be defined as:

```py
import json
import faust

app = faust.App(
    'flurs-recommender',
    broker='kafka://localhost:9092',
    value_serializer='raw',
)

topic = app.topic('flurs-events', value_type=bytes)

@app.agent(topic)
async def process(stream):
    async for obj in stream:
        event = json.loads(obj)
        # do something awesome
```

In Faust, the `@app.agent(topic)` decorator enables creating a processor, and what we have to do is just writing a Python function that does something for every single events from a stream. Since our application is a streaming recommender system, the function should update recommendation model against an observed event:

```py
@app.agent(topic)
async def process(stream):
    async for obj in stream:
        event = json.loads(obj)

        # focus only on positive feedback (i.e., rating is greater than 3)
        if event['rating'] < 3:
            continue

        # user (item) index = event['user'] (event['item']) - 1
        user, item = User(event['user'] - 1), Item(event['item'] - 1)
        recommender.update(Event(user, item))
```

It should be noticed that this processor corresponds to Step 3 in the above figure of streaming recommendation.

On the latest version of FluRS, `User`, `Item` and `Event` classes wrap user/item instances with their indices and features. For instance, `recommender` can be a matrix factorization model that is preliminary initialized as follows:

```py
from flurs.data.entity import User, Item, Event
from flurs.recommender import MFRecommender

recommender = MFRecommender(k=40)
recommender.initialize()

n_user, n_item = 943, 1682

for u in range(1, n_user + 1):
    recommender.register(User(u - 1))

for i in range(1, n_item + 1):
    recommender.register(Item(i - 1))
```

The code deterministically registers all possible instances to the recommender beforehand, since we already know total number of users and items (i.e., movies) in the public dataset.

### Running the streaming recommendation engine

Eventually, our stream recommender, `recommender.py`, can be implemented and executed as:

```py
from flurs.data.entity import User, Item, Event
from flurs.recommender import MFRecommender
import json
import faust

app = faust.App(
    'flurs-recommender',
    broker='kafka://localhost:9092',
    value_serializer='raw',
)

topic = app.topic('flurs-events', value_type=bytes)

recommender = MFRecommender(k=40)
recommender.initialize()

n_user, n_item = 943, 1682

for u in range(1, n_user + 1):
    recommender.register(User(u - 1))

for i in range(1, n_item + 1):
    recommender.register(Item(i - 1))


@app.agent(topic)
async def process(stream):
    async for obj in stream:
        event = json.loads(obj)
        if event['rating'] < 3:
            continue
        user, item = User(event['user'] - 1), Item(event['item'] - 1)
        recommender.update(Event(user, item))
```

```sh
faust -A recommender worker -l info
```

Note that the easiest way to set up a local Kafka environment on Mac would be:

```sh
brew install zookeeper kafka
brew services start zookeeper
brew services start kafka
```

### Producing MovieLens rating events to the Kafka topic

Here, the following code, `producer.py`, produces toy events to the dummy topic:

```py
import sys
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda m: json.dumps(m).encode('ascii'))
topic = 'flurs-events'

keys = ['user', 'item', 'rating', 'timestamp']

with open(sys.argv[1], 'r') as f:  # /path/to/ml-100k/u.data
    for line in f.readlines():
        event = dict(zip(keys, map(int, line.rstrip().split('\t'))))

        future = producer.send(topic, event)
        try:
            future.get(timeout=10)
        except KafkaError as e:
            print(e)
            break
```

```sh
python producer.py /path/to/ml-100k/u.data
```

The producer simulates Step 2 in the flow of incremental recommendation, where user-item interaction is observed and emitted to a core recommendation engine.

Finally, `producer.py` communicates with `recommender.py` via Kafka and Faust, and rating events are fed to the processor.

### Observations

Thanks to the easy-to-use Python-based streaming processing engine, I was able to provide mock implementation of streaming recommender system by using FluRS. Below I list some open questions we need to consider more closely:

- How to deal with unknown total number of users and items
    - We preliminary registered total number of users and items to initialize a recommender, but those numbers are normally unknown at the time of initialization in practice.
- How to choose appropriate serialization format
    - JSON-serialization is not always the best choice.
    - Event records passing through data streams should be as much as simple for efficiency.
    - If we directly pass `flurs.data.entity.Event` object to a stream, we need to implement a dedicated serializer and deserializer of the custom object.
- How to integrate recommendation logic
    - Implementation of Step 1 in the above figure, where a recommendation model is hold and recommendation is actually conducted, is not obvious at this moment.

Based on these observations, I will improve the package to make it more feasible.