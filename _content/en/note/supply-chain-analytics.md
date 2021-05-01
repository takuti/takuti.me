---
categories: [Programming]
date: 2021-04-30
draft: true
keywords: [zero, youtube, yml, yesterday, 'yes', years, yearly, year, yay, xxx]
lang: en
recommendations: [/note/julia-factorization-machines/, /note/hello-netlify/, /note/machine-learning-product/]
title: Supply Chain Analytics
---


- VASTA - mobilenetwork 3 DCs in US, 2000+ stores
- Push strategy - store model with inventory
  - Phone has short life-cycle
  - inventory = bomb!
  - Big traditional company's advantage has been diminished
  - need to change from growth to efficiency
- Pull strategy - showroom model; demand-based
- Logistics cost in US: 8.93% of total GDP
- Improving customer satisfaction has a huge impact on cost
  - How to achieve high service by minimum cost?
- Analytics -> Quantitative insights
  1. Opportunity identification
  2. Intuition & insight development
  3. Data analytics (confirm intuition)
  4. Implementation w/o sacrificing customer satisfaction

### 1. Opportunity identification

- Industry/product/revenue source overview
- Competitive landscape
- Strength & weakness
- Metrics: Inventory turns

### 2. Drivers and trade-offs in SC Planning (intuitives)

- Factories -> DC (order fullfilment/inventory) -> Store/Customer
- Store needs to meet customer demand
  - Batch, infrequent reprenishment - BestBuy - Truck Load
  - Continuous replenishment - fresh items, grocccery less-than-truck-load (LTL)
  - Direct shipping - min inventory (express shipping)
- Warehouse has inventory pooling effect
  - Economy scale, cheaper
- Market speed - if we have inventory at the time of new product introduction, the company has to "wait" until all inventories are sold
- Intuition of Push vs. Pull strategies
  - Depending on product type (product price, popularity, moving freq)
  - Pull: High value OR slow moving
  - Push: Low value AND fast moving

### 3. Quantitative SP analytics

- Quantify Push vs. Pull strategy
- Inventory holding, shipping, picking/packing, sales volume cost
- Inventory cost rates at stores:
  - Inventory cost per week per unit = Capital cost per week per unit + Deprecation per week per unit = (annual capital cost / 52) + ((product value - liquidation value) / (product life cycle))
- Shipping cost rates (per unit)
  - Push - batch shippping = volume discount, FedEx $2.4 per unit
  - Pull - FedEx $12 flat rate/unit
- Picking/packing cost at DCs
  - Economies of scale in picking/packing
    - First pick / pack - $1
      - For N identical product in Pull, this first-time factor is applied to all N products -> Expensive
    - Subsecent - $0.1; product is already located, and machine is already placed
- Sales and inventory
  - Low moving products is hard to predict demand
- Net impact by Pull: significant inventory saving >>> increase in shipping & picking/packing

### 4. Customer experience and implementation