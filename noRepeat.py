# https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/no-repeats-please

def permAlone(pos,currStr,remStr):
    # print(pos,currStr)
    global count
    if pos == n:
        count += 1
        # print(currStr)

    # if (pos,currStr,remStr) in memo:
    #     return memo[((pos,currStr,remStr))]
    for idx in range(len(remStr)):
        if pos > 0 and currStr[-1] != remStr[idx]:
            permAlone(pos+1,currStr+remStr[idx],remStr[:idx]+remStr[idx+1:])
        elif pos == 0:
            permAlone(pos+1,currStr+remStr[idx],remStr[:idx]+remStr[idx+1:])

    memo[(pos,currStr,remStr)] = count

if __name__ == "__main__":

    input_str = ["aab","aaa","aabb","abcdefa","abfdefa","zzzzzzzz","a","aaab","aaabb"]

    for str in input_str:
        memo = dict()
        count = 0
        n = len(str)
        permAlone(0,"",str)
        print("Count of",str,"is",count)


# Count of aab is 2
# Count of aaa is 0
# Count of aabb is 8
# Count of abcdefa is 3600
# Count of abfdefa is 2640
# Count of zzzzzzzz is 0
# Count of a is 1
# Count of aaab is 0
# Count of aaabb is 12