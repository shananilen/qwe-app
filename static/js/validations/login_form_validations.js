$(document).ready(function() {
    $("#login_form").validate(


        {

            rules: {
                user_email : {
                    required: true,
                    email: true


                },
                user_pwd: {
                    required: true,

                },


            },

            errorPlacement: function (error, element) {
                error.insertBefore(element.parent());
            },

            messages : {
                user_email: {
                    required: "*Email is required",
                    email: "*Should be a valid email address"
                },
                user_pwd: {
                    required: "*Password is required",
                },

            }



        }







    );
});
