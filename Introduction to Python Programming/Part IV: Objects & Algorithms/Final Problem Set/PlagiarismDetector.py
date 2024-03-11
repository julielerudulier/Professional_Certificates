#A common problem in academic settings is plagiarism
#detection. Fortunately, software can make this pretty easy!
#
#In this problem, you'll be given two files with text in
#them. Write a function called check_plagiarism with two
#parameters, each representing a filename. The function
#should find if there are any instances of 5 or more
#consecutive words appearing in both files. If there are,
#return the longest such string of words (in terms of number
#of words, not length of the string). If there are not,
#return the boolean False.
#
#For simplicity, the files will be lower-case text and spaces
#only: there will be no punctuation, upper-case text, or
#line breaks.
#
#We've given you three files to experiment with. file_1.txt
#and file_2.txt share a series of 5 words: we would expect
#check_plagiarism("file_1.txt", "file_2.txt") to return the
#string "if i go crazy then". file_1.txt and file_3.txt
#share two series of 5 words, and one series of 11 words:
#we would expect check_plagiarism("file_1.txt", "file_3.txt")
#to return the string "i left my body lying somewhere in the
#sands of time". file_2.txt and file_3.txt do not share any
#text, so we would expect check_plagiarism("file_2.txt",
#"file_3.txt") to return the boolean False.
#
#Be careful: there are a lot of ways to do this problem, but
#some would be massively time- or memory-intensive. If you
#get a MemoryError, it means that your solution requires
#storing too much in memory for the code to ever run to
#completion. If you get a message that says "KILLED", it
#means your solution takes too long to run.


#Add your code here!
def check_plagiarism(filename1, filename2):
    f1 = open(filename1, 'r')
    f2 = open(filename2, 'r')
    
    f1_data = f1.read().split(' ')
    f2_data = f2.read().split(' ')
    
    result = []

    for i in range(len(f1_data)):
        for j in range(len(f2_data)):
            words_in_common = []

            if f1_data[i] == f2_data[j]:
                currI_index = i
                currJ_index = j
                
                while f1_data[currI_index] == f2_data[currJ_index]:
                    words_in_common.append(f1_data[currI_index])
                    
                    if currI_index < len(f1_data) - 1 and currJ_index < len(f2_data) - 1:
                        currI_index += 1
                        currJ_index += 1
                        
                    else:
                        break
                        
            if len(words_in_common) > len(result):
                result = words_in_common
    
    if len(result) >= 5:
        return ' '.join(result)
    
    else:
        return False
    
        

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#if i go crazy then
#i left my body lying somewhere in the sands of time
#False
#print(check_plagiarism("file_1.txt", "file_2.txt"))
print(check_plagiarism("file_1.txt", "file_3.txt"))
#print(check_plagiarism("file_2.txt", "file_3.txt"))
