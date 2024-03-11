#Write a function called average_rainfall. average_rainfall
#should have one parameter, a list of integers. The list
#represents daily rainfall measurements for a certain area.
#
#However, at some point in the list, there will be a -1.
#This indicates that you should stop averaging, and ignore
#any subsequent values.
#
#For example:
#
#average_rainfall([1, 2, 3, 4, 5, -1, 6, 7]) -> 3.0
#
#The function would only average 1, 2, 3, 4, and 5, and
#ignore any values after the -1.
#
#You may assume all the items in the list are integers,
#that -1 is guaranteed to occur somewhere in the list,
#and that -1 will not be the first item in the list.


#Add your code here!
def average_rainfall(digits):
    count = 0
    total = 0
    for i in range(len(digits)):
        if digits[i] != -1:
            total += digits[i]
            count += 1
        else:
            break
    return total / count

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3.0
a_list = [1, 2, 3, 4, 5, -1, 6, 7]
print(average_rainfall(a_list))
