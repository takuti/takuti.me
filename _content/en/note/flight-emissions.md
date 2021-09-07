---
categories: [Programming, Data Science & Analytics]
date: 2021-03-13
keywords: [emissions, flight, visualization, flights, countries, emission, calculator,
  calculating, obtained, geographical]
lang: en
recommendations: [/note/javascript-save-svg-as-image/, /note/how-to-avoid-a-climate-disaster/,
  /note/datavis-2020/]
title: How Much CO2 Emissions Have Your Flights Made?
---

*Before reading further, play with an interactive data visualization app that I implemented with D3.js & React: **[Flight Emissions Calculator](https://takuti.github.io/flight-emissions/)***

It's been a while since the COVID-19 pandemic arose, and one of the biggest changes in my life was a significant reduction of air travel opportunities both for business and private. This fact is very unfortunate for me because traveling *was* my greatest joy in life.

https://twitter.com/takuti/status/1207165848135168002

However, at the same time, there is a positive side in terms of the environment; it's obvious that air travel is environmentally unfriendly due to its significant amount of CO2 emissions, and hence fewer flights certainly reduce our overall carbon footprint.

### Visualizing flight emissions

To realize the fact, let's see how much CO2 emissions my flights in 2019 have made:

![2019-flight-emissions](/images/flight-emissions/2019.png)

In this figure, colored countries represent that the CO2 footprint of my flights in 2019, which was about **24.239 tonnes**, exceeded their per-capita yearly emissions. That is, I flew too much during the year and made more CO2 emissions than the personal averages of almost all countries in the world. For instance, a single person in Japan produced 8.7 tonnes of CO2 in 2019 on average, and my flight emission was greater than the number. It's shameful, and I shouldn't be proud of myself for being a frequent flyer.

On the other hand, the visualization below depicts I flew significantly less than the last year in 2020 by making approximately **7.3 tonnes** of emissions, which is one-third of 2019's record:

![2020-flight-emissions](/images/flight-emissions/2020.png)

### Key facts and datasets

To begin with, we need to know how much CO2 emissions each flight makes. Although there are many in-depth studies such as [myclimate flight emissions calculation principles](https://www.myclimate.org/fileadmin/user_upload/myclimate_-_home/01_Information/01_About_myclimate/09_Calculation_principles/Documents/myclimate-flight-calculator-documentation_EN.pdf), I simply picked up some numbers reported in a [BBC article](https://www.bbc.com/news/science-environment-49349566); according to the article, **CO2 emissions per passenger per km traveled are 133g for a domestic flight and 102g for a long-haul flight**.

Next, [Per-Capita CO2 Dataset](https://ourworldindata.org/per-capita-co2) in the "Our World in Data" portal tells us how much CO2 a person in each country produces. It's interesting to see the difference between developed and developing countries, and we can intuitively recognize that large countries such as the US and Australia are more environmentally unfriendly than the others. Meanwhile, for me, there are also some non-trivial observations in the dataset; I must educate myself more on the reason why Mongolia produces such an exceptional amount of CO2, for instance.

Finally, geographical locations of airports and distances between them can be obtained from [Open Flights' Airport Database](https://openflights.org/data.html). Note that calculating a distance between two geographical points (i.e., pairs of latitude and longitude) is not straightforward, but `geoDistance` in the [d3-geo](https://github.com/d3/d3-geo) package does the job. See a Wikipedia article about [great-circle distance](https://en.wikipedia.org/wiki/Great-circle_distance#:~:text=The%20great%2Dcircle%20distance%2C%20orthodromic,line%20through%20the%20sphere's%20interior) for more information.

These are the key ingredients to draw the pictures that I showed above.

### Implementation

To implement the visualization, I was able to reuse many code fragments I previously created for **[Datavis 2020: A Free Online Course About D3.js & React](/note/datavis-2020)**; the course already taught me how to visualize a world map, how to add different colors to the countiries, and how to dynamically modify the view with `useState`, `useRef`, and `useCallback`.

One of the most important parts is calculating CO2 emissions of the flights entered into the text area. Assume a hash `airports` enables us to retrieve `[longitude, latitude]` by IATA 3-letter code of an airport (e.g., `HND` for Haneda Airport). Once the calculate button is pressed, the following callback function updates the parameters associated with the contents of the application:

```js
const [coordinates, setCoordinates] = useState([]);
const [emissions, setEmissions] = useState(0);

const handleSubmit = useCallback(_ => {
  const coords = [];

  const totalKm = inputRef.current.value.split('\n').map((route) => {
    const [src, dst] = route.split('-');
    coords.push([airports[src], airports[dst]]);
    return geoDistance(airports[src], airports[dst]) * earthRadius;
  }).reduce((total, curr) => total + curr);

  const emissions = totalKm * emissionsPerKm / 1000000;
  setEmissions(emissions);

  setCoordinates(coords);
});
```

After setting the states, d3-geo helps us a lot to render the information; an array of pairs of coordinates can be easily represented on the map as multiple arcs, and I was able to easily imitate [Great Circle Mapper](http://www.gcmap.com/), a well-known flight visualization tool on the web:

```jsx
const projection = geoEquirectangular();
const path = geoPath(projection);

<path
  className="route"
  d={path({ type: "MultiLineString", coordinates: coordinates })}
/>
```

Eventually, my **[Flight Emissions Calculator](https://takuti.github.io/flight-emissions/)** app integrates flight logs with CO2 emission data on a world map.

### Bottom line

Climate crisis is not somebody else's problem. It is my problem. But understanding the severity is indeed difficult due to the scale of the problem, complexity of the facts, and unfamiliarity of the numbers.

Here, visualization is a powerful tool that conveys the essential information in an interpretable way. Once we obtained the insights, we become able to more confidently and proactively take an action to keep or change the situation. That's why [a good dashboard matters](/note/augmented-analytics).

Last but not least, carefully reviewing visualization and its original data & eagerly seeking additional sources are the crucial next steps. Data becomes outdated, and we make mistakes when learning important facts and converting them into a functional application. Therefore, ensuring the accuracy of visualization is a fundamental step of a project so that no misleading insights are displayed.