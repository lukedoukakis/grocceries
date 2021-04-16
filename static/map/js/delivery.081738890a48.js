function initMap() {
    // Create the map.
    const uluru = { lat: 34, lng: -117 };
    const map = new google.maps.Map(document.getElementById('map'), {
      zoom: 9,
      center: uluru, 
      disableDefaultUI: true,
    });

    directionsService = new google.maps.DirectionsService;
    directionsDisplay = new google.maps.DirectionsRenderer({
        map: map
      });

    var userPos = new google.maps.LatLng(accountLoc[0], accountLoc[1]);
    const userImage = "/static/images/male.svg";
    const user = new google.maps.Marker({
        position: userPos,
        map,
        icon: userImage,
    });

    //fix driver image
    var driverPos = new google.maps.LatLng(driverLoc[0], driverLoc[1]);
    const driverImage = "/static/images/car.svg";
    const driver = new google.maps.Marker({
        position: driverPos,
        map,
        icon: userImage,
    });

    //make storeMarkers
    var waypoints = new Array();  
    for(i = 0; i < storeLats.length; i++)
    {
        storeLat = parseFloat(storeLats[i]);
        storeLon = parseFloat(storeLons[i]);

        storePos = new google.maps.LatLng(storeLat, storeLon);
        const store = new google.maps.Marker({
            position: storePos,
            label: "Store " + (i + 1),
            map,
        });
        waypoints.push({
            location: storePos,
            stopover: true,
        });
    }

    //calculate distances here
    calculateAndDisplayRoute(directionsService, directionsDisplay, driverPos, userPos, waypoints);
    
}



function calculateAndDisplayRoute(directionsService, directionsDisplay, pointA, pointB, waypoints) {
    directionsService.route({
      origin: pointA,
      destination: pointB,
      waypoints: waypoints,
      optimizeWaypoints: true,
      travelMode: google.maps.TravelMode.DRIVING
    }, 
    function(response, status) {
        //if api responding correct do this otherwise bail
      if (status == google.maps.DirectionsStatus.OK) {
        directionsDisplay.setDirections(response);

        //gets time in minutes for total trip
        var totalTimeInSeconds = 0;
        var legCount = directionsDisplay.getDirections().routes[directionsDisplay.getRouteIndex()].legs.length;
        for(i = 0; i < legCount; i++)
        {
            totalTimeInSeconds += directionsDisplay.getDirections().routes[directionsDisplay.getRouteIndex()].legs[i].duration.value;
        }
        var hours = Math.floor(totalTimeInSeconds/3600);
        totalTimeInSeconds -= hours * 3600;
        var minutes = Math.floor(totalTimeInSeconds/60);
        var time = hours + " hours & " + minutes + " minutes";
        document.getElementById("deliveryTime").innerHTML = time;

        //gets distance in km
        //var distance = parseFloat(Math.round(directionsDisplay.getDirections().routes[directionsDisplay.getRouteIndex()].legs[0].distance.value / 1000));
        //console.log(distance);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
  }
