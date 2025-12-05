---
categories: [Conference, Machine Learning]
date: 2019-10-26
images: [/images/apachecon-2019/takuti.jpg]
lang: en
title: 'ApacheCon 2019 North America #ACNA19 & Europe #ACEU19'
lastmod: '2022-06-04'
keywords: [apachecon, apache, iot, hivemall, community, projects, cdp, beam, talk,
  session]
recommendations: [/note/iotswc-2019/, /note/hivemall-events-2018-autumn/, /note/hivemall-pyspark/]
---

As a committer/PPMC of [Apache Hivemall](https://github.com/apache/incubator-hivemall) (incubating), I have attended and presented at [ApacheCon North America](https://www.apachecon.com/acna19/) and [ApacheCon Europe](https://aceu19.apachecon.com). 

![takuti.jpg](/images/apachecon-2019/takuti.jpg)

[Photo: Jan Michalko / plain schwarz](https://www.flickr.com/photos/newthinking_de/48950979278/in/album-72157711465296723/)

These were my very first ApacheCon experiences, and it was great to be part of the community in this memorial year - yes, it's [the 20th anniversary of Apache Software Foundation](https://www.infoq.com/news/2019/09/apachecon-opening-keynote/).

A key message I've got from the conferences is about ***the power of community***. Of course, all sessions are technically stimulating and exciting to learn, but, more than that, I was impressed by how to make such a big conference possible as a result of gathering diverse people and projects from the OSS community.

### ApacheCon North America @ Las Vegas

In this annual conference, we have presented the recent updates on the Hivemall project:

<script async class="speakerdeck-embed" data-id="18bfa20f16fd441a84d703fd14b6fee3" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

I feel the audiences had a highly practical point of view; through the questions, they were trying to get a deeper understanding of how Hivemall runs with MapReduce, Tez, and Spark.

When I mentioned the sketching algorithms Hivemall has [imported from Brickhouse](https://github.com/apache/incubator-hivemall/pull/135), somebody pointed out taking advantage of [Apache DataSketches](https://datasketches.github.io), which naturally came into their mind from [another ApacheCon session](https://www.apachecon.com/acna19/s/#/scheduledEvent/1181). I'm sure the sustainable Apache ecosystem makes such a consideration of inter-project collaboration easier.

As an audience, notable things I've seen were:

- There were **less machine learning sessions** than I expected.
- Widely used Apache projects, **CloudStack, Pulsar, Kafka, and Beam** in particular, are drawing exceptional attention.
- **IoT ecosystem** is growing in the community.

Unlike the other "Big Data" conferences, I couldn't see so many ML-centric talks, and I believe attendee's interests were more in how large companies are utilizing the Apache projects in their production-grade systems at scale.

For example, in a special series of talks named Beam Summit, [Lyft introduced their use of Apache Beam for dynamic ride pricing](https://docs.google.com/presentation/d/1WCFny8qlWzb_ebZdUm3IxkoqWCjA5-r_TtCB8x0qa9g/edit#slide=id.g1af79f30ad_0_11). In fact, they mentioned "ML" in the talk, but the point was how to make ML more operational, rather than the detail of their pricing logic. Similarly, Beam is an effective tool to implement ML pipelines as we can see in [TensorFlow Extended](https://github.com/tensorflow/tfx).

Meanwhile, I can confidently say IoT is becoming an important use case of Apache projects. In ApacheCon NA, a dedicated session covers [integration between MQTT and Kafka](https://www.confluent.io/hub/confluentinc/kafka-connect-mqtt), [IoT application development using Spark and Bahir](https://github.com/lresende/bahir-iot-demo), and example of industrial solution named [StreamPipes](https://www.streampipes.org/).

More specifically, since MQTT is a protocol designed for IoT use cases that assume constrained unreliable TCP/IP connections, Kafka nicely compensates the limitations by providing reliable, scalable, decoupleable path of IoT data streams. In terms of system architecture, there are multiple IoT design patterns inspired by Lambda / [Kappa architecture](https://www.oreilly.com/ideas/applying-the-kappa-architecture-in-the-telco-industry).

It should be finally noted that talk right before my session introduced an interesting project called [Apache Unomi](https://unomi.apache.org ) ("You-know-me"), an open-source customer data platform (CDP). As my company is building an [enterprise CDP](https://www.treasuredata.com), I can share sympathy for its difficulty with the developers.

https://twitter.com/takuti/status/1172279583095148544

Ah, many surprises! I didn't expect to see CDP talk at ApacheCon, as well as the insightful IoT sessions.

### ApacheCon Europe @ Berlin

While the European version of ApacheCon is not held regularly, it happened this year to celebrate the anniversary.

https://twitter.com/ApacheCon/status/1187007925887393794

In contrast to the generic introduction of Hivemall in my ACNA talk, I have focused more on integrating Hivemall with PySpark:

<script async class="speakerdeck-embed" data-id="f6c6ade94b9a41b7b0ba5c5db5da8e1c" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

The content is based on my previous article: [Apache Hivemall in PySpark](/note/hivemall-pyspark), and I modified the [sample Google Colab notebook](https://gist.github.com/takuti/59bc761543786112a86528f61bbae67c) a lot to be ready for the event. 

As Spark is widely used for large-scale machine learning, I can easily imagine the audiences are interested in its internal implementation and scalability in comparison with Spark MLlib. I hope my talk and Q&A helps to get the points, but I'm sure we need to clarify more somewhere at the [documentation site](https://hivemall.incubator.apache.org/userguide/) to help users to convince "Why Hivemall?".

After the session, I had a great conversation with [Alexey Zinovyev](https://github.com/zaleslaw) who has presented about [Ignite ML](https://apacheignite.readme.io/docs/machine-learning), in the context of distributed ML. We shared how the parallelizable implementation of well-know ML techniques is challenging and interesting, and we agreed to have a look at the projects for each other.

Similarly to North America, IoT-related talks had a strong presence across the conference. The very first talk "[How to Become an IoT Developer](https://aceu19.apachecon.com/session/how-become-iot-developer-and-have-fun)" motivates us to play with the physical devices such as Raspberry Pi, and following talks introduced specific IoT projects from the community, including [PLC4X](https://github.com/apache/plc4x), [IoTDB](https://github.com/apache/incubator-iotdb), [Mynewt](https://mynewt.apache.org), and [NiFi](https://nifi.apache.org), with cool demonstrations.

### Bottom Line

My first ApacheCon experiences were simply great not only as a speaker but as a developer working on real-world CDP and IoT applications at Arm. 

If I give feedback, it would be nicer if we could see more interactions with non-Apache projects & communities; in fact, the Apache community is solid, but it sometimes shows a closed, nonflexible atmosphere that possibly makes bringing new joiners and new technology trends into the community harder.

Anyway, the community-driven conferences are super productive and insightful for me, and it's somewhat unusual compared to many other "enterprise-driven" ones. 