#One common function of online text-parsers is trying to find
#known text in a block of other text. For example, from a web
#site, we might want to find any phone numbers present on the
#web site.
#
#Write a function called find_phone_number. The function
#should have one parameter, a string. The function should
#return the phone number that was present in the string.
#
#For this problem, you may make the following assumptions:
#
# - The phone number will be all digits, such as 4043219876.
# - There will only be one phone number in the string.
# - There will be a phone number in the string.
# - Either the phone number will be at the start or end of
#   the string, or it will have spaces on either side of it.
#
#There may be other numbers in the string, but there will only
#be one 10-digit number. Find and return that number as a
#string.
#
#Hint: There are lots of different ways to do this. Think about
#all the tools at your disposal: split, find, casting strings
#to integers, error handling, etc.!


#Add your code here!
def find_phone_number(string):
    i = 0
    number = ""
    while i < len(string):
        if string[i].isdigit():
            number = number + string[i]
            if len(number) == 10:    
                return number
            else:
                i += 1
            
        else:
            number = ""
            i +=1
    
    return number


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#4049876543
#7705551234
#6789123456
print(find_phone_number("hello 4049876543 goodbye"))
print(find_phone_number("7705551234 this is alex"))
print(find_phone_number("doh ray me abc 123 its 6789123456"))
