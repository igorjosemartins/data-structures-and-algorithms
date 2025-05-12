from collections import deque

# BFS
def numIslands(grid):
  if not grid:
    return 0

  rows = len(grid)
  columns = len(grid[0])
  
  visited = set()
  islands = 0
  
  def bfs(row, column):
    q = deque()
    q.append((row, column))
    
    # [1,0] => baixo   | [-1,0] => cima
    # [0,1] => direita | [0,-1] => esquerda
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while q:
      curr_row, curr_col = q.popleft()

      for d_row, d_col in directions:
        total_row = curr_row + d_row
        total_col = curr_col + d_col

        if total_row in range(rows) and total_col in range(columns) and grid[total_row][total_col] == "1" and (total_row, total_col) not in visited:
          q.append((total_row, total_col))
          visited.add((total_row, total_col))
  
  for r in range(rows):
    for c in range(columns):
      if grid[r][c] == "1" and (r, c) not in visited:
        bfs(r, c)
        islands += 1

  return islands

# DFS
def numIslands2(grid):
  if not grid:
    return 0
  
  rows, cols = len(grid), len(grid[0])
  visited = set()
  islands = 0
  
  def dfs(r,c):
    # validação out of bounds + se já é uma posição visitada + se é '0'
    if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c] == '0':
      return
    
    visited.add((r,c))
    
    # checa recursivamente para as posições adjacentes:
    # cima
    dfs(r - 1, c)
    # baixo
    dfs(r + 1, c)
    # direita
    dfs(r, c + 1)
    # esquerda
    dfs(r, c - 1)
  
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == '1' and (r,c) not in visited:
        dfs(r,c)
        islands += 1
  
  return islands