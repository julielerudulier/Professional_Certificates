my_gpa = 3.6
my_major = "Computer Science"
my_interest = "Software"
company_gpa_req = 3.5
company_major_recruiting  = "Computer Science"
company_interest = "Software"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#It's career fair season and you are in the middle of applying
#to all of these different companies for a potential internship
#next summer, but you plan on only applying to companies that
#you are interested in and companies whose requirements you meet.
#
#You'll only apply to the company if your GPA either matches or
#is greater than the company's required GPA. Even then you'll
#only apply to them if the major they are recruiting is your
#major. However if you are not the major they are recruiting,
#you'll still apply to them if your interest matches the interest
#the company is advertising.
#
#Write some lines of code using logical operators that will print
#True if you do end up applying to the company or False if you
#don't end up appplying to the company based on the requirements
#described above. Use the variable names as listed in the top of
#the problem description.
#
#If your code is working correctly, with the original values of
#the variables defined above, your code should print out True.

#Add your code below!
print((my_gpa >= company_gpa_req) and (company_major_recruiting == my_major or my_interest == company_interest)) 



