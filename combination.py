def combination(arr, r):
    arr.sort()
    
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
        
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            generate(chosen)
            chosen.pop()

    generate([])

combination([1, 2, 3, 4], 2)

# 중복 제거 조합
def combination2(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])

combination2("AABC", 2)