import copy

n, m = map(int, input().split())

graph = []
temp = [[0]*m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx, ny)

def dfs(count):

    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
        

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(count+1)
                graph[i][j] = 0
    

dfs(0)
print(result)
