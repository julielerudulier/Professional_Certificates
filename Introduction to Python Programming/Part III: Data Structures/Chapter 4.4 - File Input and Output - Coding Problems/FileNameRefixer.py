#You've been sent a list of names. Unfortunately, the names
#come in two different formats:
#
#First Middle Last
#Last, First Middle
#
#You want the entire list to be the same. For this problem,
#we'll say you want the entire list to be Last, First Middle.
#
#Write a function called name_refixer. name_refixer should have two
#parameters: an output filename (the first parameter) and the
#input filename (the second parameter). You may assume that every
#line will match one of the two formats above: either First Middle
#Last or Last, First Middle. 
#
#name_refixer should write to the output file the names all
#structured as Last, First Middle. If the name was already structured
#as Last, First Middle, it should remain unchanged. If it was
#structured as First Middle Last, then Last should be moved
#to the front and a comma should be added after it.
#
#The names should appear in the same order as the original file.
#
#For example, if the input file contained the following lines:
#David Andrew Joyner
#Hart, Melissa Joan
#Cyrus, Billy Ray
#
#...then the output file should contain these lines:
#Joyner, David Andrew
#Hart, Melissa Joan
#Cyrus, Billy Ray


#Add your code here!
def NFL(a_list):
    for i in range(len(a_list)):
        if ',' not in a_list[i]:
            splits = a_list[i].split()
            a_list[i] = splits[2] + ", " + splits[0] + " " + splits[1]
        
    return a_list

def name_refixer(output_file, input_file):
    in_file = open(input_file, "r")
    out_file = open(output_file, "w")
    
    new_names = []
    for line in in_file:
        new_names.append(line.strip())
        
    new_list = NFL(new_names)
    for name in new_list:
        print(name, file = out_file)
    
    in_file.close()
    out_file.close()
    return 


#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, output_file.txt should have the text:
#Joyner, David Andrew
#Hart, Melissa Joan
#Cyrus, Billy Ray
name_refixer("output_file.txt", "input_file.txt")
print("Done running! Check output_file.txt for the result.")

#If you accidentally erase input_file.txt, here's its original
#text to copy back in (remove the pound signs):
#David Andrew Joyner
#Hart, Melissa Joan
#Cyrus, Billy Ray
