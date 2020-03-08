# https://www.youtube.com/watch?v=2KuGYl76Ul4&list=PL7_9joZ9PjilgeB6wk9ECEIvLAq6c_bBB&index=4&t=0s
# Coding interview with a Google engineer: Delete nodes from tree

# Given a 2d grid of 1s (land) and 0s (water) , count the number of isalnd
# An isalnd is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You assume all four edges of the grid are all surrounded by water

# Example
# 11000
# 11000
# 00100
# 00011

# Output = 3

def count_island(land_water_grid):
	
	print("Debugging") if debug else None
	if land_water_grid is None:
		return "No Island"
	island_count = 0
	
	rows = len(land_water_grid)
	cols = len(land_water_grid[0])
	
	if rows == 1 and cols == 1:
		return land_water_grid[0][0]
		
	if land_water_grid[0][0] == 1:
		island_count += 1
	print(island_count) if debug else None
	
	if land_water_grid[rows-1][cols-1] == 1:
		if rows > 1 and cols > 1:
			if land_water_grid[rows-1-1][cols-1] == 0 and land_water_grid[rows-1][cols-1-1] == 0:
				island_count += 1
		elif rows > 1:
			if land_water_grid[rows-1-1][cols-1] == 0:
				island_count += 1
		elif cols > 1:
			if land_water_grid[rows-1][cols-1-1] == 0:
				island_count += 1
	print(island_count) if debug else None
	
	for c in range(1,cols-1):
		if land_water_grid[0][c] == 1:
			if land_water_grid[0][c-1] == 0:
				island_count += 1
		if rows > 1:
			if land_water_grid[rows-1][c] == 1:
				if land_water_grid[rows-1][c-1] == 0:
					island_count += 1
	print(island_count) if debug else None
	
	for r in range(1,rows-1):
		if land_water_grid[r][0] == 1:
			if land_water_grid[r-1][0] == 0:
				island_count += 1
		if cols > 1:
			if land_water_grid[r][cols-1] == 1:
				if land_water_grid[r-1][cols-1] == 0:
					island_count += 1
	print(island_count) if debug else None
	
	for r in range(1,rows-1):
		for c in range(1,cols-1):
			if land_water_grid[r][c] == 1:
				if land_water_grid[r-1][c] == 0 and land_water_grid[r][c-1] == 0 and land_water_grid[r+1][c] == 0 and land_water_grid[r][c+1] == 0:
					island_count += 1
		
	print(island_count) if debug else None
	return island_count
	
debug = False
grid = [[1,1,0,0,0]\
        ,[1,1,0,0,0]\
		,[0,0,1,0,0]\
		,[0,0,0,1,1]]
		
print(count_island(grid) == 3)
print(count_island([[1,1,0,0,0]]) == 1)
print(count_island([[0]]) == 0)
print(count_island([[1]]) == 1)
print(count_island([[1],[0]]) == 1)
print(count_island([[1],[0],[1]]) == 2)
print(count_island([[0,0,0,0,0]]) == 0)
print(count_island([[1,0,0,0,0]]) == 1)
print(count_island([[0,0,0,0,1]]) == 1)
print(count_island([[0,0,1,0,0]]) == 1)



# (base) D:\>python interview.io.6_count_island.py
# True
# True
# True
# True
# True
# True
# True
# True
# True
# True