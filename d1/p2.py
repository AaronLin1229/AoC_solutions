with open("ip", 'r') as f:
    arr = f.readlines()

    for i in range(len(arr)):
        arr[i] = arr[i][:-1]
        if arr[i] == '': arr[i] = -1
        else: arr[i] = int(arr[i])

cnt = 0
car_arr = []
for i in range(len(arr)):
    if arr[i] != -1:
        cnt += arr[i]
    else:
        car_arr.append(cnt)
        cnt = 0

if(car_arr != 0):
    car_arr.append(cnt)
    cnt = 0

car_arr.sort(reverse = True)
print(car_arr[0] + car_arr[1] + car_arr[2])
