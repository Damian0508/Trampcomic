$(document).ready(function(){

    $(".arrow").click(function(){
        // $("#comic-page").css("opacity", "0.5");
        $.ajax({
            url: window.location.pathname,
            data: {
                'element_id': this.id
            },
            success: function(response) {
                window.history.pushState({path:response.new_url},'', response.new_url);

                $("#comic-page").attr("src", response.image_path);
                $("#en-flag").attr("href", '/en/'+ response.episode +'/'+ response.page +'/');
                $("#pl-flag").attr("href", '/pl/'+ response.episode +'/'+ response.page +'/');
                $("#episode-number").html(response.episode);
                $("#page-number").html(response.page + '/'+ response.nr_of_pages);

                var next_image1 = new Image();
                var next_image2 = new Image();
                next_image1.src = response.next_image_path_1;
                next_image2.src = response.next_image_path_2;

            }
        });
    });

    window.onpopstate = function() {
        location.reload();
    };

    window.onload = function(){
        console.log('now');
        var next_image1 = new Image();
        var next_image2 = new Image();
        next_image1.src = $("#preload-1").text();
        next_image2.src = $("#preload-2").text();
    };
});

$(document).keyup(function(e) {
    if(e.which == 37) {
        $("#previous-page").click();
    };
    if(e.which == 39) {
        $("#next-page").click();
    }
});