#!/usr/bin/node
// hamza saidu
// function to retrieve content using jquery ajax


$(function()
{
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", 
        function(data, status){
            var hello = data.hello;
            $("#hello").text(hello);
        });
});

