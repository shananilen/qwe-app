$.validator.addMethod("passwordStrength", function(value, element) {
    // Check if the password contains at least one uppercase letter, one lowercase letter,
    // one digit, and one special character
    return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}$/.test(value);
}, "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.");

$(document).ready(function() {



    $("#register_form").validate(


        {

            rules: {
                reg_form_firstname_input : {
                    required: true,


                },
                reg_page_lastname_input : {
                    required: true,


                },
                reg_form_email_input : {
                    required: true,
                    email: true


                },
                reg_form_password_input: {
                    minlength:8,
                    required: true,
                    passwordStrength: true

                },
                reg_form_confirm_pwd_input: {
                    required: true,
                    equalTo: "#form3Example4"
                }


            },

            errorPlacement: function (error, element) {
                error.insertBefore(element.parent());
            },

            messages : {
                reg_form_firstname_input: {
                    required: "*First name is required",
                },
                reg_page_lastname_input: {
                    required: "*Last name is required",

                },
                reg_form_email_input: {
                    required: "*Email is required",
                    email: "*Invalid email address"
                },
                reg_form_password_input: {
                    required: "*Choose a password",
                    minlength: "*Password must have at least 8 characters"
                },
                reg_form_confirm_pwd_input:{
                    required: "*Confirm your password",
                    equalTo: "*password mismatched"
                }

            }



        }







    );
});
