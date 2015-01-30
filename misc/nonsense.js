function simplifyResponseHandler(data) {
    var $paymentForm = $("#simplify-payment-form");
    // Remove all previous errors
    $(".error").remove();
    // Check for errors
    if (data.error) {
        // Show any validation errors
        if (data.error.code == "validation") {
            var fieldErrors = data.error.fieldErrors,
                    fieldErrorsLength = fieldErrors.length,
                    errorList = "";
            for (var i = 0; i < fieldErrorsLength; i++) {
                errorList += "<div class='error'>Field: '" + fieldErrors[i].field +
                        "' is invalid - " + fieldErrors[i].message + "</div>";
            }
            // Display the errors
            $paymentForm.after(errorList);
        }
        // Re-enable the submit button
        $("#process-payment-btn").removeAttr("disabled");
    } else {
        // The token contains id, last4, and card type
        var token = data["id"];
        // Insert the token into the form so it gets submitted to the server
        $paymentForm.append("<input type='hidden' name='simplifyToken' value='" + token + "' />");
        // Submit the form to the server
        $paymentForm.get(0).submit();
    }
}
$(document).ready(function() {
    
    $('#dateModal').modal({
      keyboard: false
    });

    $('#dateModal').modal('show');


    $("#simplify-payment-form").on("submit", function() {
        // Disable the submit button
        $("#process-payment-btn").attr("disabled", "disabled");
        // Generate a card token & handle the response
        SimplifyCommerce.generateToken({
            key: "sbpb_ZDg4ZTU2ZDktZWI5ZS00NjYyLWI5YjYtYzFjZDIwZDhhYWVl",
            card: {
                number: $("#cc-number").val(),
                cvc: $("#cc-cvc").val(),
                expMonth: $("#cc-exp-month").val(),
                expYear: $("#cc-exp-year").val()
            }
        }, simplifyResponseHandler);
        // Prevent the form from submitting
        return false;
    });

    $('#vegButton').on('click', function(e){
         e.preventDefault();
         $.ajax({
             url: $(this).attr('action'),
             method: $(this).attr('method'),
             success: function(data){ $('#target').html(data) }
         });
     });
});

thedata = {
  id : "4b0abb46-35d0-44d1-a6b3-5e7e26b35ef2", // String of token identifier,
  card : {...}, // Dictionary of the card used to create the token
  used : false, // Boolean of whether this token has been used,
};
