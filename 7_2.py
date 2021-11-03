import os
import yaml

from pprint import pprint

with open('folder.yaml') as f:
    templates = yaml.safe_load(f)

def create_folder(path,data):

    if not os.path.exists(path):
        os.mkdir(path)
    if isinstance(data,list):
        for param in data:
            create_folder(path,param)
    if isinstance(data,dict):
        for fol, sub in data.items():
            create_folder(f'{path}/{fol}', sub)
    if isinstance(data,str):
        with open(f'{path}/{data}', 'w') as f:
            pass

for folder, subfolder in templates.items():
    create_folder(folder, subfolder)
    
pprint(templates)