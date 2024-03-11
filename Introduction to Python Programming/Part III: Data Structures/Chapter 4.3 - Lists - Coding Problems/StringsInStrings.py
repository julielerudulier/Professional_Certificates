#Write a function called inside_search. inside_search should
#have two parameters: a list of strings and a string to search
#for. inside_search should return a list of all the indices at
#which the string in the list contains the search string. Note
#that the string at that index does not need to BE the search
#string, but rather must just contain it.
#
#For example:
#
#a_list = ["cat", "cats", "dog", "dogs", "catsup"]
#search_term = "cat"
#inside_search(a_list, search_term) -> [0, 1, 4]
#
#Note that the strings "cat", "cats", and "catsup" all contain
#the search string "cat", and thus the result is their indices:
#[0, 1, 4].
#
#Make sure the list you return is sorted from lowest index to
#highest.


#Add your code here!
def inside_search(a_list, search):
    indices = []
    for i in range(len(a_list)):
        if search in a_list[i]:
            indices.append(i)
    return indices        


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[0, 1, 4]
#[2, 3]
#[1, 4]
#[4]
#[]
cats_and_dogs_list = ["cat", "cats", "dog", "dogs", "catsup"]
print(inside_search(cats_and_dogs_list, "cat"))
print(inside_search(cats_and_dogs_list, "dog"))
print(inside_search(cats_and_dogs_list, "cats"))
print(inside_search(cats_and_dogs_list, "sup"))
print(inside_search(cats_and_dogs_list, "aardvark"))
