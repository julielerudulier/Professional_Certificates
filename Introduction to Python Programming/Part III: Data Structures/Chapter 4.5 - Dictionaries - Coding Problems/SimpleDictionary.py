#-----------------------------------------------------------
#Let's get back to basics for a moment. We're going to write
#a function that very simply reads a dictionary and returns
#a result.
#
#Write a function called safe_lookup. safe_lookup should have
#two parameters: a dictionary and a key. safe_lookup should
#see if the key is in the dictionary. If it is, it should
#return its value. If it not, it should return None (not the
#string, but the value None: return None).
#
#safe_lookup might be used to avoid having to add error
#handling every time a dictionary is used. A programmer could
#call safe_lookup(dict, key) and know that it will not cause
#an error even if key is not found.


#Add your code here!
def safe_lookup(a_dict, a_key):
    if a_key in a_dict:
        return a_dict[a_key]
    else:
        return None


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#1
#2
#3
#None
test_dictionary = {"A": 1, "B": 2, "C": 3}
print(safe_lookup(test_dictionary, "A"))
print(safe_lookup(test_dictionary, "B"))
print(safe_lookup(test_dictionary, "C"))
print(safe_lookup(test_dictionary, "D"))
