#Write a function called average_file. average_file should
#have one parameter: a filename.
#
#The file should have an integer on each line. average_file
#should return the average of these integers. However, if
#any of the lines of the file are _not_ integers,
#average_file should return the string "Error reading file!"
#
#Remember, by default, every time you read a line from a
#file, it's interpreted as a string.


#Add your function here!
def average_file(filename):
    file = open(filename, "r")
    lines = file.readlines()
    count = 0
    summation = 0
    lists = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if ord(lines[i][j]) > 57:
                file.close()
                return "Error reading file!"
        summation += int(lines[i])
        count += 1
    return (summation * 1.0) / count
    
                   


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5.0, then Error reading file!
#
#You can select valid_file.txt and invalid_file.txt from
#the dropdown in the top left to preview their contents.
print(average_file("valid_file.txt"))
print(average_file("invalid_file.txt"))
