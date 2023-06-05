#!/usr/bin/node
// hamza saidu
// function to retrieve content using jquery ajax


$(function()
{
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", 
        function(data, status){
            var result = data.results;
            for (var content = 0; content < result.length; content++) {
                $("#list_movies").append(`<li> ${result[content]["title"]}</li>`);
            }
        });
});
