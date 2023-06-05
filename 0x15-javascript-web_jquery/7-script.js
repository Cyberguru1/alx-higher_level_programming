#!/usr/bin/node
// hamza saidu
// function to retrieve content using jquery ajax


$(function()
{
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", 
        function(data, status){
            var name = data.name;
            $("#character").text(name);
        });
});

