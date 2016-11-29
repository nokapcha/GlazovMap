


ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
        center: [58.140429, 52.674267],
        zoom: 14
    }, {
            searchControlProvider: 'yandex#search'
        })
        ,
        myPlacemark0 = new ymaps.Placemark([100.0, 100.0], {
            hintContent: 'decsriptio',
            balloonContent: ''
        }, {
                iconLayout: 'default#image',
                iconImageHref: '/images/schools.png',
                iconImageSize: [32, 32],
                iconImageOffset: [0, 0]
            })
        ,
        myPlacemark1 = new ymaps.Placemark([58.139312, 52.666964], {
            hintContent: 'Comfortable',
            balloonContent: ''
        }, {
                iconLayout: 'default#image',
                iconImageHref: '/images/cafe.png',
                iconImageSize: [32, 32],
                iconImageOffset: [0, 0]
            })
        ,
        myPlacemark2 = new ymaps.Placemark([58.139903, 52.680059], {
            hintContent: 'Mi-Mi-Np',
            balloonContent: ''
        }, {
                iconLayout: 'default#image',
                iconImageHref: '/images/cafe.png',
                iconImageSize: [32, 32],
                iconImageOffset: [0, 0]
            })
        ,
        myPlacemark3 = new ymaps.Placemark([58.140203, 52.677312], {
            hintContent: 'Southern Fried Chicken',
            balloonContent: ''
        }, {
                iconLayout: 'default#image',
                iconImageHref: '/images/cafe.png',
                iconImageSize: [32, 32],
                iconImageOffset: [0, 0]
            })
        ,
        myPlacemark4 = new ymaps.Placemark([58.139604, 52.675449], {
            hintContent: 'Father's house',
balloonContent: ''
}, {
                iconLayout: 'default#image',
                iconImageHref: '/images/cafe.png',
                iconImageSize: [32, 32],
                iconImageOffset: [0, 0]
            })
        ; myMap.geoObjects.add(myPlacemark0);
    myMap.geoObjects.add(myPlacemark1);
    myMap.geoObjects.add(myPlacemark2);
    myMap.geoObjects.add(myPlacemark3);
    myMap.geoObjects.add(myPlacemark4);
});



