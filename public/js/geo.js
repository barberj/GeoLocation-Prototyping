function alertPosition(position){
    alert("Latitude: " + position.coords.latitude + " Longitude: " + position.coords.longitude);
}

function getGeoLocal(){
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(alertPosition);
    } else {
        alert("Browser doesn\'t support geolocation");
    }
}
