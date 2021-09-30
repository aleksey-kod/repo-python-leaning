
cube_list = []
for i in range(1, 1001, 2):
    cube_list.append(i ** 3)
#print(cube_list)
zadanie = 2
while zadanie != 0:
    summalist = 0
    for idx in range(len(cube_list)):
        temp = cube_list[idx]
        sum_n = 0
        while temp != 0:
            sum_n = sum_n + temp % 10
            temp = temp//10
        if sum_n % 7 == 0:
            summalist+=cube_list[idx]
    print(summalist)
    for idx in range(len(cube_list)):
        cube_list[idx]=cube_list[idx]+17
    zadanie -=1





