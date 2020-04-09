# first non repeating character
	
def firstNonRepeatingChar(s):
	nonRepeating = []
	charDict = dict()
	
	for i in range(len(s)):
		#print(s[i])
		if s[i] not in charDict.keys():
			charDict[s[i]] = 1
			nonRepeating.append(s[i])
		else:
			charDict[s[i]] += 1
			if charDict[s[i]] == 2:
				idx = nonRepeating.index(s[i])
				del nonRepeating[idx]
			
	if len(nonRepeating) == 0:
		return '_'
	#print(nonRepeating)
	return nonRepeating[0]

print("******** O(n^2) ************")
print(firstNonRepeatingChar('aaabcccdeeef')=='b')
print(firstNonRepeatingChar('abcbad')=='c')
print(firstNonRepeatingChar('abcabcabc')=='_')




class Node:
	def __init__(self,key):
		self.key = key
		self.next = None
		self.prev = None
		
def firstNonRepeatingChar(s):
	head = None
	tail = None
	charDict = dict()
	
	for i in range(len(s)):
		#print(s[i])
		if s[i] not in charDict.keys():
			n = Node(s[i])
			charDict[s[i]] = (n,1)
			# add to the list
			if head is None and tail is None:
				head = n
				tail = n
			else:
				tail.next = n
				n.prev = tail
				tail = n
				tail.next = None
		else:
			n,count = charDict[s[i]]
			charDict[s[i]] = (n,count+1)
			if count+1 == 2:
				# Delete from list
				if head == n and tail == n:
					head = None
					tail = None
				elif head == n:
					head = n.next
					if head is not None:
						head.prev = None
				elif tail == n:
					tail = n.prev
					tail.next = None
				else:
					n.prev.next = n.next
					if n.next is not None:
						n.next.prev = n.prev
					n.prev = None
					n.next = None
			
	if head is None:
		return '_'
	return head.key

print("******** O(n) ************")
print(firstNonRepeatingChar('aaabcccdeeef')=='b')
print(firstNonRepeatingChar('abcbad')=='c')
print(firstNonRepeatingChar('abcabcabc')=='_')


# (base) D:\>python algo_first_nonrepeating.py
# ******** O(n^2) ************
# True
# True
# True
# ******** O(n) ************
# True
# True
# True