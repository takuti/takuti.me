---
categories: [Programming]
date: 2021-09-04
keywords: [image, save, visualization, html, line, fitbit, interactive, flight, emissions,
  javascript]
lang: en
recommendations: [/note/flight-emissions/, /note/first-vis-with-fitbit/, /note/datavis-2020/]
title: Save HTML <svg> as an Image
---

After playing with [interactive data visualization using D3.js and React](/note/datavis-2020/), I wanted to have a "Download" function so that I can easily save the visualization as an image rather than taking a screenshot of a browser window:

- [Practicing D3 Interactive Data Visualization with Fitbit Activity/Sleep Log](/note/first-vis-with-fitbit/)
- [How Much CO2 Emissions Have Your Flights Made?](/note/flight-emissions/)

In short, it can be achieved by writing a JavaScript snippet that does the following job:

1. `<svg>` to `Blob`
2. `Blob` to `Image`
3. `Image` to `<canvas>`

Eventually, HTML Canvas enables you to save the content in the form of image file. 

For the future reference, let me walk-through the process line-by-line since coming up with a complete snippet wasn't straightforward; there were some "tricky" parts that aren't fully covered by a piece of online resources e.g.:

- [javascript - Convert SVG to PNG with styles - Stack Overflow](https://stackoverflow.com/questions/49666196/convert-svg-to-png-with-styles)
- [Save SVG as an Image](http://techslides.com/save-svg-as-an-image)

Assume we have an SVG drawing `index.html` and its stylesheet e.g., `style.css`:

```html
<svg xmlns="http://www.w3.org/2000/svg">
  <rect width=64 height=64 />
</svg>
```

```css
svg rect {
  fill: blue;
}
```

### SVG to Blob

The first and most confusing step is to convert SVG into a `Blob` object represented by XML:

```js
const svg = document.querySelector('svg');

// CSS must be explicitly embedded
const style = createStyleElementFromCSS();
svg.insertBefore(style, svg.firstChild);

const data = (new XMLSerializer()).serializeToString(svg);
const svgBlob = new Blob([data], {
    type: 'image/svg+xml;charset=utf-8'
});

// remove the temporarily injected CSS
style.remove();
```

To unlock the conversion, we have to keep the following points in our mind:

1. Define `<svg>` with `xmlns="http://www.w3.org/2000/svg"`
2. Embed `style` inside of the `<svg>` tag

Here, the inserted `style` element can be dynamically constructed as follows:

```js
const createStyleElementFromCSS = () => {
  // assume index.html loads only one CSS file in <header></header>
  const sheet = document.styleSheets[0];

  const styleRules = [];
  for (let i = 0; i < sheet.cssRules.length; i++)
    styleRules.push(sheet.cssRules.item(i).cssText);

  const style = document.createElement('style');
  style.type = 'text/css';
  style.appendChild(document.createTextNode(styleRules.join(' ')))

  return style;
};
```

Although we defined the style in the separate `.css` file, it's important for `<svg>` to explicitly contain the information. Otherwise, a saved image loses all the information about color, font, shape, etc. 

Consequently, the `svgBlob` object has the XML representation of an SVG element below:

```html
<svg xmlns="http://www.w3.org/2000/svg">
  <style type="text/css">
    svg rect { fill: blue; }
  </style>
  <rect width=64 height=64 />
</svg>
```

### Blob to Image

Next, loading the `Blob` object to `Image` allows the application to treat the original SVG in a more handy way:

```js
// convert the blob object to a dedicated URL
const url = URL.createObjectURL(svgBlob);

// load the SVG blob to a flesh image object
const img = new Image();
img.addEventListener('load', () => {
  // (Next step: Image to Canvas)
});
img.src = url;
```

For instance, `url` denotes a reference to the object as: `blob:http://localhost:3000/a1c7704c-09a5-46f5-a102-7bc84d8ecbce`

### Image to Canvas

Once `Image` recognizes the Blob URL, we finally draw the image on an HTML Canvas and trigger a download operation.

```js
img.addEventListener('load', () => {
  // draw the image on an ad-hoc canvas
  const bbox = svg.getBBox();

  const canvas = document.createElement('canvas');
  canvas.width = bbox.width;
  canvas.height = bbox.height;

  const context = canvas.getContext('2d');
  context.drawImage(img, 0, 0, bbox.width, bbox.height);

  URL.revokeObjectURL(url);

  // trigger a synthetic download operation with a temporary link
  const a = document.createElement('a');
  a.download = 'image.png';
  document.body.appendChild(a);
  a.href = canvas.toDataURL();
  a.click();
  a.remove();
});
```

Notice that the event handler cleanses the environment by removing `url` and `a`, an ad-hoc download link. Meanwhile, in case you want to obtain an image in a particular type, `canvas.toDataURL()` takes an optional parameter like `canvas.toDataURL('image/jpeg')`. 

That's it. Now we're capable of extracting an image file from an HTML-coded SVG illustration. [My flight emission calculator app](https://takuti.github.io/flight-emissions/) already has a Download button for the desired use case. 

A set of code snippets below is a complete, compact example of things I explained in this article.

<script async src="//jsfiddle.net/zvma7oLt/3/embed/html,css,js/"></script>