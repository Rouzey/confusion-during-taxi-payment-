#  define the fare per km
#  define the distance _km
# set total fare so as to multiply the fare per km and the distance km

Define fare_per_km
Define distance_km
Set total_fare = fare_per_km * distance_km

# define the payment method
# define fare paid
# using a boolean to see what payment method the user will use
# also to show if the payment method is invalid
Define payment_method
Define fare_paid
If payment_method is "cash" Then
    Collect fare_paid from the passenger
Else If payment_method is "credit card" Then
    Process credit card payment
Else If payment_method is "digital wallet" Then
    Process digital wallet payment
Else
    Display an error message for invalid payment method
End If

#define the total fare
# define the fare paid
# change would be the fare minus the total
#using a boolean to display the calculated change and give receipt as well as check if the payment is sufficient or insufficient 
Define total_fare
Define fare_paid
Set change = fare_paid - total_fare
If change < 0 Then
    Display an error message indicating insufficient payment
Else
    Display the calculated change and provide a receipt
End If




