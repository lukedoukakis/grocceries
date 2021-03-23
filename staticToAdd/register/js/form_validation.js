$('#id_username').on('input', function () {
    var id_user_name = $(this).val();
    $.ajax({
       url: "{% url 'validate_user_name' %}",
       data: {
           'username': id_user_name
       },
       dataType: 'json',
       success: function (data) {
           if (data.is_taken) {
               $("#validate_user_name").show();
               document.getElementById('id_username').style.borderColor = "red";
               document.getElementById("btnAddUser").disabled = true;
           } else {
               $("#validate_user_name").hide();
               document.getElementById('id_username').style.borderColor = "#e7e7e7";
               document.getElementById("btnAddUser").disabled = false;
           }
        }
      });
   });