#One common issue with auto-generated text is a mismatch
#between numbers and whether a word is pluralized. For example,
#your code might accidentally say "You bought 1 items" or
#"You have 7 cat".
#
#Write a function called pluralize. pluralize should have three
#parameters: an integer and two strings. The integer is the
#number of some item. The first string is the string to use if
#the item should not be pluralized. The second string is the
#string to use if the item should be pluralized.
#
#pluralize should return the correct string based on the number
#and plural form: it should use the non-plural version if the
#number is 1, and the plural form for all other numbers.
#
#For example:
#
# pluralize(1, "cat", "cats") -> "1 cat"
# pluralize(7, "item", "items") -> "7 items"
# pluralize(127, "octopus", "octopi") -> "127 octopi"


#Add your code here!
def pluralize(n, string1, string2):
    if n > 1:
        return str(n) + " " + string2
    elif n == 1:
        return str(n) + " " + string1


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#1 cat
#7 items
#127 octopi
print(pluralize(1, "cat", "cats"))
print(pluralize(7, "item", "items"))
print(pluralize(127, "octopus", "octopi"))


