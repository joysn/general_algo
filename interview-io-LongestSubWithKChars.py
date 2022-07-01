# https://www.youtube.com/watch?v=XMcVV9G8F-s
# Given a string, find the length of the longest substring in it with no more than k characters
# string = araaci
# k = 2
# output = 4


def longestSub():
    n = len(s)
    
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = 1

    maxSubStr = ''
    maxSubStrLen = 0
    for i in range(n):
        count_dict = dict()
        for j in range(i,n):
            if i == j:
                dp[i][j] = 1
                count_dict[s[j]] = 1
            elif s[j] not in count_dict.keys():
                count_dict[s[j]] = 1
                dp[i][j] = dp[i][j-1]+1
            else:
                count_dict[s[j]] += 1
                dp[i][j] = dp[i][j-1]
            if dp[i][j] <= k:
                if maxSubStrLen < len(s[i:j+1]):
                    maxSubStrLen = j-i+1
                    maxSubStr = s[i:j+1]
                # maxSubStr = max(maxSubStr,j-i+1)
                # print(i,j,maxSubStr)
            
    # for e in dp:
    #     print(e)
    
    return maxSubStrLen,maxSubStr

def longestSub1():
    n = len(s)
    
    dp = [0 for _ in range(n)]

    maxSubStr = ''
    maxSubStrLen = 0
    for i in range(n):
        count_dict = dict()
        for j in range(i,n):
            if i == j:
                dp[j] = 1
                count_dict[s[j]] = 1
            elif s[j] not in count_dict.keys():
                count_dict[s[j]] = 1
                dp[j] = dp[j-1]+1
            else:
                count_dict[s[j]] += 1
                dp[j] = dp[j-1]
            if dp[j] <= k:
                if maxSubStrLen < len(s[i:j+1]):
                    maxSubStrLen = j-i+1
                    maxSubStr = s[i:j+1]
                # print(i,j,maxSubStr)
            
    # for e in dp:
    #     print(e)
    
    return maxSubStrLen,maxSubStr


if __name__=="__main__":
    s = "araaci"
    for k in range(len(s)):
        print("String",s,"k",k,"Longest Sub",longestSub())
        print("String",s,"k",k,"Longest Sub",longestSub1())

    s = "cbbebi"
    k = 3
    print("String",s,"k",k,"Longest Sub",longestSub())
    print("String",s,"k",k,"Longest Sub",longestSub1())
