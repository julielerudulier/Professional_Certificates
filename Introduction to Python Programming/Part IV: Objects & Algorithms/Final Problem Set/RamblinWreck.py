#Last problem, you wrote a function that generated the all-
#time win-loss-tie record for Georgia Tech against any other
#team.
#
#That dataset had a lot of other information in it. Let's
#use it to answer some more questions. As a reminder, the
#data will be a CSV file, meaning that each line will be a
#comma-separated list of values. Each line will describe one
#game.
#
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent

This line will open the file:
record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    
# Answer to question 1: Auburn
# Answer to question 2: 1327
# Answer to question 3: 1143
# Answer to question 4: 513-226-27
# Answer to question 5: 11-3-0
# Answer to question 6: 302-177-10
# Answer to question 7: 206-110-12
# Answer to question 8: Duke
# Answer to question 9: Carnegie Tech
# Answer to question 10: 11
# Answer to question 11: Tulane
# Answer to question 12: Furman

#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.

print(all_time_record("1955"))
