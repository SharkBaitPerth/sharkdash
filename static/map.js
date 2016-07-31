var map = L.map('map').setView([-31.9505, 115.8605], 10);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw', {
  maxZoom: 18,
  attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
  '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
  'Imagery © <a href="http://mapbox.com">Mapbox</a>',
  id: 'mapbox.light'
}).addTo(map);

L.AwesomeMarkers.Icon.prototype.options.prefix = 'fa';

var greenMarker = L.AwesomeMarkers.icon({
    icon: 'check',
    markerColor: 'green'
  });

var orangeMarker = L.AwesomeMarkers.icon({
    icon: 'exclamation',
    markerColor: 'orange'
  });

var redMarker = L.AwesomeMarkers.icon({
    icon: 'exclamation-triangle',
    markerColor: 'red'
  });

var cottesloe = L.marker([-31.996, 115.7431], {icon: greenMarker}).addTo(map);
