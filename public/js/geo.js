function alertPosition(position){
    console.log("Latitude: " + position.coords.latitude + " Longitude: " + position.coords.longitude);
}

function getGeoLocal(){
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(initialize_map);
    } else {
        alert("Browser doesn\'t support geolocation");
    }
}

var map, marker;
function initialize_map(position){
    map = new google.maps.Map(document.getElementById('map'), {
         zoom: 3,
         center: new google.maps.LatLng(position.coords.latitude, position.coords.longitude),
         mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    atlanta = new google.maps.Marker({map: map, icon: 'http://www.google.com/intl/en_us/mapfiles/ms/micons/blue.png', position: new google.maps.LatLng(position.coords.latitude, position.coords.longitude)});
    chicago = new google.maps.Marker({map: map, position: new google.maps.LatLng(41.879535, -87.624333)});
    new_york = new google.maps.Marker({map: map, position: new google.maps.LatLng(40.7560540, -73.9869510)});
    alertPosition(position);
}
