$(document).ready(function(){

    $(".arrow").click(function(){
        $.ajax({
            url: window.location.pathname,
            data: {
                'element_id': this.id
            },
            success: function(response) {
                window.history.pushState("", "", response.new_url);
                // window.history.pushState({"html":document.html,"pageTitle":document.pageTitle}, "", response.new_url);

                $("#comic-page").attr("src", response.path);
                $("#episode-number").html(response.episode);
            }
        });
    });
});