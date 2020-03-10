# https://www.youtube.com/watch?v=2KuGYl76Ul4&list=PL7_9joZ9PjilgeB6wk9ECEIvLAq6c_bBB&index=4&t=0s
# Coding interview with a Google engineer: Delete nodes from tree
# We want to delete certain nodes from a binary tree. We have a function shouldDelete(Node) that returns True 
# if we should delete the node. we can assume this function is alreayd present

# write a function deleteNodes(root), that takes a binary tree which removes the nodes that should be delete from 
# the tree and reuturns a list of tree forest

class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
		
	def setLeft(self,node):
		self.left = node
		
	def setRight(self,node):
		self.right = node
		
	

def pot(root):
	if root.left is not None:
		pot(root.left)
	if root.right is not None:
		pot(root.right)
	print(root.val,end=" ")
		
		

def shouldDelete(node):
	if testcase == 1:
		if node.val == 4 or node.val == 6 or node.val == 1:
			return True
	if testcase == 2:
		if node.val == 4 or node.val == 6:
			return True
	if testcase == 3:
		if node.val == 4 or node.val == 7:
			return True
	if testcase == 4:
		if node.val == 1:
			return True
	if testcase == 5:
		if node.val == 2 or node.val == 3:
			return True
	if testcase == 6:
		return True
	if testcase == 7:
		return False
	return False
	
def deleteNodes(root,op):
	
	if root is None:
		return None,op
	
	if root.left is None and root.right is None:
		if shouldDelete(root):
			print("1",op) if debug else None
			return None,op
		else:
			print("2",op) if debug else None
			return root,op
			
	if root.left is not None:
		nl,opl = deleteNodes(root.left,op)
		root.left = nl
		#op += opl
	if root.right is not None:
		nr,opr = deleteNodes(root.right,op)
		root.right = nr
		#op += opr
				
	if shouldDelete(root):
		if root.left is not None:
			op += [root.left.val]
		if root.right is not None:
			op += [root.right.val]
		print("3",op) if debug else None
		return None,op
	else:
		print("4",op) if debug else None
		return root,op
		
		
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2.setLeft(n4)
n2.setRight(n5)
n6.setRight(n7)
n3.setLeft(n6)
n1.setLeft(n2)
n1.setRight(n3)
pot(n1)
print()
debug = False

testcase = 7
op1,op2 = deleteNodes(n1,[])
print("Test case:",testcase)
if op1 is not None:
	print([op1.val] + op2)
else:
	print(op2)
print()


# (base) D:\>python interview.io.6_delete_nodes_tree.py
# 4 5 2 7 6 3 1
# Test case: 1
# [7, 2, 3]


# (base) D:\>python interview.io.6_delete_nodes_tree.py
# 4 5 2 7 6 3 1
# Test case: 2
# [1, 7]


# (base) D:\>python interview.io.6_delete_nodes_tree.py
# 4 5 2 7 6 3 1
# Test case: 3
# [1]


# (base) D:\>python interview.io.6_delete_nodes_tree.py
# 4 5 2 7 6 3 1
# Test case: 4
# [2, 3]


# (base) D:\>python interview.io.6_delete_nodes_tree.py
# 4 5 2 7 6 3 1
# Test case: 5
# [1, 4, 5, 6]


# (base) D:\>python interview.io.6_delete_nodes_tree.py
# 4 5 2 7 6 3 1
# Test case: 6
# []

# (base) D:\>python interview.io.6_delete_nodes_tree.py
# 4 5 2 7 6 3 1
# Test case: 7
# [1]
