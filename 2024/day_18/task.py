from collections import deque
# part 1
grid = [ [0]*71 for i in range(71)]

with open("input.txt") as file:
	data_lines = file.readlines()
	for i in range(1024):
		[x,y] = map(int,data_lines[i].split(","))
		grid[x][y] = 1

def possiblePath(n, m, grid):
	# Check if the source or destination cell is blocked
	if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
		# Return -1 to indicate no path
		return -1
	
	# Create a queue to store the cells to explore
	q = deque()
	# Add the source cell to the queue and mark its distance as 0
	q.append((0, 0))

	# Define two arrays to represent the four directions of movement
	dx = [-1, 0, 1, 0]
	dy = [0, 1, 0, -1]

	# Create a 2D list to store the distance of each cell from the source
	dis = [[-1 for _ in range(m)] for _ in range(n)]

	# Set the distance of the source cell as 0
	dis[0][0] = 0

	# Loop until the queue is empty or the destination is reached
	while q:
		# Get the front cell from the queue and remove it
		p = q.popleft()

		# Loop through the four directions of movement
		for i in range(4):
			# Calculate the coordinates of the neighboring cell
			x = p[0] + dx[i]
			y = p[1] + dy[i]
			# Check if the neighboring cell is inside the grid and not visited before
			if 0 <= x < n and 0 <= y < m and dis[x][y] == -1:
				# Check if the neighboring cell is free or special
				if grid[x][y] == 0 or grid[x][y] == 2:
					# Set the distance of the neighboring cell as one more than the current cell
					dis[x][y] = dis[p[0]][p[1]] + 1
					# Add the neighboring cell to the queue for further exploration
					q.append((x, y))
				# Check if the neighboring cell is special
				if grid[x][y] == 2:
					# Loop through the four directions of movement again
					for j in range(4):
						# Calculate the coordinates of the adjacent cell
						xx = x + dx[j]
						yy = y + dy[j]
						# Check if the adjacent cell is inside the grid
						if 0 <= xx < n and 0 <= yy < m:
							# Check if the adjacent cell is blocked
							if grid[xx][yy] == 1:
								# Change the adjacent cell to free
								grid[xx][yy] = 0

	# Return the distance of the destination cell from the source
	return dis[n - 1][m - 1]

# Driver code
if __name__ == "__main__":
	n = 71
	m = 71
	result = possiblePath(n, m, grid)
	# Function Call
	print(result)
	# part 2
	for i in range(1024, len(data_lines)):
		[x,y] = map(int,data_lines[i].split(","))
		grid[x][y] = 1
		if possiblePath(n,m,grid) == -1:
			print(f"{x},{y}")
			break
