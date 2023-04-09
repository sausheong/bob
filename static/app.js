
t = 0;
let resp = "";
$(document).ready(function(){  
    $('#prompt').keypress(function(event){        
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == 13){
            $('#send').click();
            return false;
        }
    });  

    $('#send').click(function(e){
        e.preventDefault();
        var prompt = $("#prompt").val().trimEnd();
        $("#prompt").val("");
        $("#printout").append(
            "<div class='mx-3 pt-3 fs-5 fw-semibold text-primary-emphasis'>" + 
            "<i class='fa-regular fa-comments'></i> " +
            prompt + 
            "</div>"            
        );        
        $(".border").animate({ scrollTop: $('.border').prop("scrollHeight")}, 1000);
        bob(prompt);        
    });     
  
    $('#search').click(function(e){
        e.preventDefault();
        var prompt = $("#prompt").val().trimEnd();
        $("#prompt").val("");
        $("#printout").append(
            "<div class='mx-3 pt-3 fs-5 fw-semibold text-primary-emphasis'>" + 
            "<i class='fa-solid fa-magnifying-glass-arrow-right'></i> " +
            prompt + 
            "</div>"            
        );        
        $(".border").animate({ scrollTop: $('.border').prop("scrollHeight")}, 1000);
        bob(prompt, "/search");        
    });      
});  

function bob(prompt, action="/query") {
    function myTimer() {
        $("#bot").removeClass("fa-solid fa-robot");
        $("#bot").addClass("spinner-border");   
        t++;
    }
    const myInterval = setInterval(myTimer, 1000);          
   
    $.ajax({
        url: action,
        method:"POST",
        data: JSON.stringify({input: prompt}),
        contentType:"application/json; charset=utf-8",
        dataType:"json",
        success: function(data){
            $("#printout").append(
                "<div class='mx-3'>" + 
                "<p>" + 
                data.markdown + 
                " <small>(" + t + "s)</small> " + 
                "</p>" +                 
                "<button type='button' class='btn btn-sm btn-outline-secondary' onclick='javascript:save_file();'>" + 
                "save to file <i class='fa-solid fa-download'></i>" + 
                "</button></div>" +                
                "</div>");       
            $(".border").animate({ scrollTop: $('.border').prop("scrollHeight")}, 1000);
            clearInterval(myInterval);
            $("#bot").addClass("fa-solid fa-robot");
            $("#bot").removeClass("spinner-border");              
            t = 0;
            resp = data.response;
        }
    });   
}

function save_file() {
    var blob = new Blob([resp], {type: "text/plain;charset=utf-8"});
    saveAs(blob, "response.txt");    
}