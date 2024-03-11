#In this exercise, you won't edit any of your code from the
#Burrito class. Instead, you're just going to write a
#function to use instances of the Burrito class. You don't
#actually have to copy/paste your previous code here if you
#don't want to, although you'll need to if you want to write
#some test code at the bottom.
#
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint: Don't reinvent the wheel. Use the work that you've
#already done. The function can be written in only five
#lines, including the function declaration.
#
#Hint 2: The exercise here is to write a function, not a
#method. That means this function should *not* be part of
#the Burrito class.


#If you'd like to use the test code, paste your previous
#code here.


#Write your new function here.
def total_cost(burritos):
    total_cost = 0.00
    for burrito in burritos:
        total_cost += burrito.get_cost()
    return float(total_cost)    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs. Note that these lines
#will ONLY work if you copy/paste your Burrito, Meat,
#Beans, and Rice classes in.
#
#If your function works correctly, this will originally
#print: 28.0
#burrito_1 = Burrito("tofu", True, "white", "black")
#burrito_2 = Burrito("steak", True, "white", "pinto", extra_meat = True)
#burrito_3 = Burrito("pork", True, "brown", "black", guacamole = True)
#burrito_4 = Burrito("chicken", True, "brown", "pinto", extra_meat = True, guacamole = True)
#burrito_list = [burrito_1, burrito_2, burrito_3, burrito_4]
#print(total_cost(burrito_list))

