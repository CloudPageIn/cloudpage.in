<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function() {
    $("#contactForm").submit(function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Gather form data
        var name = $("#name").val();
        var email = $("#email").val();
        var phone = $("#phone").val();
        var message = $("#message").val();

        // AJAX request to submit the form data to the server
        $.ajax({
            type: "POST",
            url: "process.php", // Replace with your server-side script
            data: {
                Name: name,
                Email: email,
                Phone: phone,
                Message: message
            },
            success: function(response) {
                // Show a success message to the user
                alert("Thank you for contacting us. We will get back to you shortly.");
                
                // Optionally, reset the form
                $("#contactForm")[0].reset();
            },
            error: function(error) {
                alert("Oops! Something went wrong. Please try again later.");
            }
        });
    });
});
</script>
