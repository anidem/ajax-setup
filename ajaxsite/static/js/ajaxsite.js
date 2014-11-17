// ajaxsite.js
jQuery(function($) {
    // Using validation to check for the presence of an input
    $( "#ajaxform" ).submit(function( event ) {
        event.preventDefault();
        $.ajax({
            url : "/comment/add/",
            type : "POST",
            data : $( "#ajaxform" ).serializeArray(),
            dataType : "json",

            // handle a successful response
            success : function(json) {
                $('#comments').append('<div class="message">' + json.subject + ': ' + json.text + '</div>');
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + err); // provide a bit more info about the error to the console
            }
        });        
    });

    $(document).ready(function() {

    });
})