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

#This line will open the file:
#record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    
def all_time_record(opponent):
    file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    
    lines = []
    for line in file:
        lines.append(line.split(","))
        
    teams = {}
    answer = ""
    points = 0
    
    for i in range(1, len(lines)):
        if lines[i][1] not in teams:
            teams[lines[i][1]] = int(lines[i][3]) - int(lines[i][4])
        elif lines[i][1] in teams:
            teams[lines[i][1]] += (int(lines[i][3]) - int(lines[i][4]))
     
    for (key, value) in teams.items():
        if value > points :
            points = value
            answer = key
            
    return answer
    

#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.

print(all_time_record("1955"))
