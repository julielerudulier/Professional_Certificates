car_value = 10000
purchase_year = 2011
car_age = 8
driver_age = 23
electric = True
emissions_passed = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#You're writing some code to determine how much it will cost
#to renew the tag on your license plate. Why? Because I just
#had to pay my tag renewal, and if I have to deal with this
#mess, so do you. 😛
#
#Georgia's tag renewal policies are unnecessarily
#complicated. I've simplified them to make this problem even
#doable. They are:
#
# - Everyone pays $20.
# - If you purchased your car before 2013 (in 2012 or earlier),
#   you also pay 1% of its current value in additional tax.
# - If the car is electric, you pay an additional $200 fee.
#   (This is real.)
# - To renew, you must have passed an annual emissions check,
#   unless your car is electric, or if you're 65 or over and
#   the car's age is 10 years or older.
#
#Your code should print one of two messages. If the person
#needs to pass an emissions test in order to renew their tag,
#it should print, "You must pass an emissions test first."
#This would be the message to print if emissions_passed is
#False and if they are not eligible for either exemption
#mentioned above.
#
#If the person is eligible to renew their tag, the code should
#print: "Your renewal fee is $__.", where __ is the renewal
#cost. Round the renewal fee to the nearest integer. This will
#be $20, plus $200 if the car is electric, plus 1% of car_value
#if the purchase_year is less than or equal to 2012.


#Add your code here!

total = 0

if not emissions_passed and not (electric or driver_age >= 65 and car_age >= 10):
    print("You must pass an emissions test first.")
else:
    total += 20
    if purchase_year < 2013:
        total = total + (car_value * 0.01)
    if electric:
        total += 200
    print("Your renewal fee is $" + str(int(total)) + ".")
    


