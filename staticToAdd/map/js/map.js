window.onbeforeunload = function(){
  console.log("hello");
};

//creates the mapp then adds all the stores in stores.json for us to see
function initMap() {
    // Create the map.
    const uluru = { lat: 33.9014918720988, lng: -117.87462697321092 };
    const map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: uluru, 
      disableDefaultUI: true,
    });
  
    // Load the stores GeoJSON onto the map.
    map.data.loadGeoJson('/static/map/js/stores.json', {idPropertyName: 'storeid'});

    map.data.forEach((store) => {
      const storeNum = store.getProperty('storeid');
      console.log(storeNum);
    });

    const apiKey = 'AIzaSyDbk5hppk7xa364BV9kbZxlsH36Pv3G01M';
    const infoWindow = new google.maps.InfoWindow();
  
    // Show the information for a store when its marker is clicked.
    map.data.addListener('click', (event) => {
      const category = event.feature.getProperty('category');
      const name = event.feature.getProperty('name');
      const description = event.feature.getProperty('description');
      const hours = event.feature.getProperty('hours');
      const phone = event.feature.getProperty('phone');
      const position = event.feature.getGeometry().get();
      const content = `
        <h2>${name}</h2><p>${description}</p>
        <p><b>Open:</b> ${hours}<br/><b>Phone:</b> ${phone}</p>
      `;
  
      infoWindow.setContent(content);
      infoWindow.setPosition(position);
      infoWindow.setOptions({pixelOffset: new google.maps.Size(0, -30)});
      infoWindow.open(map);
    });

      // Build and add the search bar
  const card = document.createElement('div');
  const titleBar = document.createElement('div');
  const title = document.createElement('div');
  const container = document.createElement('div');
  const input = document.createElement('input');
  const options = {
    types: ['address'],
    componentRestrictions: {country: 'us'},
  };

  card.setAttribute('id', 'pac-card');
  title.setAttribute('id', 'title');
  title.textContent = 'Find the nearest store';
  titleBar.appendChild(title);
  container.setAttribute('id', 'pac-container');
  input.setAttribute('id', 'pac-input');
  input.setAttribute('type', 'text');
  input.setAttribute('placeholder', 'Enter an address');
  container.appendChild(input);
  card.appendChild(titleBar);
  card.appendChild(container);
  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

  // Make the search bar into a Places Autocomplete search bar and select
  // which detail fields should be returned about the place that
  // the user selects from the suggestions.
  const autocomplete = new google.maps.places.Autocomplete(input, options);

  autocomplete.setFields(
      ['address_components', 'geometry', 'name']);

   // Set the origin point when the user selects an address
   //set the image of the user
   const image = "/static/images/male.svg";
   const originMarker = new google.maps.Marker({map: map, icon: image});
   originMarker.setVisible(false);
   let originLocation = map.getCenter();
 
   autocomplete.addListener('place_changed', async () => {
     originMarker.setVisible(false);
     originLocation = map.getCenter();
     const place = autocomplete.getPlace();
 
     if (!place.geometry) {
       // User entered the name of a Place that was not suggested and
       // pressed the Enter key, or the Place Details request failed.
       window.alert('No address available for input: \'' + place.name + '\'');
       return;
     }
 
     // Recenter the map to the selected address
     originLocation = place.geometry.location;
     map.setCenter(originLocation);
     map.setZoom(9);
     //logs the place we recenter too
     //console.log(place);
 
     originMarker.setPosition(originLocation);
     originMarker.setVisible(true);
 
     // Use the selected address as the origin to calculate distances
     // to each of the store locations
     const rankedStores = await calculateDistances(map.data, originLocation);
     showStoresList(map.data, rankedStores);
 
     return;
   });    
  }


  async function calculateDistances(data, origin) {
    const stores = [];
    const destinations = [];
  
    // Build parallel arrays for the store IDs and destinations
    data.forEach((store) => {
      const storeNum = store.getProperty('storeid');
      const storeLoc = store.getGeometry().get();
  
      stores.push(storeNum);
      destinations.push(storeLoc);
    });
  
    // Retrieve the distances of each store from the origin
    // The returned list will be in the same order as the destinations list
    const service = new google.maps.DistanceMatrixService();
    const getDistanceMatrix =
      (service, parameters) => new Promise((resolve, reject) => {
        service.getDistanceMatrix(parameters, (response, status) => {
          if (status != google.maps.DistanceMatrixStatus.OK) {
            reject(response);
          } else {
            const distances = [];
            const results = response.rows[0].elements;
            for (let j = 0; j < results.length; j++) {
              const element = results[j];
              const distanceText = element.distance.text;
              const distanceVal = element.distance.value;
              const distanceObject = {
                storeid: stores[j],
                distanceText: distanceText,
                distanceVal: distanceVal,
              };
              distances.push(distanceObject);
            }
  
            resolve(distances);
          }
        });
      });
  
    const distancesList = await getDistanceMatrix(service, {
      origins: [origin],
      destinations: destinations,
      travelMode: 'DRIVING',
      unitSystem: google.maps.UnitSystem.METRIC,
    });
  
    distancesList.sort((first, second) => {
      return first.distanceVal - second.distanceVal;
    });
  
    return distancesList;
  }

  function showStoresList(data, stores) {
    if (stores.length == 0) {
      console.log('empty stores');
      return;
    }
  
    let panel = document.createElement('div');
    // If the panel already exists, use it. Else, create it and add to the page.
    if (document.getElementById('panel')) {
      panel = document.getElementById('panel');
      // If panel is already open, close it
      if (panel.classList.contains('open')) {
        panel.classList.remove('open');
      }
    } else {
      panel.setAttribute('id', 'panel');
      panel.style.position = 'relative';
      //position said panel
      const mapParent = document.getElementById("map");
      mapParent.appendChild(panel);;
    }
  
  
    // Clear the previous details
    while (panel.lastChild) {
      panel.removeChild(panel.lastChild);
    }
  
    stores.forEach((store) => {
      // Add store details with text formatting
      const storeButton = document.createElement('a');
      storeButton.classList.add('button');
      storeButton.classList.add('btn2');
      storeButton.classList.add('btn-orange');
      const currentStore = data.getFeatureById(store.storeid);
      storeButton.textContent = currentStore.getProperty('name');
      storeButton.id = currentStore.getProperty('storeid');

      //set the parameter to the primaryKey after changing
      storeButton.href = "/storepage/" + storeButton.id;

      //creates the distance portion to be under the store name
      const distanceText = document.createElement('p');
      distanceText.classList.add('distanceText');
      distanceText.textContent = store.distanceText;

      //appends distancetext to button and then puts button onto the panel
      storeButton.appendChild(distanceText)
      panel.appendChild(storeButton);
    });
  
    // Open the panel
    panel.classList.add('open');

    
    return;
  } 