# https://www.youtube.com/watch?v=TKzLFB7Peaw
# Python interview with a Facebook engineer: Palindrome one character removed

def isPalindrome(string,length):

    start = 0
    end = length-1
    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True



def isPalindromeRemovingOneChar(string):

    if not string:
        return True

    if len(string) <= 2:
        return True

    if isPalindrome(string,len(string)):
        return True

    i = 0
    j = len(string)-1

    while i <= j and string[i] == string[j]:
        i += 1
        j -= 1
    # i == j or unmatched characters
    if i == j: # Odd sized
        return True
    if i > j: # Even sized
        return True
    
    if isPalindrome(string[i:j],j-i): # remove jth char
        return True
    if isPalindrome(string[i+1:j+1],j-i): # remove ith char
        return True
    
    return False    


if __name__ == "__main__":
    print(isPalindromeRemovingOneChar("abcd"))
    print(isPalindromeRemovingOneChar("tacocats"))
    print(isPalindromeRemovingOneChar("racercar"))

    # print(isPalindrome("aba"))
    # print(isPalindrome("abba"))
    # print(isPalindrome("bcd"))
    # print(isPalindrome("tacocat"))
    # print(isPalindrome("racecar"))

