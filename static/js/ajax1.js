/*$(function(){

    $('#search').keyup(function() {
    
        $.ajax({
            type: "POST",
            url: "/articles/search/",
            data: { 
                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
        
    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}*/

$(function () {
      $('input:radio[name=onOff]').click(function () {
         
         $("#hideYes").hide();
         $("#hideNo").hide();
         $("#hideHeading").hide();
          $.ajax({
            type: "POST",
            url: "/articles/search/",
            data: { 
                'artID': $('#artID').val(),
                'search_text' : $("input[name='onOff']:checked").val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: onOffSuccess,
            dataType: 'html'
        });
          alert("The switch has been flipped!");

      });
  });
function onOffSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}
