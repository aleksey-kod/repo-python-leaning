import json
dict_users_hobby = {}
users = open('users.csv', 'r', encoding='utf-8')
hobby = open('hobby.csv', 'r', encoding='utf-8')
line_users = users.readline()
line_hobby = hobby.readline()
while line_users:
   if not line_hobby:
      dict_users_hobby[line_users.replace(',',' ').replace('\n','')]= None
   else:
      dict_users_hobby[line_users.replace(',',' ').replace('\n','')]= line_hobby.replace('\n','')
   line_users = users.readline()
   line_hobby = hobby.readline()

with open('user_hobby.json', 'w', encoding='utf-8') as f:
   json.dump(dict_users_hobby, f)
with open('user_hobby.json', 'r', encoding='utf-8') as f:
   dict_users_hobby = json.load(f)

print(dict_users_hobby)
users.close()
hobby.close()
exit(1)




