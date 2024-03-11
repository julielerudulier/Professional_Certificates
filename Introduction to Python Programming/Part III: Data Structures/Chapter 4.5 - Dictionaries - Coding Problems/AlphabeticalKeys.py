#One of the confusing things about dictionaries is that they
#are unordered: the keys have no internal ordering to them.
#Sometimes though, you want to look through the keys in a
#particular order, such as printing them alphabetically if
#they represent something like artist names.
#
#For example, imagine if a forum tool used for a course
#exported its data as a dictionary. The keys of the dictionary
#are students' names, and the values are days of activity.
#Your goal is to return a list of students in the class
#in alphabetical order, followed by their days of activity,
#like this:
#Chopra, Deepak: 22
#Joyner, David: 14
#Winfrey, Oprah: 17
#
#Write a function named alphabetical_keys. alphabetical_keys
#should take as input a dictionary, and return a single string.
#The keys of the dictionary will be names and the values will
#be integers. The output should be a single string made of multiple
#lines, following the format above: the name (the key), a colon and
#space, then the number of days of activity (the value), sorted
#alphabetically by key.
#
#Remember, you are _returning_ this as a single string: you're
#going to need to put the \n character after each line.
#
#To convert a dictionary's keys into a list, use this line
#of code:
#keys_as_list = list(the_dict.keys)
#
#From there, you could sort keys_as_list like any normal list.


#Add your code here!
def alphabetical_keys(a_dict):
    keys = list(a_dict.keys())
    keys.sort()
    result = ""
    for key in keys:
        result += key + ": " + str(a_dict[key]) + "\n"
    return result

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Chopra, Deepak: 22
#Joyner, David: 14
#Winfrey, Oprah: 17
the_dictionary = {"Joyner, David": 14, "Chopra, Deepak": 22, "Winfrey, Oprah": 17}
print(alphabetical_keys(the_dictionary))
