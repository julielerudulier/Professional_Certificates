my_current_average = 87.1
survey_completers = 50
class_size = 100

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Unlike David Joyner (who believes such bonuses are unethical),
#Prof. Shmavid Shmoyner offers a bonus to students' final
#average based on the percentage of students that complete the
#end-of-course survey.
#
#Prof. Shmoyner's formula is simple: every person that does
#the end-of-course survey adds one point to the "pool" of
#points. These points are then divided evenly among all
#students in the class.
#
#For example, if 50 students do the end-of-course survey,
#then 50 points are divided among the class. If there were
#100 students in the class, then each student gets 0.5 bonus
#points. If there were 50 students in the class, then every
#student would get 1 bonus point.
#
#The variables above describe a particular class. Your
#average is given by my_current_average. survey_completers
#shows how many students completed the survey. class_size
#holds how many students are in the class.
#
#Write some code that will print the following message with
#the appropriate values:
#
#After the 0.5 point bonus, my average is 87.6.
#
#You should round the bonus to the nearest tenth of a point.
#To do this, you can use Python's built-in round() function.
#To use it, use the following syntax:
#
#rounded_num = round(original_num, 1)
#
#The syntax on the line above will round original_num to 1
#decimal point and assign the result to rounded_num.
#
#Hint: You might need to round both the bonus and the final
#grade separately! Python does some odd things with adding
#decimals sometimes, such as thinking 80.1 + 0.1 is 
#80.1999999999999.


#Add your code here!
bonus = round(survey_completers / class_size, 1)
new_average = round(my_current_average + bonus, 1)

print("After the " + str(bonus) + " point bonus, my average is " + str(new_average) + ".")




