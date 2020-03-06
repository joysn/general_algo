# https://www.youtube.com/watch?v=nY9tgnWLsTk
# source string -> dest string
# list of allowed intermediate words
# each transformation requires just 1 change (1 difference)
# return if can be transformed

def diffOk(src,dest):
	if len(src) != len(dest):
		return False
		
	if src == dest:
		return True
		
	count = 0
	for i in range(len(src)):
		if src[i] != dest[i]:
			count += 1
			if count > 1:
				return False
	return True

def isTransformable(src,dest, allowedStrs):
	if src == dest:
		return True
		
	if len(src) != len(dest):
		return False
		
	if diffOk(src,dest):
		return True
		
	# transform allowedStrs
	groupedList = [[src],[dest]]
	for idx in range(len(allowedStrs)):
		inserted = 0
		for gl in groupedList:
			for gw in gl:
				if diffOk(gw,allowedStrs[idx]):
					inserted = 1
					gl.append(allowedStrs[idx])
					break
		if inserted == 0:
			groupedList.append([allowedStrs[idx]])
			
	print(groupedList) if debug else None
	for i in range(len(groupedList)):
		for j in range(i+1,len(groupedList)):
			if len(set(groupedList[i]).intersection(set(groupedList[j]))) > 0:
				groupedList[i] = list(set(groupedList[i]).union(set(groupedList[j])))
				groupedList[j] = []
			if (src in groupedList[i]) and (dest in groupedList[i]):
				return True
	
	print(groupedList)
	# for gl in groupedList:
		# if (src in gl) and (dest in gl):
			# return True
			
	return False
	
debug = True
debug = False
allowedWords = ["dot","cat","hot","hog","eat","dug","dig","lot","cot","mut","but","nut","bun","ben"]
print(isTransformable("dog","hat",allowedWords))
allowedWords = ["dot","cat","hot","hog","eat","dug","dig","lot","cot","mut","but","nut","bun","ben"]
print(isTransformable("put","pen",allowedWords))
print(isTransformable("put","pin",allowedWords))

		
		
			
					
	