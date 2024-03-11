away_team = [1, 0, 0, 0, 0, 0, 0, 0, 1]
home_team = [0, 1, 0, 0, 0, 0, 2, 0]

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#A baseball game consists of 9 innings. In each inning, each
#team can score some number of runs. Whoever scores the most
#runs wins the game. Note that there are reasons why the
#number of innings might differ; extra innings for a tie game,
#fewer innings for a rain-cancelled game, etc. So, you should
#not assume there are exactly 9 full innings.
#
#The two lists above give the runs scored in each inning by
#two teams. If the away team wins, print "Away team wins!"
#If the home team wins, print "Home team wins!" You may assume
#the game will not end in a tie.
#
#Remember, you can use a loop to look at each item in a list
#with this syntax:
#
#for value in the_list:
#
#Inside that loop, the variable 'value' will take on each
#value from the list until it's seen every value. You
#don't need to know anything more about lists to solve this
#problem!
#
#Note that you must use a loop to solve this problem. If you
#use something like the sum() function, your answer will not
#be accepted.


#Add your code here! With the initial values above, it should
#print "Home team wins!"

score_away = 0
score_home = 0

for value in away_team:
    score_away += value
    
for value in home_team:
    score_home += value
  
if score_away > score_home:
    print("Away team wins!")

if score_home > score_away:
    print("Home team wins!")


