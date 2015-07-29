<?php

function acceptable($point, $q, $category, $area) {
  if ($q !== '' &&
       (strpos($point['properties']['read'], $q) === false &&
        strpos($point['properties']['name'], $q) === false))  return false;

  if ($category !== '' && strpos($point['properties']['category'], $category) === false) return false;

  preg_match('/文京区([^0-9A-Za-z\-]+)[0-9\-]+/', $point['properties']['address'], $match);
  if ($area !== '' && $match[1] !== $area) return false;

  return true;
}

$q = isset($_GET['q']) ? urldecode($_GET['q']) : '';
$category = isset($_GET['category']) ? urldecode($_GET['category']) : '';
$area = isset($_GET['area']) ? urldecode($_GET['area']) : '';

$json = json_decode(file_get_contents('../bunkyo100.geojson'), true);
$points = $json['features'];

for ($i = 0; $i < count($points); $i++) {
  if (!acceptable($points[$i], $q, $category, $area)) unset($json['features'][$i]);
}

$json['features'] = array_values($json['features']);

header('Content-Type: text/javascript; charset=utf-8');
echo json_encode($json);
