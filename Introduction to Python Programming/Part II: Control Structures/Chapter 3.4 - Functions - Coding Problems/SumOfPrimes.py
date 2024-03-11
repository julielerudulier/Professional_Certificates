#Write a function called sum_of_primes. sum_of_primes should
#take as input a single integer, and then it should sum all
#the prime numbers up to and including that integer (if it is
#prime. Note that 1 is not considered a prime number.
#
#For example, sum_of_primes(6) would return 10: 2 + 3 + 5 = 10.
#1, 4 and 6 are not prime; 2, 3, and 5 are.
#
#Other examples include:
#
# sum_of_primes(7)  -> 17 (2 + 3 + 5 + 7 = 17)
# sum_of_primes(8)  -> 17 (2 + 3 + 5 + 7 = 17)
# sum_of_primes(11) -> 28 (2 + 3 + 5 + 7 + 11 = 28)
#
#To help you with this, we have supplied you with a function
#to find if a single number is prime. You do not need to know
#how this program works; only that it works. You may use this
#function, but you do not have to. Here is the function:

def is_prime(n):
    from itertools import count, islice
    return n > 1 and all(n % i for i in islice(count(2), int(n**0.5)-1))

#Add your function here!
def sum_of_primes(n):
    sum = 0
    for i in range(2, n+1):
        if is_prime(i):
            sum += i
    return sum 

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 10, 17, 17, and 28.
print(sum_of_primes(6))
print(sum_of_primes(7))
print(sum_of_primes(8))
print(sum_of_primes(11))

