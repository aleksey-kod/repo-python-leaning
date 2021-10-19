src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new = [src[i] for i in range(1,len(src)) if src.count(src[i])==1]
print(new)