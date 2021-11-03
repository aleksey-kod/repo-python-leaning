import os
def create_folder(path,data):
    if data != []:
        for idx in data:
            for fol, sub in idx.items():
                create_folder(f'{path},{fol}',sub)
    s = path.split(',')
    dir_path = os.path.join(*s)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

list_folder={'my_project':
                 [{'settings':
                       [{'mysettings':[]}],
                   'mainapp':[],
                   'adminapp':[],
                   'authapp':[],
                   'test':[]
                   }]
             }
for folder, subfolder in list_folder.items():
    create_folder(folder, subfolder)