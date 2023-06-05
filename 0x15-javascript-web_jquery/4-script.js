#!/usr/bin/node
// click function with css


$(function()
{
    $("#toggle_header").click(function(){
        var color = trans($("header").css("color"));
        if (color == "#00ff00") {
            $("header").css("color", "#ff0000")
        } else {
            $("header").css("color", "#00ff00")
        };
        function trans(bg) {
            bg = bg.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
            function hex(x) {
                return ("0" + parseInt(x).toString(16)).slice(-2);
            }
            return "#" + hex(bg[1]) + hex(bg[2]) + hex(bg[3]);
        };
});
})
