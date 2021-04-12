function initMap() {
    // Create the map.
    const uluru = { lat: 34, lng: -117 };
    const map = new google.maps.Map(document.getElementById('map'), {
      zoom: 9,
      center: uluru, 
      disableDefaultUI: true,
    });

    const image = "/static/images/male.svg";
    const beachMarker = new google.maps.Marker({
        position: { lat: accountLoc[0], lng: accountLoc[1] },
        map,
        icon: image,
    });

    console.log(storeLats);
    console.log(driverLoc);
}
