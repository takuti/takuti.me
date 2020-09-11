---
categories: [Machine Learning, Programming]
date: 2019-03-24
keywords: [hivemall, spark, training, pyspark, uses, prediction, python, need, scikit,
  successfully]
lang: en
recommendations: [/note/hivemall-events-2018-autumn/, /note/apachecon-2019/, /note/pyconjp-2015/]
title: Apache Hivemall in PySpark
---

[Apache Hivemall](https://github.com/apache/incubator-hivemall/), a collection of machine-learning-related Hive user-defined functions (UDFs), offers Spark integration as documented [here](https://hivemall.incubator.apache.org/userguide/spark/getting_started/installation.html). Now, we will see how it works in [PySpark](https://spark.apache.org/docs/2.2.0/api/python/index.html).

Note that Hivemall requires Spark 2.1+. This article particularly uses Spark 2.3 and Hivemall 0.5.2, and the entire contents are available at [this Google Colabo notebook](https://colab.research.google.com/drive/1u9Mj6jc3oTkn02NAl2o2Vu_OkzyEn4ks).

### Installation

We do need to set up Spark and Hadoop environment first of all. For example, if you are using Colabo, follow [instructions](https://mikestaszel.com/2018/03/07/apache-spark-on-google-colaboratory/) as:

```sh
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q http://mirror.reverse.net/pub/apache/spark/spark-2.3.3/spark-2.3.3-bin-hadoop2.7.tgz
!tar xf spark-2.3.3-bin-hadoop2.7.tgz
!pip install -q findspark
```

```py
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.3.3-bin-hadoop2.7"
```

```py
import findspark
findspark.init()
```

Next, download `hivemall-spark2.x-0.y.z-incubating-with-dependencies.jar` corresponding to your Spark version from the [ASF repository](http://mirror.reverse.net/pub/apache/incubator/hivemall/):

```sh
wget -q http://mirror.reverse.net/pub/apache/incubator/hivemall/0.5.2-incubating/hivemall-spark2.3-0.5.2-incubating-with-dependencies.jar
```

### Create Spark session

Connect to the Spark instance and start a new session:

```py
from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local[*]').config('spark.jars', 'hivemall-spark2.3-0.5.2-incubating-with-dependencies.jar').enableHiveSupport().getOrCreate()
```

The Hivemall `.jar` file is explicitly loaded from `jars` option, and Hive connection and their UDF support are enabled by `enableHiveSupport()`.

### Register Hive(mall) UDF to Spark

If a Spark session is instantiated with `enableHiveSupport()` as the above example, we can use Hive UDFs in Spark. [This GitHub repository](https://github.com/bmc/spark-hive-udf) gives more explanation and examples.

Basically, the only thing we have to do is to load a Hive function from `CREATE TEMPORARY FUNCTION` statement with its appropriate class path:

```py
spark.sql("CREATE TEMPORARY FUNCTION hivemall_version AS 'hivemall.HivemallVersionUDF'")
```

Eventually, Spark SQL allows us to use the UDF just like HiveQL:

```py
spark.sql("SELECT hivemall_version()").show()
```

```
+------------------+
|hivemall_version()|
+------------------+
|  0.5.2-incubating|
+------------------+
```

### Example: Binary classification

To give a practical example, let's solve a [customer churn prediction problem](https://aws.amazon.com/blogs/machine-learning/predicting-customer-churn-with-amazon-machine-learning/) with simple binary classifier.

#### Register UDFs

Below is a minimal list of Hivemall functions to tackle the problem:

```py
# preprocessing
spark.sql("CREATE TEMPORARY FUNCTION categorical_features AS 'hivemall.ftvec.trans.CategoricalFeaturesUDF'")
spark.sql("CREATE TEMPORARY FUNCTION quantitative_features AS 'hivemall.ftvec.trans.QuantitativeFeaturesUDF'")
spark.sql("CREATE TEMPORARY FUNCTION array_concat AS 'hivemall.tools.array.ArrayConcatUDF'")

# training
spark.sql("CREATE TEMPORARY FUNCTION train_classifier AS 'hivemall.classifier.GeneralClassifierUDTF'")

# prediction and evaluation
spark.sql("CREATE TEMPORARY FUNCTION sigmoid AS 'hivemall.tools.math.SigmoidGenericUDF'")
spark.sql("CREATE TEMPORARY FUNCTION extract_feature AS 'hivemall.ftvec.ExtractFeatureUDFWrapper'")
spark.sql("CREATE TEMPORARY FUNCTION extract_weight AS 'hivemall.ftvec.ExtractWeightUDFWrapper'")
spark.sql("CREATE TEMPORARY FUNCTION logloss AS 'hivemall.evaluation.LogarithmicLossUDAF'")
spark.sql("CREATE TEMPORARY FUNCTION auc AS 'hivemall.evaluation.AUCUDAF'")
```

#### Data preparation

Dataset is a small CSV file having 3,333 records:

```sh
wget -q http://dataminingconsultant.com/DKD2e_data_sets.zip
unzip -j DKD2e_data_sets.zip "**/churn.txt"
```

Create a Spark DataFrame from the CSV file:

```py
import re
import pandas as pd

df = spark.createDataFrame(
    pd.read_csv('churn.txt').rename(lambda c: re.sub(r'[^a-zA-Z0-9 ]', '', str(c)).lower().replace(' ', '_'), axis='columns'))
df.printSchema()
```

```
root
 |-- state: string (nullable = true)
 |-- account_length: long (nullable = true)
 |-- area_code: long (nullable = true)
 |-- phone: string (nullable = true)
 |-- intl_plan: string (nullable = true)
 |-- vmail_plan: string (nullable = true)
 |-- vmail_message: long (nullable = true)
 |-- day_mins: double (nullable = true)
 |-- day_calls: long (nullable = true)
 |-- day_charge: double (nullable = true)
 |-- eve_mins: double (nullable = true)
 |-- eve_calls: long (nullable = true)
 |-- eve_charge: double (nullable = true)
 |-- night_mins: double (nullable = true)
 |-- night_calls: long (nullable = true)
 |-- night_charge: double (nullable = true)
 |-- intl_mins: double (nullable = true)
 |-- intl_calls: long (nullable = true)
 |-- intl_charge: double (nullable = true)
 |-- custserv_calls: long (nullable = true)
 |-- churn: string (nullable = true)
```

Notice that the column names are normalized just in case.

[`SparkSession.read`](https://spark.apache.org/docs/preview/api/python/pyspark.sql.html#pyspark.sql.SparkSession.read) can be an alternative option, while the example uses [`pandas.read_csv()`](https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.read_csv.html#pandas.read_csv):

```py
df = spark.read.option('header', True).schema(schema).csv('churn.txt')
```

Here, `schema` needs to be explicitly specified as follows, otherwise all columns are simply recognized as string:

```py
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import DoubleType, IntegerType, StringType

schema = StructType([
    StructField("A", IntegerType()),
    StructField("B", DoubleType()),
    StructField("C", StringType())
])
```

Finally, split the records into 80% training and 20% validation samples:

```py
df_train, df_test = df.randomSplit([0.8, 0.2], seed=31)
```

#### Training

It's time to learn how to do machine learning with Hivemall; every single step of machine learning workflow can be implemented in the form of SQL-like query as shown in [here](http://hivemall.incubator.apache.org/userguide/supervised_learning/tutorial.html). In case of using Hivemall with PySpark, `createOrReplaceTempView('table_name')` enables those queries to access to Spark DataFrames:

```py
df_train.createOrReplaceTempView('train')
```

Replace the `train` table with vectorized training samples:

```py
spark.sql("""
CREATE OR REPLACE TEMPORARY VIEW train AS
SELECT
  array_concat(
    categorical_features(
      array('intl_plan', 'vmail_plan'),
      intl_plan, vmail_plan
    ),
    quantitative_features(
      array('custserv_calls', 'account_length'),
      custserv_calls, account_length
    )
  ) as features,
  if(churn = 'True.', 1, 0) as label
FROM
  train
""")
```

For the sake of simplicity, I randomly choose four attributes, `intl_plan` and `vmail_plan` for categorical features, and `custserve_calls` and `account_length` for quantitative features. Of course we can incorporate more attributes and/or apply more aggressive feature engineering techniques such as standardization in reality.

Building a logistic regression model is done by just 10 lines of query:

```py
df_model = spark.sql("""
SELECT
  feature, avg(weight) as weight
FROM (
  SELECT
    train_classifier(features, label) as (feature, weight)
  FROM
    train
) t
GROUP BY 1
""")
df_model.show()
```

```
+--------------+-------------------+
|       feature|             weight|
+--------------+-------------------+
|custserv_calls|  9.037338733673096|
|  intl_plan#no| -7.765866041183472|
| vmail_plan#no|  3.730261445045471|
|account_length|0.20337164402008057|
|vmail_plan#yes| -5.873621702194214|
| intl_plan#yes| 11.210701942443848|
+--------------+-------------------+
```

Yes, Hivemall represents machine learning models in the form of table.

#### Prediction

Convert the 20% test set in the same way as the training samples, and `explode` them for prediction:

```py
df_test.createOrReplaceTempView('test')
spark.sql("""
CREATE OR REPLACE TEMPORARY VIEW test AS
SELECT
  phone,
  label,
  extract_feature(fv) AS feature,
  extract_weight(fv) AS value
FROM (
  SELECT
    phone,
    array_concat(
      categorical_features(
        array('intl_plan', 'vmail_plan'),
        intl_plan, vmail_plan
      ),
      quantitative_features(
        array('custserv_calls', 'account_length'),
        custserv_calls, account_length
      )
    ) as features,
    if(churn = 'True.', 1, 0) as label
  FROM
    test
) t1
LATERAL VIEW explode(features) t2 AS fv
""")
```

Join the logistic regression model with test samples and their feature set, and take sigmoid of weighted sum:

```py
df_model.createOrReplaceTempView('model')
df_prediction = spark.sql("""
SELECT
  phone,
  label as expected,
  sigmoid(sum(weight * value)) as prob
FROM
  test t LEFT OUTER JOIN model m
  ON t.feature = m.feature
GROUP BY 1, 2
""")
df_prediction.show()
```

```
+--------+--------+----------+
|   phone|expected|      prob|
+--------+--------+----------+
|414-9054|       0|       1.0|
|372-1493|       0|       1.0|
|339-7541|       1|       1.0|
|400-3150|       0|       1.0|
|365-3562|       0|       1.0|
|356-2992|       0| 0.9999807|
...
```

Since we did nothing special to achieve a better prediction model, prediction results are obviously poor.

#### Evaluation

Anyway, once prediction results are obtained, we can evaluate the accuracy of prediction. For instance, Hivemall supports Area Under the ROC Curve (AUC) and Log Loss metric for binary classification:

```py
df_prediction.createOrReplaceTempView('prediction')
spark.sql("""
SELECT
  sum(IF(IF(prob >= 0.5, 1, 0) = expected, 1.0, 0.0)) / count(1) AS accuracy,
  auc(prob, expected) AS auc,
  logloss(prob, expected) AS logloss
FROM (
  SELECT prob, expected
  FROM prediction
  ORDER BY prob DESC
) t
""").show()
```

```
+--------------------+------------------+------------------+
|            accuracy|               auc|           logloss|
+--------------------+------------------+------------------+
|0.157037037037037...|0.6012885662431942|24.322495101659264|
+--------------------+------------------+------------------+
```

Again, the result is just an example, and we do need to tweak the model to make accurate prediction.

### Conclusion

As the example above shows, we have successfully used Hivemall in combination with PySpark. That is, we can directly access to the Hivemall capabilities from Python code for each of preprocessing, training, prediction, and evaluation phase.

In practice, I can easily imagine jointly using the other Python packages e.g., scikit-learn for training, Airflow for workflow management, Flask for providing REST APIs. This fact definitely expands the potential uses of Hivemall.