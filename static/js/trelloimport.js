
$(document).ready(function(){
    $('#trelloModal').on('show.bs.modal', function(e){
        $('#import_trello_btn').on('click', function(){
            $('#trello_board').submit()
        });
        ;
        $.getJSON(advice_url, function(data){
            $.each(data, function(k , v){
                $('#select_board').append('<option value="'+ v +'">'+ k +'</option>"');
            })
        })
        var a = $('#select_board').children()

    });

    $('#trelloModal').on('hide.bs.modal', function(e){
        $('#select_board > *').remove()
        
    });

})
