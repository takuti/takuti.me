// set leaftlet map
var map = L.map('map').setView([35.72, 139.75], 14);
L.tileLayer('https://api.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    minZoom: 13,
    maxZoom: 16,
    id: 'takuti.5bebb9b7',
    accessToken: 'pk.eyJ1IjoidGFrdXRpIiwiYSI6ImFmM2UxMmFjMGI5MDA2NjIzYmZlODJkYzBkYThkZjAxIn0.VuS-dUlX3RIldJBJstFLMw'
}).addTo(map);
map.scrollWheelZoom.disable();

var categories = {};

httpObj = new XMLHttpRequest();
httpObj.open('get', './bunkyo100.geojson', true);
httpObj.onload = function(){
  // load points from GeoJSON
  var points = JSON.parse(this.responseText)['features'];

  // add markers for each point
  for (var i = 0; i < points.length; i++) {
    var marker = L.marker(points[i]['geometry']['coordinates'].reverse()).addTo(map);
    marker.bindPopup(generatePopupContent(points[i]['properties']));

    var cat = points[i]['properties']['category'];
    if (cat in categories) {
      categories[cat].push(marker);
    } else {
      categories[cat] = [marker];
    }
  }

  document.getElementById('category-checkboxes').innerHTML = generateCategoryCheckboxesContent();
}
httpObj.send(null);

function generatePopupContent(properties) {
  var content = '';
  for (key in properties) {
    content += '<b>' + key + '</b> ' + properties[key] + '<br />';
  }
  return content;
}

function generateCategoryCheckboxesContent() {
  var content = '<span class=\"category-checkbox\"><label><input type=\"checkbox\" name=\"check-all\" onchange=\"checkAll(this);\" checked><b>すべて</b></label></span>';
  for (cat in categories) {
    content += '<span class=\"category-checkbox\"><label><input type=\"checkbox\" name=\"' + cat + '\" onchange=toggleMarkerByCategory(\"' + cat + '\"); checked>' + cat + '(' + categories[cat].length + ')</label></span>';
  }
  return content;
}

function toggleMarkerByCategory(cat) {
  for (var i = 0; i < categories[cat].length; i++) {
    var marker = categories[cat][i];
    if (map.hasLayer(marker)) map.removeLayer(marker);
    else map.addLayer(marker);
  }
}

function checkAll(element) {
  var checkboxes = document.getElementsByTagName('input');
  for (var i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].type == 'checkbox') {
      checkboxes[i].checked = element.checked;
    }
  }

  if (element.checked) {
    for (var cat in categories) {
      for (var i = 0; i < categories[cat].length; i++) {
        var marker = categories[cat][i];
        if (!map.hasLayer(marker)) map.addLayer(marker);
      }
    }
  } else {
    for (var cat in categories) {
      for (var i = 0; i < categories[cat].length; i++) {
        var marker = categories[cat][i];
        if (map.hasLayer(marker)) map.removeLayer(marker);
      }
    }
  }
}
