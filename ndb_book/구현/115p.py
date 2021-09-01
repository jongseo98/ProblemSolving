loc = input()
x = 0
y = 0
row = ['1','2','3','4','5','6','7','8']
col = ['a','b','c','d','e','f','g','h']
for index in range(8):
  if loc[1] == row[index]:
    x = index + 1
  if loc[0] == col[index]:
    y = index + 1

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

count = 0
for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]
  if nx<1 or nx>8 or ny<1 or ny>8:
    continue
  count += 1

print(count)