# partition list into 3 compartments <k, =k and >k
# https://www.youtube.com/watch?v=UaI3WeesCoE&list=PL7_9joZ9PjilgeB6wk9ECEIvLAq6c_bBB&index=2&t=0s
# C# interview with a Microsoft engineer: List partition
# 3:00
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
		
class LinkedList:
	def __init__(self,front):
		self.front = front
		self.rear = front
		
	def add(self,node):
		if self.front == None:
			self.front = node
			self.rear = node
		else:
			node.next = self.front
			self.front = node
			
	def remove(self):
		if self.rear == None:
			print("Empty list")
		else:
			prev = self.front
			while prev.next != self.rear:
				prev = prev.next
			temp = self.rear
			self.rear = prev
			self.rear.next = None
			print("Removed ",temp.data)
			
	
	def addNextTo(self,node,pos):
		if  pos is not None:
			if pos == self.rear:
				self.rear = node
			temp = pos.next
			pos.next = node
			node.next = temp
			
			
		
	def removeFrom(self,pos):
		if pos is None or self.front is None:
			print("Not possible")
			return
			
		print("removeFrom:",pos.data) if debug else None
		if pos == self.front:
			self.front = self.front.next
			return
		prev = self.front
		while prev.next != pos:
			prev = prev.next
		prev.next = pos.next
		
	
	def display(self):
		if self.front == None:
			print("Empty List")
		else:
			temp = self.front
			print("[Front]",end="")
			while temp != None:
				print(temp.data,end="->")
				temp = temp.next
			print("[Rear]")
			
	def organize(self,k):
		if self.front == None:
			print("Empty List")
			return
		
		
		less = None
		equal = None
		more = None
		
		temp = self.front
		if temp.data < k:
			less = self.front
			equal = self.front
			more = self.front
		elif temp.data == k:
			equal = self.front
			more = self.front
		else:
			more = self.front
			
		print("After one pass",end="") if debug else None
		self.display() if debug else None
		
		temp = temp.next
		while temp != None:
			temp_next = temp.next
			if temp.data < k:
				print("Less",temp.data) if debug else None
				self.removeFrom(temp)
				if less is None:
					print("Less add",temp.data) if debug else None
					self.add(temp)
					less = self.front
				else:
					print("Less addNextTo",temp.data) if debug else None
					self.addNextTo(temp,less)
					if less is equal:
						equal = equal.next
					if less is more:
						more = more.next
					less = less.next	
			elif temp.data == k:
				print("Equal",temp.data) if debug else None
				self.removeFrom(temp)
				if equal is None:
					print("Equal add",temp.data) if debug else None
					self.add(temp)
					equal = self.front
				else:
					print("Equal addNextTo",temp.data) if debug else None
					self.addNextTo(temp,equal)
					if equal is more:
						more = more.next
					equal = equal.next
			else:
				print("More",temp.data) if debug else None
				self.removeFrom(temp)
				if more is None:
					print("More add",temp.data) if debug else None
					self.add(temp)
					more = self.front
				else:
					print("More addNextTo",temp.data,more.data) if debug else None
					self.addNextTo(temp,more)
					more = more.next
				
			#print("Before",temp.data, " After",temp_next.data)
			temp = temp_next
			print("After one pass",end="") if debug else None
			self.display() if debug else None
			
debug = True
debug = False
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

ll = LinkedList(n1)
ll.add(n5)
ll.add(n2)
ll.add(n4)
ll.add(n3)
ll.removeFrom(ll.front.next)
ll.addNextTo(n4,ll.front)
n6 = Node(6)
ll.addNextTo(n6,ll.rear)
ll.display()

for i in range(6,0,-1):
	print("After organize with value ",i)
	ll.organize(i)
	ll.display()
	
# (base) D:\>python algo_3partition_list.py
# [Front]3->4->2->5->1->6->[Rear]
# After organize with value  6
# [Front]3->4->2->5->1->6->[Rear]
# After organize with value  5
# [Front]3->4->2->1->5->6->[Rear]
# After organize with value  4
# [Front]3->2->1->4->5->6->[Rear]
# After organize with value  3
# [Front]2->1->3->4->5->6->[Rear]
# After organize with value  2
# [Front]1->2->3->4->5->6->[Rear]
# After organize with value  1
# [Front]1->2->3->4->5->6->[Rear]
