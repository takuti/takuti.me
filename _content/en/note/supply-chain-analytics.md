---
categories: [Business, Data Science]
date: 2021-05-07
draft: true
keywords: [zero, youtube, yml, yesterday, 'yes', years, yearly, year, yay, xxx]
lang: en
recommendations: [/note/julia-factorization-machines/, /note/hello-netlify/, /note/machine-learning-product/]
title: Actionable Insights from Supply Chain Analytics
---

After [deepening my knowledge about Supply Chain Management](/note/coursera-supply-chain-management), I became particularly curious about how data helps supply chain management. Here, another course [Supply Chain Analytics](https://www.coursera.org/learn/supply-chain-analytics) illustrated a [real-world example of VASTA](http://scal.business.rutgers.edu/CaseDetail.html), a mobile network career in the US, which made a big change in their distribution strategy as a consequence of supply chain analytics.

A list below is a step-by-step guide to using data for supply chain optimization:

1. Opportunity identification
2. Intuition & insight development
3. Data analytics to confirm intuition
4. Implementation without sacrificing customer satisfaction

Notice that actual analytics work is a limited part of the entire process. As many best practices for data science explain, understanding the domain well, making a better hypothesis, and planning a direction that makes sense to you are the crucial steps to undergo. Plus, the final implementation work happens in the real world (not on your Jupyter notebook!), and hence we shouldn't forget to be considerate of what the data doesn't explicitly tell.

### Opportunity identification

In the first phase, we understand an overview of an industry, product, and current revenue source. 

In case of VASTA, the domain knowledge about telecommunication industry is needed, and we'd like to capture a competitive landscape among the other players such as AT&T and T-Mobile. Eventually, we could identify our strength and weakness relative to the competitors, and the weakness can be an opportunity of improvement.

An identified opportunity for VASTA was the inefficiency in push-based distribution strategy. From three of distribution centers (DCs) in the US, they had regularly shipped their product (cellphones) to more than 2000 physical stores; VASTA has been one of the most traditional telco companies in the country, and the strategy worked well for a long time. However, as a product lifecycle of mobile phones becomes shorter these days, it has become difficult for individual stores to sell out their inventory as planned. Consequently, their logistics and inventory cost were piled up. 

Note that 8.93% of total GDP in the US is associated with logistics cost, according to the course, and the fact indicates how distribution strategy plays an important role to efficiently operate a business that relies on a physical product.

Moreover, high-quality service and customer satisfaction must be achieved while reducing the cost. For instance, we can easily reduce the logistics and inventory cost by simply decreasing the volume of shipment from DCs, but what will happen if the modified plan causes a shortage of in-store stock?

Based on all of the background knowledge above, VASTA ultimately considered shifting their push-based distribution strategy to pull-based strategy. Unlike push strategy that ships products to stores and sells at the onsite locations, pull strategy is a demand-based approach that compiles a product on-demand and directly sends it out from DC to a customer; the role of physical stores in the pull strategy is like a "showroom".

### Intuition: What are drivers and trade-offs in the supply chain?

Once the problem to solve and potential solution are identified, we'll try to have a better understanding of an end-to-end process and compares the trade-offs on a factual basis.

An entire supply chain can be simplified as follows:

```
Factories -> DC (order fulfillment, inventory) -> [Push] Store / [Pull] Customer
```

First, inventory at warehouses is a key piece to balance supply and demand. On one hand, inventory enables companies to economically store a huge amount of products at a lower price on a scalable manner. On the other hand, if market speed doesn't match to the warehousing strategy and there are remaining stocks when a new product has been introduced, the company has to "wait" until all inventories are sold.

Secondly, different products require to have different distribution strategies. To give an example, for an expensive product such as computers and mobile phones, batch and infrequent replenishment via truck load should work sufficiently. Meanwhile, fresh items sold at grocery stores need to be continuously replenished via less-than-truck load.

Therefore, intuition of [push-pull strategy](https://en.wikipedia.org/wiki/Push%E2%80%93pull_strategy) can be listed as follows:

- The right option depends on product type in terms of price, popularity, moving frequency.
- Push strategy works well for **low value AND fast moving** items.
- Pull strategy is suitable for **high value OR slow moving** products.
- Pull strategy makes factory-to-customer direct shipping possible while minimizing inventory.

### Quantitative supply chain analytics

We then quantify push vs. pull strategy to confirm the intuition and find out the best option to take.

On either Excel spreadsheet or your preferred programming tool, each of inventory holding, shipping, picking/packing, sales volume cost can be collected, calculated, and compared each other:

- Inventory holding cost at stores:
  - Inventory cost per week per unit 
  - = Capital cost per week per unit + Deprecation per week per unit 
  - = (annual capital cost / 52 weeks) + ((product value - liquidation value) / (product lifecycle))
- Shipping cost per unit
  - **Push strategy**: Batch shipping; volume discount rate can be applied, and it enables us to save $2.4 per unit in case of FedEx.
  - **Pull strategy**: A flat rate per unit (e.g., $12 at FedEx) is applied for every direct shipment.
- Picking/packing cost at DCs
  - Assume the first pick/pack costs $1.
  - **Push strategy**: Subsequent picking/packing can be done at a lower price (e.g., $0.1) because product is already located and machine is ready for the batch operations.
  - **Push strategy**: The first-time factor is equally applied to all subsequent products, and it'll be more expensive than push.
- Sales volume cost
  - Low moving products is hard to predict demand, and sales volume varies.

Finally, we see a consequence that the pull strategy is characterized by (1) significant inventory saving and (2) increase in shipping & picking/packing. That is, net impact becomes positive only if (1) >>> (2).

### Bottom line: Analytics lead VASTA to the right strategy

Although none of the mathematical tools we've seen were complicated, we could have a clear view of VASTA's distribution strategy thanks to the step-by-step process starting from a hypothesis: *Which push vs. pull strategy works better for VASTA?*

To the end, the following outcomes can be obtained, and VASTA could take an action that changes their push-based strategy to pull-based one considering the characteristics of today's mobile phone market & product.

![push-vs-pull](/images/supply-chain-analytics/push-vs-pull.png)

_\* Captured from [Supply Chain Analytics](https://www.coursera.org/learn/supply-chain-analytics) on Coursera._

A key takeaway from the exercise is that actionable insights cannot be obtained without having a clear understanding and assumption of your problem. In other words, if you come up with good factual insights that the data doesn't tell, data analytics is a final step to validate them and makes you confident to take an action.