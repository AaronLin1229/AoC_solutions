with open("ip", 'r') as f:
    arr = f.readlines()
for i in range(len(arr)):
    arr[i] = arr[i][:-1]


ans = 0
for line in arr:
    pts = 0
    me = line[2]
    op = line[0]

    if me == "X": #r
        pts += 1
        if op == 'A': # tie
            pts += 3
        elif op == 'B': # lose
            pts += 0
        elif op == 'C': # win
            pts += 6
    elif me == "Y": #p
        pts += 2
        if op == 'A': # win
            pts += 6
        elif op == 'B': # tie
            pts += 3
        elif op == 'C': # lose
            pts += 0
    elif me == "Z": #s
        pts += 3
        if op == 'A': # lose
            pts += 0
        elif op == 'B': # win
            pts += 6
        elif op == 'C': # tie
            pts += 3

    ans += pts


print(ans)
