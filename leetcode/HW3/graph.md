# HW3/GRAPH

+ [Course Schedule II](#course-schedule-ii)
+ [Course Schedule](#course-schedule)
+ [Number of Islands](#number-of-islands)
+ [Is Graph Bipartite?](#is-graph-bipartite)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)
<!---->
## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
v_set = defaultdict(list)
for b, e in prerequisites:
    v_set[b].append(e)
is_possible = True
v_color = {v: Solution.WHITE for v in range(numCourses)}
top_sort = []
def DFS(node):
    nonlocal is_possible
    v_color[node] = Solution.GRAY
    if node in v_set:
        for nbr in v_set[node]:
            if v_color[nbr] == Solution.WHITE:
                DFS(nbr)
            elif v_color[nbr] == Solution.GRAY:
                is_possible = False
    v_color[node] = Solution.BLACK
    top_sort.append(node)
for comp in range(numCourses):
    if v_color[comp] == Solution.WHITE:
        DFS(comp)
return top_sort if is_possible else []

```

## Course Schedule

https://leetcode.com/problems/course-schedule/

```python
v_set = defaultdict(list)
for b, e in prerequisites:
    v_set[b].append(e)
is_possible = True
v_color = {v: Solution.WHITE for v in range(numCourses)}
top_sort = []
def DFS(node):
    nonlocal is_possible
    v_color[node] = Solution.GRAY
    if node in v_set:
        for nbr in v_set[node]:
            if v_color[nbr] == Solution.WHITE:
                DFS(nbr)
            elif v_color[nbr] == Solution.GRAY:
                is_possible = False
    v_color[node] = Solution.BLACK
    top_sort.append(node)
for comp in range(numCourses):
    if v_color[comp] == Solution.WHITE:
        DFS(comp)
return is_possible
```

## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
# вход: матрица m x n
# выход: кол-во островов
# проход BFS по всем клеткам матрицы (кроме посещенных)
visited = set()
q = deque()
islands = 0
rows, cols = len(grid), len(grid[0])
def BFS(row, col):
    direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited.add((row, col))
    q.append((row, col))
    while q:
        new_r, new_c = q.popleft()
        # проверка соседних клеток
        for dr, dc in direct:
            curr_r = new_r + dr
            curr_c = new_c + dc
            if (curr_r in range(rows) and
                    curr_c in range(cols) and
                    grid[curr_r][curr_c] == "1" and
                    (curr_r, curr_c) not in visited):
                visited.add((curr_r, curr_c))
                q.append((curr_r, curr_c))
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "1" and (r, c) not in visited:
            BFS(r, c)
            islands += 1
return islands
```

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

```python
# репрезентация графа
# закрашиваем белым
# DFS - разбиение на два класса
# конфликт при окрашивании - return False
visited = set()
d = len(graph)
v_color = {v: Solution.NC for v in range(d)}
is_possible = True
def validcolor(node, curr_c, next_c):
    if v_color[node] != Solution.NC:
        return v_color[node] == next_c
    v_color[node] = next_c
    for nbr in graph[node]:
        if not validcolor(nbr, curr_c, -next_c):
            return False
    return True
# проверка каждой вершины на принадлежность классу
for v in range(d):
    if (v_color[v] == Solution.NC and not validcolor(v, Solution.C1, Solution.C2)):
        return False
return True
```

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
k = k + 2 #доступные ребра
prices = [[1e9]*n for _ in range(k)]
prices[0][src] = 0
for i in range(1,k):
    for j in range(n):
        prices[i][j] = prices[i-1][j]
    for b, e, c in flights:
        prices[i][e] = min(prices[i][e], prices[i-1][b] + c)
if prices[k-1][dst] == 1e9:
    return -1
else:
    return prices[k-1][dst]
```

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
n = len(grid)
if grid[0][0] != 0 or grid[n - 1][n - 1] != 0 or grid is None:
    return -1
if len(grid) == 1 and len(grid[0]) == 1 and grid[0][0] == 0:
    return 1
if len(grid) == 1 and len(grid[0]) == 1 and grid[0][0] == 1:
    return -1
q = deque()
start = (0, 0)
q.append(start)
grid[0][0] = 1
directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
while len(q) != 0:
    x, y = q.popleft()
    distance = grid[x][y]
    for dx, dy in directions:
        xnew = x + dx
        ynew = y + dy
        if 0 <= xnew < n and 0 <= ynew < n and grid[xnew][ynew] == 0:
            q.append((xnew, ynew))
            grid[xnew][ynew] = distance + 1
        if xnew == n - 1 and ynew == n - 1:
            return grid[n - 1][n - 1]
return -1
```

## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
if root is None:
    return 0
if len(root.children) == 0:
    return 1
s = 0
for c in root.children:
    d = self.maxDepth(c)
    if d + 1 > s:
        s = d + 1
return s
```

