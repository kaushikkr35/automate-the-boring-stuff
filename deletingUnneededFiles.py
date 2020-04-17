import os, send2trash, shutil

directory = input('Enter the absolute path of the directory that you wish to search: ')
size_cap = int(input('Enter the threshold file size (in MB) above which you would like to detect files: '))
size_cap_mb = size_cap * 100000

print('The following files have a size greater than %d MB' % (size_cap))
for folders, subfolders, files in os.walk(directory):
    for filename in files:
        sizecheck = os.path.getsize(os.path.join(folders, filename))

        if sizecheck > size_cap_mb:
            print('Name:', filename, ' Size:', str(round(sizecheck/100000,2)), ' MB')

exit()
