#This will be the largest, most authentic program you've
#written so far. It will require everything you've learned
#and should take some time to test and debug. Be patient,
#you can do it!
#
#Write a function called average_word_length that takes as
#input a string called my_string, and returns as output the
#average length of the words in the string.
#
#In writing this function, note the following:
#
# - You should account for consecutive spaces. A string like
#   "Hi   Lucy" is two words with an average length of 3.0
#   characters.
# - You should not assume the string starts with a letter.
#   A string like "  David" has one word with an average
#   length of 5.0 characters.
# - You should not count punctuation marks toward the
#   length of a word. A string like "Hi, Lucy" has two
#   words with an average length of 3.0 characters: the ,
#   after "Hi" does not count as a character in the word.
#   The only punctuation marks you need to handle are
#   these: . , ! ?
# - You may assume the only characters in the string are
#   letters, the punctuation marks listed above, and spaces.
# - If my_string is not a string, you should instead return
#   the string, "Not a string".
# - If there are no words in my_string, you should instead
#   return the string, "No words". This could happen for
#   strings like "" (an empty string) and ".,!?" (a string
#   of only punctuation marks). You may assume that any
#   of these punctuation marks will always be followed by
#   at least one space.
#
#Here are a few hints that might help you:
#
# - You can peak at the first character in my_string with
#   my_string[0]. If my_string is "Hi, Lucy", then the value
#   of my_string[0] is "H". You don't have to do this, but
#   you can if you want.
# - There are lots of ways you can do this. If you're
#   stuck, try taking a step back and thinking about the
#   problem from a fresh perspective.
# - If you're still stuck, try counting words and letters
#   separately, and worrying about average length only
#   after both have been counted.
# - The word count should equal the number of letters that
#   come immediately after a space or the start of the
#   string. The character count should simply equal the
#   number of characters besides spaces and punctuation
#   marks. The average word length should be character
#   count divided by word count.


#Write your function here!

def average_word_length(my_string):
    temp_count = 0
    letter_count = 0
    average = 0
    
    try :
        if my_string[0] == " ":
            word_count = 0
            
            for i in my_string:
                if i == " ":
                    temp_count += 1
                    
                    if temp_count == 1:
                        word_count += 1
                        
                    else:
                        temp_count += 1
                        
                elif i != " ":
                    temp_count = 0
                    
                    if i != "." and i != "," and i != "!" and i != "?":
                        letter_count += 1
                        
            if letter_count == 0:
                return "No words"
            
        else:
            word_count = 1
            
            for i in my_string:
                if i == " ":
                    temp_count += 1
                    
                    if temp_count == 1:
                        word_count += 1
                        
                    else:
                        temp_count += 1
                        
                elif i != " ":
                    temp_count = 0
                    
                    if i != "." and i != "," and i != "!" and i != "?":
                        letter_count += 1
                        
            if letter_count == 0:
                return "No words"
        
        average = letter_count / word_count
        return average
    
    except:
        return "Not a string"


#When your function works, the following code should
#output:
#2.0
#3.0
#4.0
#Not a string
#No words

print(average_word_length("Hi"))
print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))



