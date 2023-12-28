$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting in the default way

        // Get form data
        const formData = {
            email: $('#email').val(),
            password: $('#password').val()
        };

        $.ajax({
            url: '/your-backend-endpoint', // Replace with your actual backend endpoint
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