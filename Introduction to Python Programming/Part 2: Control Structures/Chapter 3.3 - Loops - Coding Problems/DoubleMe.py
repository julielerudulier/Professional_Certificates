a_num = 8

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Take the value of a_num and repeatedly double it until the
#result has at least 7 digits. Then, print the first 7-or-more
#digit number that results from this repeated doubling.
#
#For example, for a_num = 8:
#
#8 -> 16 -> 32 -> 64 -> 128 -> 256 -> 512 -> 1024 -> 2048 -> 
#4096 -> 8192 -> 16384 -> 32768 -> 65536 -> 131072 -> 262144 -> 
#524288 -> 1048576
#
#So, you'd print 1048576.
#
#Hint: to check the number of digits, convert the product to a
#string, then use the len() function to check the string's length.


#Add your code here!

while len(str(a_num)) < 7:
    a_num *= 2
    
print(a_num)
