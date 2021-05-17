load_image_html = (table, table_position) => {
    let next_image = new Image();
    next_image.src = $(table[table_position]).text();
    next_image.onload = function(){
        if(table_position+1 <= table.length-1){
            load_image_html(table, table_position+1);
        }
    };
};

load_image_response = (table, table_position) => {
    let next_image = new Image();
    next_image.src = table[table_position];
    next_image.onload = function(){
        if(table_position+1 <= table.length-1){
            load_image_response(table, table_position+1);
        }
    };
};

$(document).ready(function(){

    $(".arrow").click(function(){
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

                images_src = [
                    response.next_images_path_dict.image1,
                    response.next_images_path_dict.image2,
                    response.next_images_path_dict.image3,
                    response.next_images_path_dict.image4];

                load_image_response(images_src, 0);
            }
        });
    });

    window.onpopstate = function() {
        location.reload();
    };

    window.onload = function(){
        images_src = ["#preload-1","#preload-2","#preload-3","#preload-4"];
        load_image_html(images_src, 0);
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