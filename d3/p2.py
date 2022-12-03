d = dict()

cnt = 1
for i in range(ord('a'), ord('z') + 1):
    d[chr(i)] = cnt
    cnt += 1
for i in range(ord('A'), ord('Z') + 1):
    d[chr(i)] = cnt
    cnt += 1


try:
    ans = 0
    while True:
        s1 = input()
        s2 = input()
        s3 = input()
        a = list(set(s1) & set(s2) & set(s3))
        a = a[0]
        ans += d[a]

except EOFError:
    print(ans)
