import os # easy to use files 
import hashlib # makes a specific hash for every file
import tkinter # graphics
from tkinter.filedialog import askdirectory # get the user to select a folder

tkinter.Tk().withdraw() # prevents a windiow from showing

path = askdirectory(title='Select a folder') # opens a window that asks the user to select a folder

walk = os.walk(path) # walks trough all the files and folders and subfolders in the users chosen folder 

uniquefiles = dict() # list of files that only appeard once

score = 0

for folder,sub_folder,files in walk:
    for file in files:
        filepath = os.path.join(folder,file) # joining the path
        filehash = hashlib.md5(open(filepath,'rb').read()).hexdigest()

        if filehash in uniquefiles:
            os.remove(filepath)
            print(f'{filepath} has been removed')
            score += 1
        else:
            uniquefiles[filehash]=path

if score == 0:
    print('There are no duplicates in this folder.')