# 골드5 Fly me to the Alpha Centauri
# https://eunhee-programming.tistory.com/99 -> 잘 모르겠음 (수학문제)
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    n = 0

    while True:
        if distance <= n * (n+1):
            break
        n += 1
    
    if distance <= n**2:
        print(n*2 - 1)
    else:
        print(n*2)