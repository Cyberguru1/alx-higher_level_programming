#!/usr/bin/node
// click function with to remove and empty list elements

$(function(){
    $("#add_item").click(function(){
        $(".my_list").append("<li>Item</li");
    });
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
     };

    async function loop(){
        for (var i = 0; i < 100; i++) {
            await sleep(i * 10);
            $(".my_list").append(`"<li>item ${i} </li>"`);
            var colos = `#ff00${i.toString(16)}`;
            $(".my_list li").css("color", colos);
            if (i % 10 == 0) {
                $(".my_list").empty();
            }
            else if (i == 99){
                i = 0;
            }

        }
    }
    loop();
    $("#r_item").click(function(){
        $(".my_list").empty();
    })
})

