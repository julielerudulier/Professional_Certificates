A = 50
T = 301
n = 0.5
Ea = 30
R = 0.8268

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#The Arrhenius equation is a formula used in physical
#chemsitry to show temperature dependence on reaction rates.
#A modified form of the equation is showed below:
#
# k = A x T^n x e^(-Ea/(R x T))
#
#Where k is a rate constant, T is the temperature in Kelvin,
#n is some constant, A is the pre-exponential factor, Ea is
#the activation energy, R is the universal gas constant, and
#e is the mathematical constant.
#
#It can also be seen here: 
#https://wikimedia.org/api/rest_v1/media/math/render/svg/178c4170c8a642485243ccc3e816f7ae4056dd51
#
#Below, write some lines of code that replicates this modified
#Arrhenius equation using the variables created above as the
#different factors in the equation, and print out the resulting
#value of k. For the mathematical constant e, we have imported
#e from the math library so you can simply use e to access this
#value (as if it's a variable defined above as well).
#
#You should round the result to two decimal places. To do this,
#you can use Python's built-in round() function. To use it, use
#the following syntax:
#
#rounded_num = round(original_num, 2)
#
#The syntax on the line above will round original_num to 2
#decimal points and assign the result to rounded_num.

#With the current values of these variables, your code should
#output 768.95.

from math import e

#Write your code here!
k = A * (T**n) * e**(-Ea / (R * T))
print(round(k, 2))


