#!/usr/bin/node
// hamza saidu
// function to change color, when script is imported from 
// head tag <head>


// document.addEventListener("DOMContentLoaded", function() {
    
// });

$(function() {
    $("#add_item").click(function(){
        $("my_list").append("<li>Item</li>");
    });
    $("#remove_item").click(function(){
        $("my_list").empty("<li>Item</li>");
    });
    $("#clear_item").click(function(){
        $("my_list").remove();
    })
})
