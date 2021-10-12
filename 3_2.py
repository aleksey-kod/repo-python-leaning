def thesaurus(*args):
    dict ={}
    for i in args:
        if dict.get(i[0]) == None:
            dict[i[0]] =[i]
        else:
            dict[i[0]] = dict[i[0]]+[i]
    return dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
""" Если требуется сортировка """
dict = thesaurus("Мария", "Петр", "Илья","Иван" )
list_keys = list(dict.keys())
list_keys.sort()
for i in list_keys:
    print(i, ':', dict[i])
print()
