import os

def lister(path, indent):
    for filename in os.listdir(path):
        newpath = os.path.join(path,filename)
        if os.path.isdir(newpath):
            print(indent,'***', filename)
            lister(newpath,indent+' ')
        else:
            if filename[-3:] == '.py':
                print(indent,filename)
parentOfParent = os.path.join('..','..')
lister(parentOfParent,'')
