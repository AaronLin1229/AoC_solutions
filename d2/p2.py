with open("ip", 'r') as f:
    arr = f.readlines()
for i in range(len(arr)):
    arr[i] = arr[i][:-1]

# 1 for Rock, 2 for Paper, and 3 for Scissors

ans = 0
for line in arr:
    me = line[2]
    op = line[0]

    if me == "X": # lose
        ans += 0
        if op == 'A': # choose s
            ans += 3
        elif op == 'B': # choose r
            ans += 1
        elif op == 'C': # choose p
            ans += 2
    elif me == "Y": # tie
        ans += 3
        if op == 'A': # choose r
            ans += 1
        elif op == 'B': # choose p
            ans += 2
        elif op == 'C': # choose s
            ans += 3
    elif me == "Z": # win
        ans += 6
        if op == 'A': # choose p
            ans += 2
        elif op == 'B': # choose s
            ans += 3
        elif op == 'C': # choose r
            ans += 1

print(ans)
