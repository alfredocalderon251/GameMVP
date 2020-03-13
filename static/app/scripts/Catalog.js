

$(document).ready(function () {
    $(".btn_gamecard").on("click", function () {
        gameid = this.getAttribute("data-gameid");
        window.location.href = "game/?id="+gameid;
        //alert($(this).text());
    });
    console.log('loaded')
});