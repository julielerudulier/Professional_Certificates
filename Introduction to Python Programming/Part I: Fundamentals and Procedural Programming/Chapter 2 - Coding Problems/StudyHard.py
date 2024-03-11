test_percent = 20
review_time = 2
feel_prepared = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#You've been studying for your test for a few hours and you're
#trying to decide if you can go to bed or if you need to study
#longer.
#
#To go to bed, you need to feel prepared. Even if you "feel"
#prepared, you need to make sure you have prepared adequately:
#that means reviewing for at least 2 hours (review_time), or
#at least 4 hours if the test is worth 20 percent or more of
#your grade.
#
#So, to go to bed, you must feel prepared (feel_prepared must
#be True), and you must have reviewed for 2 or more hours
#(review_time must be greater than or equal to 2). If the
#test is worth 20% or more (test_percent is greater than
#or equal to 20), you should have reviewed for 4 or more hours
#(review_time greater than or equal to 4).
#
#Add your code below! It should print True if you can go to
#bed, False if you cannot.
print(feel_prepared == True and ((review_time >= 2 and test_percent < 20) or (test_percent >= 20 and review_time >= 4)))





