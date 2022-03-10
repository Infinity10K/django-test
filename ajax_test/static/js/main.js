function fetchdata(){
    $.ajax({
        url: "{% url 'index' %}",
        type: 'GET',
        success: function(data){
            $("timeNow").empty();
            $("timeNow").append(data);
        },
        error: function(error){
            console.log(error)
        },

        timeout: 1
    });
}


$(document).ready(function(){
    setInterval(fetchdata, 5000);
});