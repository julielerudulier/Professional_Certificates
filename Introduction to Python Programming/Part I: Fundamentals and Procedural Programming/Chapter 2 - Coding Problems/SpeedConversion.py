speed_mph = 60

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#In the United States, speeds are typically given in terms of
#miles per hour. In the rest of the world, speeds are
#typically given in kilometers per hour.
#
#To convert miles per hour to kilometers per hour, we
#multiply miles per hour by 1.6 (technically 1.60934, but
#we're going to round anyway, so the extra decimals won't
#matter).
#
#Write some code that will convert the speed given by
#speed_mph to kilometers per hour, then print the
#following message (substituting in the right values):
#
#60 miles per hour equals 96 kilometers per hour.
#
#You should drop off any decimals that result from this
#conversion. Note that this is different from rounding:
#if speed_mph was 53, your answer would be 84 kilometers
#per hour, not 84.8 or 85. (Hint: Converting a float to
#an integer automatically rounds down.)


#Add your code here!
converted_speed = int(speed_mph  * 1.6)
print(speed_mph, "miles per hour equals", converted_speed, "kilometers per hour.")



