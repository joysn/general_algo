# https://www.youtube.com/watch?v=ahIpip2DQ70&list=PL7_9joZ9PjilgeB6wk9ECEIvLAq6c_bBB&index=9
# Find k closest points based on distance from vertex to the given list of points
# Since we are dealing with minheap and we need points with min distance in heap, we change the __lt__ function to be like __gt__
# Or use * -1 with the distance to make it into a maxheap

from heapq import heappop, heappush, heappushpop
import math

class Point:
	def __init__(self,x,y,dist):
		self.x = x
		self.y = y
		self.dist = dist
		
	def __lt__(self,other):
		return self.dist >= other.dist
		
	def __repr__(self):
		return str([self.x,self.y,round(self.dist,2)])
		
		
		
def distance(p1,p2):
	squares = [(a-b)**2 for a, b in zip(p1,p2)]
	squared_sum = sum(squares)
	#return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]))
	return math.sqrt(squared_sum)
	
		
def find_k_closest(points,vertex,k):

	if k < 0:
		raise ValueError("Value of k must be greater than 0")
	
	no_of_points = len(points)
	
	closest_points = []
	for i in range(no_of_points):
		point = Point(points[i][0],points[i][1],distance(points[i],vertex))
		
		if len(closest_points) < k:
			heappush(closest_points,point)
		else:
			heappushpop(closest_points,point)
			
	op = []
	for i in range(len(closest_points)):
		op.append(heappop(closest_points))
		
	return op
	
	
points = [[1,2],[2,3],[1,-3]]
a = list((p,i) for p,i in enumerate(points))
print(a)

points = [[1,2],[2,3],[1,-3]]
vertex = [2,2]
k = 2
print("Among all Points:",points," ",k," Closest points to:",vertex,"are:",find_k_closest(points,vertex,k))
points = [[1,2],[2,3],[1,-3],[100,200]]
print("Among all Points:",points," ",k," Closest points to:",vertex,"are:",find_k_closest(points,vertex,k))
points = [[1,2],[2,3],[1,-3],[100,200],[1.5,1.5]]
print("Among all Points:",points," ",k," Closest points to:",vertex,"are:",find_k_closest(points,vertex,k))
points = [[1,2],[2,3],[1,-3],[100,200],[1.5,1.5],[1.5,1.5]]
print("Among all Points:",points," ",k," Closest points to:",vertex,"are:",find_k_closest(points,vertex,k))
k = -1
print("Among all Points:",points," ",k," Closest points to:",vertex,"are:",find_k_closest(points,vertex,k))