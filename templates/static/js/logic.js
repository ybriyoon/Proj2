var myMap = L.map('mapid', {minZoom: 3}).setView([30.0444, 31.2357], 3);

var southWest = L.latLng(-89.98155760646617, -180),
northEast = L.latLng(89.99346179538875, 180);
var bounds = L.latLngBounds(southWest, northEast);

myMap.setMaxBounds(bounds);
myMap.on("drag", function() {
  myMap.panInsideBounds(bounds, {animate: false});
});

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
  accessToken: API_KEY
}).addTo(myMap);

var lat = [];
var long = [];
var womanname = [];
var womanrole = [];
var womanpic = [];
var desc = [];

mapdata.forEach((mapdata) => {
  lat.push(parseFloat(mapdata.Latitude));
  long.push(parseFloat(mapdata.Longitude));
  womanname.push(mapdata.name);
  womanrole.push(mapdata.role);
  womanpic.push(mapdata.img);
  desc.push(mapdata.description);
});

var i;
for (i = 1; i < mapdata.length; i++) {
  L.marker([lat[i], long[i]]).bindPopup(
    '<img src="' + womanpic[i] + '" width="150" height="150"/><br><strong>' + womanname[i] + '</strong><br><i>' + womanrole[i] + '</i><br><br>' + desc[i]
    ).addTo(myMap);
};