#In the previous problem, you were given a list of integers
#representing the amount of rainfall on each of multiple
#days. Somewhere in the list was the number -1. You were
#asked to find the average of the numbers prior to the -1.
#
#Geometric mean is a different measurement of central
#tendency used in math and statistics. With a regular mean,
#you sum the numbers, then divide the sum by how many
#values there were. With a geometric mean, you multiply the
#numbers, and then you take the nth root of the product,
#where n is the number of values.
#
#For example, if the five values were 1, 2, 3, 4, 5, then
#you would first multiply the values:
# 
# 1 x 2 x 3 x 4 x 5 = 120
#
#...and then take the 5th root because there are 5 numbers.
#The simplest way to take the 5th root is to raise the
#number to the 1/5 power:
#
# (120) ** (1/5) = 2.6

#Write a function called geometric_rainfall.
#geometric_rainfall should have one parameter, a list of
#integers. geometric_rainfall should calculate the
#geometric mean of all values in the list _before_ the
#first -1.
#
#For example:
#
#geometric_rainfall([1, 2, 3, 4, 5, -1, 6, 7]) -> 2.6
#
#The function would find the geometric mean of 1, 2, 3,
#4, and 5, and ignore any values after the -1.
#
#You may assume all the items in the list are integers,
#that -1 is guaranteed to occur somewhere in the list,
#and that -1 will not be the first item in the list.


#Add your code here!

def geometric_rainfall(integers):
    count = 0
    product = 1
    for i in range(len(integers)):
        if integers[i] != -1:
            product *= integers[i]
            count += 1
        else:
            break
    return product ** (1/count)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3.0
a_list = [1, 2, 3, 4, 5, -1, 6, 7]
print(geometric_rainfall(a_list))
