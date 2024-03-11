#Write a function called search_for_string() that takes two
#parameters, a list of strings, and a string. This function
#should return a list of all the indices at which the
#string is found within the list.
#
#You may assume that you do not need to search inside the
#items in the list; for examples:
#
#  search_for_string(["bob", "burgers", "tina", "bob"], "bob")
#      -> [0,3]
#  search_for_string(["bob", "burgers", "tina", "bob"], "bae")
#      -> []
#  search_for_string(["bob", "bobby", "bob"])
#      -> [0, 2]
#
#Use a linear search algorithm to achieve this. Do not
#use the list method index.
#
#Recall also that one benefit of Python's general leniency
#with types is that algorithms written for integers easily
#work for strings. In writing search_for_string(), make sure
#it will work on integers as well -- we'll test it on
#both.


#Write your code here!
def search_for_string(lst, string):
    result = []
    idx = -1
    for i in lst:
        if i == string:
            idx += 1
            result.append(idx)
        else:
            idx += 1
    return result


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: [1, 4, 5]
sample_list = ["artichoke", "turnip", "tomato", "potato", "turnip", "turnip", "artichoke"]
print(search_for_string(sample_list, "turnip"))
