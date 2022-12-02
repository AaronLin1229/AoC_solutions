with open("ip", 'r') as f:
    arr = f.readlines()

    for i in range(len(arr)):
        arr[i] = arr[i][:-1]
        if arr[i] == '': arr[i] = -1
        else: arr[i] = int(arr[i])


max_cnt = -1
cnt = 0
for i in range(len(arr)):
    if arr[i] != -1:
        cnt += arr[i]
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 0

max_cnt = max(max_cnt, cnt)
print(max_cnt)
