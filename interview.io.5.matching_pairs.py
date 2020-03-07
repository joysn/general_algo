# https://www.youtube.com/watch?v=wBXZD436JAg
# Python interview with a LinkedIn engineer: Matching pairs
# List of whole positive #s.
# Given a number, find the complement of the number

def find_pair(num_list,target):
	l = len(num_list)
	if l == 0 or l == 1:
		return ("No valid pairs")
		
	my_dict = dict()
	for i in range(l):
		if num_list[i] not in my_dict.keys():
			my_dict[num_list[i]] = 1
		else: # Not needed if there are no duplicates
			my_dict[num_list[i]] += 1
			
	for i in range(l):
		comp_num = target - num_list[i]
		if comp_num == num_list[i]: # Special Case
			if my_dict[num_list[i]] > 1:
				return (num_list[i],comp_num)
		else:
			if comp_num in my_dict.keys():
				return (num_list[i],comp_num)
			
			
	return ("No valid pairs")
	
	
print(find_pair([14,13,6,7,8,10,1,2],3))
print(find_pair([14,13,6,7,8,10,1,2],4))
print(find_pair([14,13,6,7,8,10,1,2],0))
print(find_pair([14],14))
print(find_pair([],0))
	

	