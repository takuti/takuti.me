---
categories: [Machine Learning, Programming, Data Science & Analytics]
date: 2022-11-11
lang: en
title: Google Cloud Dataflow and Its Positive Impact on Developer Productivity
keywords: [cloud, dataflow, data, apache, pipelines, pipeline, beam, google, resource,
  airflow]
recommendations: [/note/airflow-lineage/, /note/coursera-machine-learning-on-gcp/,
  /note/data-validation/]
---

With the [specialization on Coursera](/note/coursera-machine-learning-on-gcp), I've been on a not-too-fancy yet meaningful learning curve over the last few months in the context of machine learning on Google Cloud.

One obvious challenge in cloud data management and machine learning is the need for integrating multiple data sources and processing massive records in multi-phases without loss of visibility, scalability, and maintainability. Here, I found [Google Cloud Dataflow](https://cloud.google.com/dataflow), or [Apache Beam](https://beam.apache.org/) as its foundation, is particularly promising because the hosted Apache Beam-based data pipeline enables developers to simplify how to represent an end-to-end data lifecycle while taking advantage of GCP's flexibility in autoscaling, scheduling, and pricing.

Here I list my first impressions after spending a meaningful amount of time using Dataflow in some projects.

### Programming model as an implicit enforcement mechanism

First of all, I like the programming model as an engineer. Like [Apache Airflow](https://airflow.apache.org/)'s `>>`, a "good" data engineering tool offers a unique, simplified programming model (syntax) to make data pipelines not just programmable but accessible (i.e., readable and modifiable) for every team member. To give an example, the following code snippet is an [official example of counting words from texts](https://github.com/apache/beam/blob/5d2dbf957e4e82fb3980726940df02ac67e563cd/sdks/python/apache_beam/examples/wordcount.py#L87):


```py
with beam.Pipeline(options=pipeline_options) as p:
    # Read the text file[pattern] into a PCollection.
    lines = p | 'Read' >> ReadFromText(known_args.input)

    counts = (
        lines
        | 'Split' >> (beam.ParDo(WordExtractingDoFn()).with_output_types(str))
        | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
        | 'GroupAndSum' >> beam.CombinePerKey(sum))

    # Format the counts into a PCollection of strings.
    def format_result(word, count):
        return '%s: %d' % (word, count)

    output = counts | 'Format' >> beam.MapTuple(format_result)

    output | 'Write' >> WriteToText(known_args.output)
```

Note that Apache Beam supports multiple programming languages including Java and Go.

Instead of creating a consolidated module that does a bunch of operations at once, Beam developers need to dissect a single job into a series of simpler functions such as reading lines, generating key-value pairs, and aggregating them by keys. Eventually, it allows backend infrastructure, which can be on GCP, to efficiently process the records in a distributed manner. 

This is particularly important in case a team is large and working on mission-critical workloads posing strict scalability/reliability standards. In reality, implementing scalable and maintainable code is not straightforward for everyone on the team. Hence, it'd be great if the framework would work as an implicit enforcement mechanism so that the tool naturally helps developers to achieve the required quality of code.

### Shortcut to turn batch workload into streaming

Secondly, I'm impressed with how easy implementing a streaming pipeline in the same programming model as the batch is. To be more precise, a [streaming variant of the word counting example](https://github.com/apache/beam/blob/5d2dbf957e4e82fb3980726940df02ac67e563cd/sdks/python/apache_beam/examples/streaming_wordcount.py#L61) is very much similar to batch, except input/output sources (PubSub topics, instead of text files) and need for time windowing:

```py
with beam.Pipeline(options=pipeline_options) as p:
    # ...
    def count_ones(word_ones):
        (word, ones) = word_ones
        return (word, sum(ones))

    counts = (
        lines
        | 'split' >> (beam.ParDo(WordExtractingDoFn()).with_output_types(str))
        | 'pair_with_one' >> beam.Map(lambda x: (x, 1))
        | beam.WindowInto(window.FixedWindows(15, 0))
        | 'group' >> beam.GroupByKey()
        | 'count' >> beam.Map(count_ones))
    # ...
```

It should be noticed that regardless of whether it's batch or streaming, converting records into key-value pairs `beam.Map(lambda x: (x, 1))` plays a crucial role in the examples; if your data is represented as a collection of key-value pairs, achieving (near-)real-time efficiency can be significantly easier in many cases.

### Harmonizing with machine learning operations

Additionally, since the challenges mentioned above can be particularly painful when it comes to machine learning, which tends to be a mess due to ambiguity in what the scientists' code does, the combination of Apache Beam and GCP (or Beam itself, depending on how your backend infrastructure is built) potentially brings a huge paradigm shift to a cross-functional engineering team.

In fact, my first contact with Apache Beam was in the machine learning context at [ApacheCon 2019](/note/apachecon-2019/), where Lyft engineers presented their use case for dynamic pricing. If there is an enforcement mechanism in the framework and flexibility between batch vs. streaming, it'd be easier for a variety of engineers holding diverse specialties/seniority to unite their codebase, talk in the same "language" with each other, and make their data pipelines more maintainable and scalable in the longer run.

### Working on GCP

Last but not least, running/deploying/scheduling a Beam-based pipeline on GCP is not so complicated. In Python, after `pip install 'apache-beam[gcp]'`, we can simply trigger a pipeline from command-line e.g., by `python wordcount.py` with the GCP-specific pipeline options such as region, Cloud Storage bucket, project ID, and `--runner DataflowRunner`.

Although [Google Cloud's official tutorial](https://cloud.google.com/dataflow/docs/quickstarts/create-pipeline-python) is the best place to start, I jot down some quick observations below for future reference, which I have directly benefited from during the initial attempts.

**Customization**. Just like the [usage of Apache Beam](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/), it's also possible to add extra PyPI/non-PyPI dependencies through `setup.py`. Ultimately, you may deploy and run your pipeline to GCP like:

```sh
python /path/to/pipeline_script.py --runner DataflowRunner --setup_file /path/to/setup.py
```

**Orchestration and triggering**. To schedule the pipelines, we can leverage [Cloud Scheduler](https://cloud.google.com/community/tutorials/schedule-dataflow-jobs-with-cloud-scheduler) or [Workflows](https://cloud.google.com/blog/products/application-development/orchestrate-data-pipelines-using-workflows/). It seems to be important not to be confused a concept of data pipeline with DAG-based workflow management like Apache Airflow; it's micro vs. macro workload management in my limited experience, although there can be wider hybrid use cases and different perceptions I'm not aware of.

**Resource management**. In terms of cost and performance trade-off in batch workloads, autoscaling and [flexible resource scheduling](https://cloud.google.com/dataflow/docs/guides/flexrs) (FlexRS) greatly help to optimize the resource use as you need; your team may be willing to sacrifice execution time to accomplish a job at a lower price.

**Permission**. A pitfall you may (I did) encounter is around permission control. By default, the Dataflow workers use Google-managed service account `<project-number>-compute@developer.gserviceaccount.com` [as documented](https://cloud.google.com/dataflow/docs/concepts/security-and-permissions#default-service-account). This may or may not hinder the pipelines from reading from (writing to) desired data sources like BigQuery tables and Cloud Storage buckets. Therefore, knowing the default behavior and using a user-managed service account with `--serviceAccount` pipeline option would be unavoidable in practice.

Overall, Apache Beam can be a deeply satisfying option for the data & machine learning teams to standardize data pipelines at scale, and Google Cloud Dataflow is indeed a powerful enabler that eases its operational concerns. In particular, I cannot emphasize the importance of visibility of the data lifecycle (i.e., [data lineage](/note/airflow-lineage/)) enough, and I believe working with a solid programming model that increases developer productivity is one of the best approaches we can take. In many situations I encountered in the past, data engineers' struggles are not about how sophisticated your machine learning algorithm is, and we'd rather need focus on how "accessible" a resulting pipeline is.
