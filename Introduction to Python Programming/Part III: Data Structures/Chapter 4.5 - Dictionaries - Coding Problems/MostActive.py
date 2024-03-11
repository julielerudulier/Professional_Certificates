#Write a function called most_active. most_active should take
#one parameter, a dictionary. The dictionary's keys will all
#be strings representing people's names. The dictionary's
#values will be integers representing days of activity on a
#course forum.
#
#most_active should return the name of the most active student
#in the class. That is, most_active should return the key
#whose value is the highest in the dictionary.
#
#For example:
#
#some_dictionary = {"Joyner, David": 14, "Chopra, Deepak": 22, "Winfrey, Oprah": 17}
#most_active(some_dictionary) -> "Chopra, Deepak"
#
#The key "Chopra, Deepak" has the highest value (22), so
#the function returns "Chopra, Deepak". You may assume
#there will not be a tie for most active.


#Add your code here!
def most_active(a_dict):
    days = 0
    winner = ""
    for (key, value) in a_dict.items():
        if value > days:
            days = value
            winner = key
            
    return winner


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Chopra, Deepak
some_dictionary = {"Joyner, David": 14, "Chopra, Deepak": 22, "Winfrey, Oprah": 17}
print(most_active(some_dictionary))

