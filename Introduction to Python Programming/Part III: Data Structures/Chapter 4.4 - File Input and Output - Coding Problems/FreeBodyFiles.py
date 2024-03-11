#Recall Coding Problem 4.3.9 (Advanced), the free body
#diagram problem. If you were unable to solve that, we've
#included the sample answer in the dropdown in the top left
#-- feel free to use that to write your answer to this
#problem.
#
#Revise your code from that problem to use a file instead of
#a list as its parameter. Name this new function
#find_net_force_from_file. The function should take one
#parameter, the name of a file. The function should return
#the net magnitude and direction, just as it did in the other
#problem.
#
#Each line of the file will have two numbers, both integers:
#the first number will be the magnitude, and the second
#number will be the angle (in degrees, from -180 to 180).
#There will be a space between them.
#
#HINT: You may have multiple functions in your code if you
#want!
#
#HINT 2: Try to write this such that you can reuse as much
#of your earlier code as possible. Remember, when loading
#from a file, any text you load is initially a string. You'll
#almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#Add your function here!
def find_net_force_from_file(filename):
    file = open(filename, "r")
    lines = []
    for line in file:
        line = line.split()
        lines.append(line)   
    sum_HC = 0
    sum_VC = 0
    for i in range(len(lines)):
        sum_HC += int(lines[i][0]) * cos(radians(int(lines[i][1])))
        sum_VC += int(lines[i][0]) * sin(radians(int(lines[i][1])))
    file.close()
    return (round(sqrt(sum_HC ** 2 + sum_VC ** 2), 1), 
            round(degrees(atan2(sum_VC, sum_HC)), 1))
    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))

