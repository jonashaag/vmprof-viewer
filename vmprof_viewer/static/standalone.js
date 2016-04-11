var app = angular.module(
    'vmprof', ['ngRoute', 'vmprof.controllers'], function($routeProvider) {
        $routeProvider
            .when('/:log', {
                templateUrl: 'static/details.html',
                controller: 'details'
            })
            .otherwise({
                redirectTo: '/'
            });

    });
