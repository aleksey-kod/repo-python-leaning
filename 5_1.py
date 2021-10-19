def odd_nums(n):
    for i in range(n):
        if i%2!=0:
            yield i

odd_to_15 = odd_nums(15)
print(type(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
for num in odd_to_15:
    print(num)
