# https://www.youtube.com/watch?v=L9Me2tDDgY8
# Given an array of strings, group the anagrams together
# strs = ["eat","tea","tan","ate", "nat","bat"]
# op = [["bat"], ["nat", "tan"], ["ate","eat","tea"]]


def sortAnagrams():

    op_dict = dict()
    for str in strs: #n
        str_freq = dict()
        for ch in str: #m
            if ch not in str_freq.keys():
                str_freq[ch] = 1
            else:
                str_freq[ch] += 1
        s_arr = tuple(sorted(str_freq.items())) #mlogm
        if s_arr not in op_dict.keys():
            op_dict[s_arr] = [str]
        else:
            op_dict[s_arr].append(str)
    
    op = []
    for k in op_dict.keys():
        op.append(op_dict[k])
    return op


def sortAnagrams1():

    anagram_dict = dict()
    for str in strs: #n
        sstr = "".join(sorted(str)) #mlogm
        # print(sstr)
        if sstr not in anagram_dict.keys():
            anagram_dict[sstr] = [str]
        else:
            anagram_dict[sstr].append(str)
    
    op = []
    for k in anagram_dict.keys():
        op.append(anagram_dict[k])
    return op

    

if __name__=="__main__":
    strs = ["eat","tea","tan","ate", "nat","bat"]
    print(sortAnagrams())
    print(sortAnagrams1())