---
categories: [Data Science]
date: 2021-04-04
keywords: [cost, right, demand, average, operations, method, logistics, inventory,
  forecasting, value]
lang: en
recommendations: [/note/machine-learning-product/, /note/learn-how-others-work/, /note/nrf-2020/]
title: The Essence of Supply Chain Management
---

On Coursera, I have [completed **Supply Chain Management Specialization**](https://coursera.org/verify/specialization/CR3YNENM4MYG) offered by Rutgers University, which consists of four different topics in an end-to-end supply chain management process:

1. Logistics
2. Operations
3. Planning
4. Sourcing

The series of courses gave me a clear picture of how real-world companies build and operate supply chains, and what kind of practical problems exist throughout the process.

For me, a key takeaway from the specialization can be three-fold:

- There is always a trade-off between service level, risk, and cost.
- To make the right decision, having a solid corporate-wide objective, mission, and strategy is important.
- Starting from the simplest possible approach and making continuous improvement lead an organization to success.

Sounds like general statements to run a business? I know, but this is exactly how the real-world supply chain runs.

As a data scientist, I have worked for a couple of companies that are struggling with supply chain optimization in the past. Of course, I *could* tackle their problems without having domain-specific knowledge, by simply applying general data science & analytics practices from EDA (Exploratory Data Analysis) to statistical modeling. However, if I knew the basic concepts and best practices taught by the courses, I could do a better job and more confidently present the insights to convince stakeholders. 

Let me summarize what I learned from the specialization in the following sections.

### Logistics

The first course was about logistics, and they highlighted three different transportation modes: truck, flight, and train.

| Mode | Characteristics |
|:---|:---|
|Truck|Trucking denotes freight on the roads, and the most popular transportation mode has advantages in terms of accessibility, speed (especially for short distances), reliability, and flexibility. Different types of trucks take different responsibilities in a supply chain; some of them are used for direct pickup/delivery, whereas long-haul ones go through intermediate facilities for cross-docking and relaying.|
|Flight|Flight is another important mode that focuses heavily on its speed for certain items. Although the mode is not profitable enough, flying air allows suppliers to readily deliver their products across the world. These efforts could eventually lead to a high service level.|
|Train|To build a long-haul transportation network, trains would be a reasonable alternative. While the speed is still competitive with trucking, using trains is much more efficient in terms of both cost and fuel consumption. In Japan, for example, we could see many freight trains, especially in the countryside.|

Importantly, freight transportation typically doesn't complete in a single section, and intermediate facilities for warehousing play a key role to make the global supply chains possible. Having warehouses enable us to:

- efficiently and immediately respond to customer demand;
- keep the service level stable;
- ensure the redundancy for upcoming orders while managing risks (e.g., shortage of certain products, accident in logistics).

Designing a warehouse is also an interesting topic that requires us to optimize retrieval, pickup, and delivery time depending on a product category in terms of demand. To give an example, a floor map below is the one that I designed for an assignment; we (1) separate inbound and outbound dock doors, (2) make rack/people placement symmetric, (3) minimize the time to access the fast movers, and (4) make conveyors easily reachable from anywhere in the warehouse:

![warehouse](/images/coursera-supply-chain-management/warehouse.png)

When we look at individual items stored in the warehouses, there are two types of inventory: **cycle stock** and **safety stock**; the former shows a relatively stable balance between supply and demand over time, whereas the latter is prepared for unexpected situations from the risk management standpoint. These stocks can be fulfilled as a result of a continuous review cycle, and there is a specific order point (i.e., threshold to make an order) depending on an organization.

Last but not least, where inventory is located is an important question to establish a good supply chain. Customer satisfaction is largely based on the **lead time** (i.e., time from order to delivery) and **percentage of orders shipped from inventory**, and optimal numbers differ depending on SKUs. Meanwhile, holding too much inventory and/or building too many warehouses are clearly cost-inefficient. Hence, a company has to come up with a reasonable supply chain network that consists of a sufficient amount/placement of warehouses.

For instance, I designed the following supply chain network for an assignment. Imagine there are 10 sample customers (blue pins) across the US, and I decided to have three warehouses (red stars) as depicted so that we can deliver our product to all of the sample destinations in 3 days at the latest:

![facilities](/images/coursera-supply-chain-management/facilities.png)

### Operations

The second topic was operations, which describe an entire process of transforming raw materials into actual products. 

Since customers always want to buy the best products at the lowest cost, brands need to seriously optimize their day-to-day operations. Key variables include (1) cost, (2) quality, (3) speed, and (4) flexibility, and we have to take trade-offs under certain constraints; producing the world's highest quality & cheapest product is infeasible, and the brands must balance the variables based on their own criteria.

The course refers to [TOYOTA Production System](https://global.toyota/en/company/vision-and-philosophy/production-system/) (TPS) as the best practice of operations for producing as much product as possible given the constraints. There are two important steps in TPS:

1. **Kaizen** (continuous improvement)
2. **Elimination of waste**

Moreover, we can follow the [Lean Thinking](https://en.wikipedia.org/wiki/Lean_thinking#:~:text=Lean%20thinking%20is%20a%20transformational,was%20coined%20by%20James%20P.) framework that generalizes TPS and makes the thinking process widely applicable. According to the framework, what we could do to continuously enhance the operations without wasting time and money is as follows:

1. Specify a value
2. Map a value stream
3. Make value flow
4. Pull back from customer
5. Strive for perfection

Most importantly, the process starts from **specifying a core value**. Without such a clear guideline, how can we evaluate the current status and make sure we're heading in the right direction?

In practice, continuous improvement in supply chains requires us to find a single constraint, namely "**bottleneck**", that poses the largest negative impact on an overall process. Once we identified the bottleneck, eliminating it from the production system becomes an immediate goal to make operations better, and the effort continues infinitely in the long run.

To support an ultimate decision-making process, there is a couple of mathematical tools that enable us to quantitatively measure and optimize the condition of inventory.

One of them is called **EOQ** (**Economic Order Quantity**). Assume:

- $D = $ Demand; how much we sell in a given period
- $V = $ Value of the item (i.e., purchase cost, production cost)
- $O = $ Order cost; cost of placing and receiving the item
- $C = $ Inventory carrying cost

Here, an optimal order quantity of this item, EOQ, can be calculated by:

$$
\mathrm{EOQ} = \sqrt{\frac{2OD}{CV}}
$$

Note that EOQ is a specific order quantity $Q$ which balances an order receiving cost $\frac{OD}{Q}$ and inventory holding cost $\frac{VCQ}{2}$, and total cost for this product is calculated as a sum of these two costs: 

$$
\mathrm{Total Cost}(Q) = \frac{OD}{Q} + \frac{VCQ}{2}
$$

Another formula tells us **how much safety stock we'd need for achieving a certain service level**. When we'd like to achieve $p$% of service level (i.e., $p$% of customers can be covered by the stock), the required amount of safety stock can be calculated as follows by using $\mathrm{norminv}$, the inverse of the standard normal cumulative distribution:

$$
\mathrm{SafetyStock} = \mathrm{norminv}(p) \times \sqrt{t \times S_d^2 + d^2 \times S_t^2},
$$

where $t$ and $d$ are average replenishment lead time and daily sales (i.e., demand), respectively, and $S_t$ and $S_d$ are their standard deviation. Nothing is special, and everything can be readily calculated on Excel.

Beyond the simple math, we also see the other techniques such as [Six Sigma](https://www.sixsigma-institute.org/What_Is_Six_Sigma.php) and [Kanban](https://www.ascm.org/ascm-insights/kanban-and-the-lean-supply-chain/) in the course, but the basic principle stays same &mdash; *Continuously improve the process and eliminate the wastes.* 

"Quality is free" &mdash; That is, investment on improving quality equals to cost you'll spend on waste.

### Planning

We just saw demand data (i.e., sales history) plays an important role in optimizing operations. Therefore, **getting a better sense of demand trends** is mandatory to improve the supply chains. 

To be more precise, accurately forecasting demand is the only practical way to get closer to your business goal. That's why the third course of the specialization was all about demand prediction, and they introduced different types of forecasting techniques. 

Demand can be represented as the following time-series data, and a good forecasting method takes into account its patterns (e.g., seasonality, noise).

![series](/images/holt-winters/series.png)

It is important to note that **we do NOT necessarily have to use complex techniques** such as machine learning **to achieve the best prediction results**; taking a step-by-step approach and choosing the right method at the right time would be the shortest path toward success.

| Method | Overview |
|:---:|:---|
|Naive (Base)|![base](/images/holt-winters/base.png)This basic method simply assumes today's demand is the same as yesterday. It is easy to implement, but sensitive to noise.|
|Cumulative Mean (Simple Average)|![simple_average](/images/holt-winters/simple_average.png)The second method calculates demand at time $t=T$ as an average of all the past data points from $t=0$ to $t=T-1$. This method is more stable against noise compared to the naive method. Note that cumulative mean assumes all prior data is equally useful.|
|Moving Average|![moving_average](/images/holt-winters/moving_average.png)Moving average computes an average of the most recent $N$ (window size) data points. How to choose $N$ is questionable; a smaller value makes the forecast more reactive, whereas larger $N$ leads to a similar result to the cumulative mean method. Typically, people try different $N$ while measuring their accuracy, and choose the most accurate one in the end.|
|Exponential Smoothing|![smoothing](/images/holt-winters/smoothing.png)Exponential smoothing introduces a configurable parameter $\alpha \in \[0.0, 1.0\]$ that controls a balance between a previous data point $d\_{T-1}$ and the most recent forecast $f\_{T-1}$ as follows: $\alpha \times d\_{T-1} + (1-\alpha) \times f\_{T-1}$. The formula allows us to easily tweak a forecasting model by seeking an optimal value of $\alpha$.|

_\* See **[takuti/anompy](https://github.com/takuti/anompy)** for Python implementation of these forecasting methods._

Again, evaluation and continuous improvement are critical in supply chain management, and hence the course finally introduced how to measure the accuracy of predictions. The accuracy metrics include but are not limited to: 

- Mean Error (ME; suitable for measuring the tendency of a forecast model i.e., over-forecast, under-forecast), 
- Mean Absolute Percent Error (MAPE), and 
- Mean Squared Error (MSE; emphasize the negative impact of larger errors). 

### Sourcing

So far, we've seen the process of forecasting, ordering, storing, and delivering the products. But where were these products originally coming from? 

Regardless of raw material or intermediate components, purchasing is a required effort for a company to run a business. Here, optimizing the purchase activities is key for the companies to manage their costs and make their supply chain sustainable.

First, I'd like to highlight the list of **right**s a good supply chain must satisfy:

> Buy the **right** material, at the **right** quantity, at the **right** quality, from the **right** source, at the **right** price. [...] Delivered at the **right** time, to the **right** location, with the **right** transportation mode, at the **right** level of service. And finally, all of this has to be managed with the **right** contract and the **right** length of payment terms. &mdash; "[Supply Chain Sourcing](https://www.coursera.org/learn/sourcing)" on Coursera

To ensure the company is doing the "right" things, a procurement department is in charge of purchasing activities in a centralized manner; they establish relationships with suppliers while having a better view of sales and price, and pass the baton to the following manufacturing and logistics department.

The right selection of suppliers is defined not only from a **risk management perspective** (e.g., service level, redundancy against catastrophic event) but also **environmental, social, and economical aspects**. The course illustrated the examples of [Patagonia](https://www.patagonia.com/our-footprint/) and [Johnson & Johnson](https://www.jnj.com/partners/supplier-diversity) who have explicit criteria in this regard.

Speaking of relationship with suppliers, [Kraljic Matrix](https://en.wikipedia.org/wiki/Kraljic_matrix) splits the suppliers into four different categories depending on their risk and business impact.

| Category | Characteristics |
|:---|:---|
|Strategic supplier|A truly established win-win relationship that leads to mutual benefit between our company and supplier. It'll be a long-term relationship that co-creates value and innovation together. [Coca-Cola and McDonald's](https://www.nytimes.com/2014/05/16/business/coke-and-mcdonalds-working-hand-in-hand-since-1955.html) is one example of sharing mutual benefits. |
|Bottleneck suppliers|Setting up a tight control and manage risk is the most important thing to do for these suppliers. We must diversify the risks to prepare better for any undesired circumstances.|
|Noncritical, routine supplier|Simplicity matters. We don't want to spend too much time and money to work with these suppliers, and hence reducing complexity and automating/simplifying the process as much as possible is the best thing to do.|
|Leverage supplier|Cost and quantity are simply important, and we should aggressively negotiate with these suppliers to get more supply at a lower cost.|

If we successfully targeted suppliers following the classification, the organization could efficiently and effectively establish an end-to-end supply chain by **minimizing cost and risk**, **maximizing profit and service level**, and **retaining a critical mission** (core value) **the organization has**.

*Should we make (insource) or buy (outsource)?* &mdash; The answer is already there when we have a well-defined corporate-wide objective; a clear goal enables a company to accurately evaluate and monitor their suppliers, and the consequence consistently guides them in the right direction in terms of sourcing.

### Bottom line

Supply Chain Management Specialization ends with a course on Supply Chain Management Strategy that let the learners apply L.O.P.S. (Logistics-Operations-Planning-Sourcing) techniques to a real-life supply chain problem. 

We analyzed the supply chain of a medical device company to make up [newly-imposed 2.3% tax on medical devices/products revenue in the US](https://www.forbes.com/sites/waynewinegarden/2018/10/24/repeal-the-medical-device-tax/?sh=57ade6f5334f) and made recommendations for the executives about possible areas of improvement, as well as potential risks they have to take.

Throughout the courses, I realized how supply chain management can be a great source of success for an organization. Even if it's a subtle improvement on a little piece in a complex end-to-end process, the scale of the real-world supply chain makes the effort extremely effective for reducing costs, providing better services, and managing risks. 

The complexity of techniques you employed doesn't matter, and accumulating small wins following the concept of Kaizen is the best approach we could take.