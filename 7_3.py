import os
import shutil

project_dir = 'my_project_yaml'
if not os.path.exists(f'{project_dir}/templates'):
    os.mkdir(f'{project_dir}/templates')
try:
    for root, dirs, files in os.walk(project_dir):
        if 'templates' in dirs and root !=project_dir :
            for sub in os.listdir(f'{root}/templates/'):
                if sub.find(".")==-1:
                    shutil.copytree(f'{root}/templates/{sub}',f'{project_dir}/templates/{sub}')
except FileExistsError:
    print('Папки уже существуют')