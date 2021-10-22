file = open('nginx_logs.txt', 'r', encoding='utf-8')
log_list=[]
dict_spam = {}
for line in file:
   r = line.split()
   log_list.append((r[0],r[5].replace('"',''),r[6]))
   dict_spam[r[0]] = 0
for i in log_list:
   dict_spam[i[0]]+= 1
list_sort_spam = list(dict_spam.items())
list_sort_spam.sort(key=lambda s: s[1],reverse=True)
"""Вывод списка с самым большим количеством запросов"""
for i in list_sort_spam:
   print(i)
print(dict_spam)
file.close()
