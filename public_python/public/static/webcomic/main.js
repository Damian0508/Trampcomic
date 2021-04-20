$(document).ready(function(){

    $(".arrow").click(function(){
        $.ajax({
            url: window.location.pathname,
            data: {
                'element_id': this.id
            },
            success: function(response) {
                window.history.pushState({path:response.new_url},'', response.new_url);

                $("#comic-page").attr("src", response.path);
                $("#en-flag").attr("href", '/en/'+ response.episode +'/'+ response.page +'/');
                $("#pl-flag").attr("href", '/pl/'+ response.episode +'/'+ response.page +'/');
                $("#episode-number").html(response.episode);
            }
        });
    });

    window.onpopstate = function() {
        location.reload();
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