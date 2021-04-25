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

        startTime = new Date().getTime()/1000;
        totalDeliveryTime = totalTimeInSeconds;

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

  var totalDeliveryTime = 0;
  var orderCompleted = false;
  //runs every 5 seconds and checks order completion
  var intervalId = window.setInterval(function(){
    if(!orderCompleted)
    {
      updateStatus();
    }
    else
    {
      //delete items in cart here
    }
  }, 2000);

  var startTime = 0;
  function updateStatus()
  {
    //do an update if delivery time is set
    if(totalDeliveryTime != 0)
    {
      var timeDifference = new Date().getTime()/1000 - startTime;
      var percent = timeDifference/totalDeliveryTime;
      var statusPiece = document.getElementById("status");

      //switch on time completed for changing status
      switch(true)
      {
        case percent >= .1 && percent <= .4:
          statusPiece.innerHTML = "Status: Order processed. Driver on way to store";
          break;

        case percent >= .4 && percent <= .6:
          statusPiece.innerHTML = "Status: Order Finished being put together";
          break;

        case percent >= .6 && percent <= .9:
          statusPiece.innerHTML = "Status: Driver has picked the order up";
          break;

        case percent >= .9 && percent <= 1:
          statusPiece.innerHTML = "Status: Driver is almost to your house";
          break;

        case percent >= 1: //finished
          statusPiece.innerHTML = "Status: Order Delivered";
          orderCompleted = true;
          break;
      }
    }
  }
