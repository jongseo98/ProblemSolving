# 골드1 외판원 순회
# 이해를 못하겠음
n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

INF = int(1e9)
dp = [[INF] * (1 << n) for _ in range(n)] # 비트마스크 형식으로 거리 초기화 - ex) 4라면 0000 ~ 1111 까지 16개

def dfs(x, visited): # (현재 방문 도시, 방문했던 도시 집합)
    if visited == (1 << n) - 1:     # 모든 도시를 방문했다면
        if graph[x][0]:             # 출발점으로 가는 경로가 있을 때
            return graph[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF

    if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, n):           # 모든 도시를 탐방
        if not graph[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue

        # 점화식 부분(위 설명 참고)
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]

# print(dfs(0, 1))