


$(document).ready(function () {
    $('.form-add').submit(function (e) {
        e.preventDefault();
        var form = $(this);
        var form_action = form.attr('action');
        var form_serialize = form.serialize();
        $.ajax({
            method: 'POST',
            type: 'json',
            url: form_action,
            data: form_serialize,
            success: function (data) {
                console.log(data);
                document.getElementById("demo").innerHTML = "Add to List";

                setTimeout(function(){
                    document.getElementById("demo").innerHTML = '';
                }, 500);
            }
        });
    });
    $('.form-add2').submit(function (f) {
        f.preventDefault();
        var form2 = $(this);
        var form2_action = form2.attr('action');
        var form2_serialize = form2.serialize();
        $.ajax({
            method: 'POST',
            url: form2_action,
            data: form2_serialize,
            success: function (data) {
                console.log(data);
                document.getElementById("demo1").innerHTML = "Add to List";
                setTimeout(function(){
                    document.getElementById("demo1").innerHTML = '';
                }, 500);
            }
         });
    });
});
