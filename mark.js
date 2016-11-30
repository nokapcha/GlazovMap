


ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
        center: [58.140429, 52.674267],
        zoom: 14
    }, {
            searchControlProvider: 'yandex#search'
        })
        ,
        myPlacemark0 = new ymaps.Placemark([58.141162, 52.643032], {
            hintContent: 'decsription',
            balloonContent: ''
        }, {
                iconLayout: 'default#image',
                iconImageHref: '/images/schools.png',
                iconImageSize: [32, 32],
                iconImageOffset: [-16, -16]
            })
        ,
        myPlacemark100 = new ymaps.Placemark([58.172289, 52.636147], {
            hintContent: 'School no -1',
            balloonContent: ''
        }, {
                iconLayout: 'default#image',
                iconImageHref: '/images/schools.png',
                iconImageSize: [32, 32],
                iconImageOffset: [-16, -16]
            })
        ,
        myPlacemark1 = new ymaps.Placemark([58.139312, 52.666964], {
            hintContent: 'Comfortable',
            balloonContent: ''
        }, {
                iconLayout: 'default#image',
                iconImageHref: '/images/cafe.png',
                iconImageSize: [32, 32],
                iconImageOffset: [-16, -16]
            })
        ,
        myPlacemark2 = new ymaps.Placemark([58.139903, 52.680059], {
            hintContent: 'Mi-Mi-Np',
            balloonContent: ''
        }, {
                iconLayout: 'default#image',
                iconImageHref: '/images/cafe.png',
                iconImageSize: [32, 32],
                iconImageOffset: [-16, -16]
            })
        ,
        myPlacemark3 = new ymaps.Placemark([58.140203, 52.677312], {
            hintContent: 'Southern Fried Chicken',
            balloonContent: ''
        }, {
                iconLayout: 'default#image',
                iconImageHref: '/images/cafe.png',
                iconImageSize: [32, 32],
                iconImageOffset: [-16, -16]
            })
        ,
        myPlacemark4 = new ymaps.Placemark([58.139604, 52.675449], {
            hintContent: 'Fathers house',
            balloonContent: ''
        }, {
                iconLayout: 'default#image',
                iconImageHref: '/images/cafe.png',
                iconImageSize: [32, 32],
                iconImageOffset: [-16, -16]
            })
        ; myMap.geoObjects.add(myPlacemark0);
    myMap.geoObjects.add(myPlacemark100);
    myMap.geoObjects.add(myPlacemark1);
    myMap.geoObjects.add(myPlacemark2);
    myMap.geoObjects.add(myPlacemark3);
    myMap.geoObjects.add(myPlacemark4);
});



