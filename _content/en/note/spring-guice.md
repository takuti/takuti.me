---
categories: [Engineering]
date: 2021-10-30
images: [/images/spring-guice/uml.png]
title: Cross-Framework Dependency Injection with spring-guice
lastmod: '2022-09-02'
keywords: [guice, spring, injection, application, dependency, party, framework, third,
  class, your]
recommendations: [/note/machine-learning-product/, /note/becoming-a-product-manager/,
  /note/learn-how-others-work/]
---
 
[Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection) (DI) is a well-known design pattern that creates and binds dependent objects outside of a class. The technique nicely decouples dependencies from a main application class and enables developers to achieve high testability, maintainability, and extensibility. As I understand, [Google Guice](https://github.com/google/guice) and [Spring Framework](https://spring.io/projects/spring-framework) are major DI frameworks in Java.
 
Unsurprisingly, working with a specific framework among others often causes a compatibility issue. Imagine you are developing an application using Guice for DI. Meanwhile, there is a third-party package that may accelerate your development effort, which actually relies on Spring unlike yours. Here, ***how can we apply Spring-based injection logic to Guice-based applications?*** An intermediate tool [**spring-guice**](https://github.com/spring-projects/spring-guice) could be a solution in this situation.
 
### Dummy scenario: Machine learning application using Guice
 
Assume there is a Java-based machine learning framework that provides `BaseModel` and `BaseMetric` interface, and you have implemented `LogisticRegression` model and `Recall` metric on top of the framework. An ultimate goal for you is to implement the following `BinaryClassification` application using Guice:
 
```java
public class BinaryClassification {
 
   @Inject
   private BaseModel model;
 
   @Inject
   private BaseMetric metric;
 
   ...
 
}
```
 
Notice that such abstraction can be commonly seen in the community, and [scikit-learn's `BaseEstimator`](https://github.com/scikit-learn/scikit-learn/blob/2571cb29892f52633cfc2ad326887960ffa375da/sklearn/base.py#L149) is a good example. The actual implementation doesn't follow the DI design pattern in the formal sense though.
 
In Guice, the injectors can be triggered as:
 
```java
Injector injector = Guice.createInjector(new ModelModule(), new MetricModule());
BinaryClassification app = injector.getInstance(BinaryClassification.class);
```
 
where the modules defining which model/metric to bind are:
 
```java
public class ModelModule extends AbstractModule {
  
   @Override
   protected void configure() {
       bind(BaseModel.class).to(LogisticRegression.class);
   }
  
}
```
 
```java
public class MetricModule extends AbstractModule {
  
   @Override
   protected void configure() {
       bind(BaseMetric.class).to(Recall.class);
   }
  
}
```

 ### Leveraging a third-party application using Spring

As a UML diagram, the original implementation can be depicted:
 
![uml](/images/spring-guice/uml.png)
 
Meanwhile, you found a novel `RandomForest` implementation for the framework on GitHub, and it seems to be promising as an alternative to your `LogisticRegression` model. However, unlike your own app, the third-party code depends on Spring to achieve DI and serves the custom application in the form of `@Configuration`-annotated `SpringAppConfig` module:
 
```java
@Configuration
@ComponentScan("org.example.ml.app.spring") // RandomForest is in this path
public class SpringAppConfig {
}
```
 
In this situation, **spring-guice** enables you to easily apply the Spring-based injection logic to your Guice-based client application as follows:
 
```java
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.guice.module.SpringModule;
 
AnnotationConfigApplicationContext context =
       new AnnotationConfigApplicationContext(SpringAppConfig.class);
 
Injector injector = Guice.createInjector(new SpringModule(context), new MetricModule());
BinaryClassification app = injector.getInstance(BinaryClassification.class);
```
 
Eventually, the Spring module seamlessly replaces your `LogisticRegression` with `RandomForest` in the binary classification app.
 
### Bottom line
 
"Dependency for Dependency Injection" is sometimes troublesome, especially when your application needs to interact with a number of third-party software that are out of your control. Of course, rewriting original Spring-based code with Guice could be a solution if the third-party implementation is simple enough, but it's not always the case. Hence, knowing one or more bridge tools helps us to consider the trade-off and make a better decision.
 
Last but not least, spring-guice has additional use cases that aren't covered by my example above, and their [README](https://github.com/spring-projects/spring-guice/blob/master/README.md) highlights the multiple ways to fulfill the gap.
 
You can find a complete version of the sample code on GitHub: [**takuti-sandbox/spring-guice-test**](https://github.com/takuti-sandbox/spring-guice-test)