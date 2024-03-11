#In this problem, your goal is to write a function that can
#either count all the vowels in a string or all the consonants
#in a string.
#
#Call this function count_letters. It should have two
#parameters: the string in which to search, and a boolean
#called find_consonants. If find_consonants is True, then the
#function should count consonants. If it's False, then it
#should instead count vowels.
#
#Return the number of vowels or consonants in the string
#depending on the value of find_consonants. Do not count
#any characters that are neither vowels nor consonants (e.g.
#punctuation, spaces, numbers).
#
#You may assume the string will be all lower-case letters
#(no capital letters).


#Add your code here!
def count_letters(string, find_consonants):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    
    if find_consonants:
        for i in string:
            if i not in vowels and i != " ":
                count += 1
        
    if not find_consonants:
        count = 0
        for i in string:
            if i in vowels and i != " ":
                count += 1
    
    return count

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 14, then 7.

a_string = "up with the white and gold"

print(count_letters(a_string, True))
#print(count_letters(a_string, False))




