var myGeoObject = new ymaps.GeoObject({
    geometry: {
        type: "Polygon",
        coordinates: [
            [
                [55.75, 37.80],
                [55.80, 37.90],
                [55.75, 38.00],
                [55.70, 38.00],
                [55.70, 37.80]
            ]
        ],
        fillRule: "nonZero"
    },
    properties: {
        hintContent: "Description"
    }
}, {
        fillColor: '#00FF00',
        strokeColor: '#0000FF',
        opacity: 0.5,
        strokeWidth: 5,
    });
myMap.geoObjects.add(myGeoObject);