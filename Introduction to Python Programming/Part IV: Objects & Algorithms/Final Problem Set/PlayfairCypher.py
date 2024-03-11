#One of the early common methods for encrypting text was the
#Playfair cipher. You can read more about the Playfair cipher
#here: https://en.wikipedia.org/wiki/Playfair_cipher
#
#The Playfair cipher starts with a 5x5 matrix of letters,
#such as this one:
#
# D A V I O
# Y N E R B
# C F G H K
# L M P Q S
# T U W X Z
#
#To fit the 26-letter alphabet into 25 letters, I and J are
#merged into one letter. When decrypting the message, it's
#relatively easy to tell from context whether a letter is
#meant to be an i or a j.
#
#To encrypt a message, we first remove all non-letters and
#convert the entire message to the same case. Then, we break
#the message into pairs. For example, imagine we wanted to
#encrypt the message "PS. Hello, worlds". First, we could
#convert it to PSHELLOWORLDS, and then break it into letter
#pairs: PS HE LL OW OR LD S. If there is an odd number of
#characters, we add X to the end.
#
#Then, for each pair of letters, we locate both letters in
#the cipher square. There are four possible orientations
#for the pair of letters: they could be in different rows
#and columns (the "rectangle" case), they could be in the
#same row but different columns (the "row" case), they could
#be in the same column but different rows (the "column"
#case), or they could be the same letter (the "same" case).
#
#Looking at the message PS HE LL OW OR LD SX:
#
# - PS is the Row case: P and S are in the same row.
# - HE is the Rectangle case: H and E are in different rows
#   and columns of the square.
# - LD is the Column case: L and D are in the same column.
# - LL is the Same case as it's two of the same letter.
#
#For the Same case, we replace the second letter in the pair
#with X, and then proceed as normal. When decrypting, it
#would be easy to see the our result was not intended to be
#PS HELXO WORLDSX, and we would thus assume the X is meant to
#repeat the previous letter, becoming PS HELLO WORLDSX.
#
#What we do for each of the other three cases is different:
#
# - For the Rectangle case, we replace each letter with
#   the letter in the same row, but the other letter's
#   column. For example, we would replace HE with GR:
#   G is in the same row as H but the same column as E,
#   and R is in the same row as E but the same column as
#   H. For another example, CS would become KL: K is in
#   C's row but S's column, and L is in C's column but S's
#   row.
# - For the Row case, we pick the letter to the right of
#   each letter, wrapping around the end of the row if we
#   need to. PS becomes QL: Q is to the right of P, and L
#   is to the right of S if we wrap around the end of the
#   row.
# - For the Column case, we pick the letter below each
#   letter, wrapping around if necessary. LD becomes TY:
#   T is below L and Y is below D.
#
#We would then return the resultant encrypted message.
#
#Decrypting a message is essentially the same process.
#You would use the exact same cipher and process, except
#for the Row and Column cases, you would shift left and up
#instead of right and down.
#
#Write two methods: encrypt and decrypt. encrypt should
#take as input a string, and return an encrypted version
#of it according to the rules above.
#
#To encrypt the string, you would:
#
# - Convert the string to uppercase.
# - Replace all Js with Is.
# - Remove all non-letter characters.
# - Add an X to the end if the length if odd.
# - Break the string into character pairs.
# - Replace the second letter of any same-character
#   pair with X (e.g. LL -> LX).
# - Encrypt it.
#
#decrypt should, in turn, take as input a string and
#return the unencrypted version, just undoing the last
#step. You don't need to worry about Js and Is, duplicate
#letters, or odd numbers of characters in decrypt.
#
#For example:
#
# encrypt("PS. Hello, world") -> "QLGRQTVZIBTYQZ"
# decrypt("QLGRQTVZIBTYQZ") -> "PSHELXOWORLDSX"
#
#HINT: You might find it easier if you implement some
#helper functions, like a find_letter function that
#returns the row and column of a letter in the cipher.
#
#HINT 2: Once you've written encrypt, decrypt should
#be trivial: try to think of how you can modify encrypt
#to serve as decrypt.
#
#To make this easier, we've gone ahead and created the
#cipher as a 2D tuple for you:
CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))

#Add your code here!

def encrypt(string):
    string = string.upper()
    string = string.replace("J", "I")
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
    
    for i in string:
        if i in punc:
            string = string.replace(i, "")
    
    if len(string) % 2 != 0:
        string += "X"
        
    for i in range(0, len(string) - 1, 2):
        if string[i] == string[i + 1]:
            string = string[:i+1] + "X" + string[i+2:]
        
    pairs = []
    
    for i in range(0, len(string) - 1, 2):
        pairs.append([string[i], string[i+1]])
    
    result = ""
    for i in range(len(pairs)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(CIPHER, pairs[i][0])
        ele2_x, ele2_y = search(CIPHER, pairs[i][1])
 
        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(CIPHER, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(CIPHER, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(CIPHER, ele1_x, ele1_y, ele2_x, ele2_y)
 
        cipher = c1 + c2
        result += str(cipher)
        
    return result

 
def search(cipher, element):
    for i in range(5):
        for j in range(5):
            if(cipher[i][j] == element):
                return i, j
 
 
def encrypt_RowRule(cipher, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = cipher[e1r][0]
    else:
        char1 = cipher[e1r][e1c+1]
 
    char2 = ''
    if e2c == 4:
        char2 = cipher[e2r][0]
    else:
        char2 = cipher[e2r][e2c+1]
 
    return char1, char2
 
 
def encrypt_ColumnRule(cipher, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = cipher[0][e1c]
    else:
        char1 = cipher[e1r+1][e1c]
 
    char2 = ''
    if e2r == 4:
        char2 = cipher[0][e2c]
    else:
        char2 = cipher[e2r+1][e2c]
 
    return char1, char2
 
 
def encrypt_RectangleRule(cipher, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = cipher[e1r][e2c]
 
    char2 = ''
    char2 = cipher[e2r][e1c]
 
    return char1, char2


def decrypt(string):
    i = 0
    while i < len(string):
        n = search2(CIPHER, string[i], string[i+1])
        if n[0] == n[2]:
            string = string[:i] + CIPHER[n[0]][modulus5(n[1]-1)] + CIPHER[n[0]][modulus5(n[3]-1)] + string[i+2:]
        elif n[1] == n[3]:
            string = string[:i] + CIPHER[modulus5(n[0]-1)][n[1]] + CIPHER[modulus5(n[2]-1)][n[1]] + string[i+2:]
        else:
            string = string[:i] + CIPHER[n[0]][n[3]] + CIPHER[n[2]][n[1]] + string[i+2:]
        i += 2
 
    return string
   
    
def search2(cipher, char1, char2):
    positions = [0, 0, 0, 0]
 
    if char1 == 'j':
        char1 = 'i'
    elif char2 == 'j':
        char2 = 'i'
 
    for i in range(5):
        for j in range(5):
            if cipher[i][j] == char1:
                positions[0], positions[1] = i, j
            elif cipher[i][j] == char2:
                positions[2], positions[3] = i, j
 
    return positions


def modulus5(n):
    if n < 0:
        n += 5
    return n % 5



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: QLGRQTVZIBTYQZ, then PSHELXOWORLDSX
print(encrypt("PS. Hello, worlds"))
print(decrypt("QLGRQTVZIBTYQZ"))
