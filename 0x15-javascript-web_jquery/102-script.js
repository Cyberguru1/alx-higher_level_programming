#!/usr/bin/node
// hamza saidu
// function to change color, when script is imported from 
// head tag <head>


// document.addEventListener("DOMContentLoaded", function() {
    
// });

$(function() {
    $("#btn_translate").click(function(){
        var lang = $("#language_code").val();
        var url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
        $.get(url, function(data, status){
            $("#hello").text(data.hello);
        });
    });

})
