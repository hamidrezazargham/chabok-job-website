$(document).ready(function() {
    $('#signupForm').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting in the default way

        // Get form data
        const formData = {
            name: $('#name').val(),
            email: $('#email').val(),
            password: $('#password').val(),
            role: $('input[name=inlineRadioOptions]:checked').val()
        };

        // Post form data to the backend
        $.ajax({
            url: 'https://c042-109-230-67-162.ngrok-free.app/sign-up/', // Replace with your actual backend endpoint
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(data) {
                // Handle the response from the backend
                console.log(data);
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    });
});