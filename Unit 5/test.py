import os

def lister(path):
    for filename in os.listdir(path):
        return filename

def open_file(file_name):
    file = open(os.path.join(path,file_name))
    
    

path = '.'

file_name = lister(path)
print(file_name)
