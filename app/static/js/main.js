function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

    $(".get_delete_id").on("click", function () {
        var productID = $(this).attr("data-id");
        window.localStorage.setItem('item', productID);
    });


setInterval(function myFunction() {
    $.ajax({
        url: '/logic/',
        type: 'post',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        success: function (response) {
            document.getElementById("random_number").innerHTML = response.random_number;

        },
        error:
        function () {
            document.getElementById("random_number").innerHTML = 'Cannot get number';
        }

    });
}, 5000);