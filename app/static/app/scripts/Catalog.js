

$(document).ready(function () {
    $(".btn_gamecard").on("click", function () {
        gameid = this.getAttribute("data-gameid");
        window.location.href = "game/?id="+gameid;
        //alert($(this).text());
    });
    console.log('loaded')
});

function RemoveCart(id) {
    var Cart = {};
    Cart.id = id;    

    $.ajax({
        url: "../ajax/RemoveCartGame/",
        data: { id: id },
        //contentType: "application/json;charset=utf-8",
        //dataType: 'json',
        type: "POST",
        headers: {//<==
            "X-CSRFTOKEN": $('input[name="csrfmiddlewaretoken"]').val()//<==
        },
        success: function (data) {
            if (data != "Error") {
                $('#cart_game_' + id).remove();
                alert('CartRemoved');
            }
            else if (data == "Error") {
                alert("Error");
            }
        },
        error: function (data) {
            alert('Error');
        }

    });
}