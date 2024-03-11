#Write a function called select_a_show. select_a_show
#should have one parameter, an integer representing
#how many minutes until you have to leave.
#select_a_show should return the following:
#
# - If you have 0 or fewer minutes, it should return
#   the string, "You're late!"
# - If you have 1 to 10 minutes, it should return
#   the string, "Leave now, be early!"
# - If you have 11 to 45 minutes, it should return
#   the string, "Watch a comedy!"
# - If you have 46 to 100 minutes, it should return
#   the string, "Watch a drama!"
# - If you have more than 100 minutes, it should return
#   the string, "Watch a movie!"


#Add your function here!
def select_a_show(minutes):
    if minutes <= 0:
        return "You're late!"
    elif minutes <= 10:
        return "Leave now, be early!"
    elif minutes <= 45:
        return "Watch a comedy!"
    elif minutes <= 100:
        return "Watch a drama!"
    else:
        return "Watch a movie!"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#"You're late!", "Leave now, be early!", "Watch a comedy!",
#"Watch a drama!", and "Watch a movie!".
print(select_a_show(-5))
print(select_a_show(5))
print(select_a_show(34))
print(select_a_show(68))
print(select_a_show(124))



