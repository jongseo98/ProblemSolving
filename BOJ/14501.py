# 실버3 퇴사
import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * n
dp.append(0)
for i in range(n-1, -1, -1):
    if t[i] + i <= n:
        dp[i] = max(dp[i+1], dp[i+t[i]] + p[i])
    else:
        dp[i] = dp[i+1]

print(max(dp))