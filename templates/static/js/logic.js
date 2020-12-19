var myMap = L.map('mapid').setView([30.0444, 31.2357], 2);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
  accessToken: API_KEY
}).addTo(myMap);

var marker = L.marker([40.7128, -74.006]).addTo(myMap);

var lat = [];
var long = [];

mapdata.forEach((mapdata) => {
  lat.push(parseFloat(mapdata.Latitude));
  long.push(parseFloat(mapdata.Longitude));
});

var i;
for (i = 0; i < mapdata.length; i++) {
  L.marker([lat[i], long[i]]).addTo(myMap);
};