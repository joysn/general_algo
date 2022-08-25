# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-4-largest-palindrome-product

def isPalindrome(num):
    return str(num) == str(num)[::-1]

def maxPalProd(n):

    op = 0
    for i in range(10**n-1,10**(n-1),-1):
        for j in range(i,10**(n-1),-1):
            p = i * j
            if p > op and isPalindrome(p):
                op = p
                break
    return op

if __name__ == "__main__":

    for i in range(1,5):
        print("Max Palindromic prodcut of",i,"digit 2 numbers is",maxPalProd(i))