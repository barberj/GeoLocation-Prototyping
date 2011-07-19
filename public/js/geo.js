function alertPosition(position){
    alert("Latitude: " + position.coords.latitude + " Longitude: " + position.coords.longitude);
}

function getGeoLocal(){
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(initialize_map);
    } else {
        alert("Browser doesn\'t support geolocation");
    }
}

var map;
function initialize_map(position){
    map = new google.maps.Map(document.getElementById('map'), {
         zoom: 5,
         center: new google.maps.LatLng(position.coords.latitude, position.coords.longitude),
         mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    alertPosition(position);
}
