list=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(list))
for idx in range(len(list)):
    if list[idx].isdigit():
        list[idx] = list[idx].rjust(2,"0")
    elif list[idx][1:].isdigit():
        list[idx] = list[idx][:1]+list[idx][1:].rjust(2, "0")
listfin =' '.join(list)
print(listfin)
print(id(list))
print(id(listfin))
# Реализация задачи 3
while (len(list)>1):
    list[0]=list[0]+' '+list[1]
    list.pop(1)
print(list)
print(id(list))
