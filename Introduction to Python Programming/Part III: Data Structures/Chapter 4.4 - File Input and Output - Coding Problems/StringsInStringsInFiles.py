#Write a function called search_in_files. search_in_files
#should have two parameters: a filename and a string to search for.
#search_in_files should return a list of line numbers as integers
#where the string appeared. Note that the string at that index does
#not need to BE the search string, but rather must just contain it.
#You should assume that the first line in a file is line 1, not line
#0.
#
#For example, if the files contents was:
#cat
#cats
#dog
#dogs
#catsup
#
#Then search_in_files("input_file.txt", "cat") would return
#[1, 2, 5], because "cat" appears on lines 1, 2, and 5.
#
#Make sure the list you return is sorted from lowest line number to
#highest.


#Add your code here!
def search_in_files(filename, search_string):
    file = open(filename, "r")
    lines = []
    for line in file:
        lines.append(line)
    indices = []
    for i in range(len(lines)):
        if search_string in lines[i]:
            indices.append(i+1)
    return indices


#The code below will test your function. You can find the file it
#references in the drop-down in the top left. If your code works,
#this should print:
#[1, 2, 5]
#[3, 4]
#[2, 5]
#[5]
#[]
print(search_in_files("input_file.txt", "cat"))
print(search_in_files("input_file.txt", "dog"))
print(search_in_files("input_file.txt", "cats"))
print(search_in_files("input_file.txt", "sup"))
print(search_in_files("input_file.txt", "aardvark"))
