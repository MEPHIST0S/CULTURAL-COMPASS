// Инициализация карты
const map = L.map('map', {
    center: [40.35, 47.50],
    zoom: 7, 
    maxBounds: [
        [38.25, 44.50],
        [42.00, 50.80]
    ],
    maxBoundsVisibile: true,
    scrollWheelZoom: true
});

// Установка тайлов
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);


const southWest = L.latLng(38.25, 44.50);
const northEast = L.latLng(42.00, 50.80);
const bounds = L.latLngBounds(southWest, northEast);

map.setMaxBounds(bounds);
map.setView([40.35, 47.50], 7);
map.setMinZoom(6);
map.setMaxZoom(15);

map.on('drag', function() {
    map.panInsideBounds(bounds);
});

fetch('/api/sites')
    .then(response => response.json())
    .then(data => {
        data.forEach(site => {
            let marker = L.marker([site.latitude, site.longitude]).addTo(map);
            marker.bindPopup(`<strong>${site.name}</strong><br>${site.description}<br>${site.address}`);
        });
    });

//FILTER
document.getElementById('search').addEventListener('input', filterSites);
document.getElementById('category').addEventListener('change', filterSites);

function filterSites() {
    const searchTerm = document.getElementById('search').value.toLowerCase();
    const selectedCategory = document.getElementById('category').value;
}