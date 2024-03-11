#-----------------------------------------------------------
#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls. The
#list is used to see what names are most common in a given
#year.
#
#We've grabbed that data for any name used more than 25
#times, and provided it to you in a file called
#babynames.csv. The line below will open the file:

file = open('../resource/lib/public/babynames.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has three values, separated by
#commas. The first value is the name; the second value is
#the number of times the name was given in the 2010s (so
#far); and the third value is whether that count
#corresponds to girls or boys. Note that if a name is
#given to both girls and boys, it is listed twice: for
#example, so far in the 2010s, the name Jamie has been
#given to 611 boys and 1545 girls.
#
#Use this dataset to answer the questions below.


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.

lines = []
for line in file:
        lines.append(line.split(","))
     
names = {}
diff = {}
result = "" 

for i in range(len(lines)):
    if lines[i][0] not in names.keys():
        names[lines[i][0]] = {}
        names[lines[i][0]]["gender 1"] = lines[i][2].strip()
        names[lines[i][0]]["total 1"] = int(lines[i][1])
        names[lines[i][0]]["diff"] = 0
        names[lines[i][0]]["count"] = 1
        
    elif lines[i][0] in names.keys():
        names[lines[i][0]]["count"] += 1
        names[lines[i][0]]["diff"] += (int(lines[i][1]) - names[lines[i][0]]["total 1"])

results = {}

for name in names.keys():
    if names[name]["count"] == 2:
        if names[name]["diff"] < 0:
            results[name] = names[name]["diff"] * (-1)
        elif names[name]["diff"] > 0 or names[name]["diff"] == 0:
            results[name] = names[name]["diff"] 
            
max = 100000000
winner = ""

for key, value in results.items():
    if value < max:
        max = value
        winner = key
 
print(winner)
