# https://www.codechef.com/problems/DIVSUBS

# You are given a multiset of N integers. Please find such a nonempty subset of it that the sum of the subset's elements is divisible by N. Otherwise, state that this subset doesn't exist.
# Input
# The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. 
# The first line of each test consists of a single integer N - the size of the multiset.
# The second line of each test contains N single space separated integers - the multiset's elements.
# Output
# For each test case output:
# -1 if the required subset doesn't exist
# If the required subset exists, output two lines. Output the size of the subset on the first line and output the list of indices of the multiset's element that form the required subset. Of course, any number can be taken in the subset no more than once.
# If there are several such subsets, you can output any.

import copy
def divsub(nums):
    l = len(nums)
    op_list = list()
    for i in range(l):
        sum = nums[i]
        t_op = [i]
        if sum%l == 0:
            op_list.append([i])
        for j in range(i+1,l):
            sum += nums[j]
            t_op.append(j)
            if sum%l == 0:
                # print(sum)
                op_list.append(copy.deepcopy(t_op))
                

    l_ret = len(op_list)
    if l_ret == 0:
        return -1,[]
    return l_ret, op_list


def divsub2(nums):
    l = len(nums)
    cum_sum = [0 for i in range(l)]
    cum_sum[0] = nums[0]
    for idx in range(1,l):
        cum_sum[idx] = cum_sum[idx-1] + nums[idx]
    
    mod_freq = dict()
    for idx in range(l):
        mod = cum_sum[idx]%l
        if mod == 0:
            left = 0
            right = idx
            break
        if mod in mod_freq.keys():
            left = mod_freq[mod]+1
            right = idx
            break
        mod_freq[mod] = idx


    print("Input",nums, l)
    print("Output size",right-left + 1)
    for i in range(left,right+1):
        print("Output elements",nums[i],end=" ")
    print()


print(divsub([4,6,10]))
print(divsub([4,6,10,9]))
print(divsub([4,6,10,9,5]))

print("*************")
divsub2([4,6,10])
divsub2([4,6,10,9])
divsub2([4,6,10,9,5])



# (1, [[1]])
# (3, [[0], [0, 1, 2], [1, 2]])
# (6, [[0, 1], [0, 1, 2], [1, 2, 3], [1, 2, 3, 4], [2], [4]])
# *************
# Input [4, 6, 10] 3
# Output size 1
# Output elements 6 
# Input [4, 6, 10, 9] 4
# Output size 1
# Output elements 4 
# Input [4, 6, 10, 9, 5] 5
# Output size 2
# Output elements 4 Output elements 6 
