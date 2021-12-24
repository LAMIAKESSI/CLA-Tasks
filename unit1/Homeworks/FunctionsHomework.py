# 1 A function that checks whether a passed string is palindrome or not
def isPalindrome(str) :
    isPalindrome = True
    for i in range(0,int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            isPalindrome = False
        
    return isPalindrome


# 2 A function that checks if a given number is prime or not 
def isPrime(nbr):
    isPrime = True
    if (nbr == 0):
        isPrime = False
        print(" 0 is neither prime nor composite")
    elif (nbr == 1):
        isPrime = False
        print(" 1 is neither prime nor composite")
    else:
        for i in range(2,int(nbr)):
            if nbr % i == 0:
                isPrime = False
                break
    return isPrime

# 3 A function that checks if nb is in given range
def inRange(nbr, start, end):
    return nbr in range(int(start),int(end))

# 4 A function that calculate the factorial of a number
def facto(nbr):
    factorial = 1
    if nbr == 0 :
        factorial = 1
    else: 
        for i in range(1, nbr+1):
            factorial = factorial*i
    return factorial
   
# 5 A function program to reverse a string. 
def reverse(str):
   return str[::-1]

# 6 A function to sum all the numbers in a list
def sum(list):
    sum = 0
    for i in list:
        sum +=i 
    return sum

# 7 A function that finds the Max of three numbers.
def maximum(nb1, nb2, nb3):
    list = [nb1,nb2,nb3]
    return max(list)
    
