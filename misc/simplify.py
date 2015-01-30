import simplify
simplify.public_key = "sbpb_ZDg4ZTU2ZDktZWI5ZS00NjYyLWI5YjYtYzFjZDIwZDhhYWVl"
simplify.private_key = "5sAgsRE0N/bmqyVn2ErCyOWmjPhfygMcqWtVTU70lud5YFFQL0ODSXAOkNtXTToq"

payToken = 


payment = simplify.Payment.create({
        "token" : payToken,
        "amount" : "1000",
        "description" : "prod description",
        "currency" : "USD"
})
if payment.paymentStatus == 'APPROVED':
    print "Payment approved"




