s1 = 95
s2 = 40
s3 = 50
s4 = 100
s5 = 87
s6 = 24
s7 = 8
s8 = 76
s9 = 52
s10 = 84

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you are a professor and trying to determine whether
#you should curve the grades for an exam based on the class 
#average. You are given the exam scores for your class of 10
#students above. Find the class average; if it is less than 70,
#then the exam should be curved.
#
#Once you have determined whether the exam should be curved,
#print the following string: "The exam should be curved: True."
#If the exam should not be curve, use 'False' instead of 'True',
#but either way, make sure to include the period after the
#result.

#Add your code here! With the initial values of the 10 variables
#above, your result should be True.
average = (s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10) / 10
print("The exam should be curved: " +  str(average < 70) + ".")




