import os

os.path.join('folder1', 'folder2', 'folder3', 'file.png')

os.getcwd()

os.chdir('c:\\')

os.path.dirname('c:\\folder1\\folder2\\spam.png')
os.path.basename('c:\\folder1\\folder2\\spam.png')

os.path.exists('c:\\folder1\\folder2\\spam.png')
os.path.isfile('c:\\folder1\\folder2\\spam.png')
os.path.isdir('c:\\folder1\\folder2\\spam.png')

os.makedirs('c:\\folder1')



helloFile = open('c:\\users\\joy\\hello.txt')
helloFile.read()
helloFile.close()
helloFile.readlines()
helloFile.write('\n\nBacon is delicious')


import shutil
shutil.copy('c:\\spam.txt', 'c:\\delicious')
shutil.copytree('c:\\delicious', 'c:\\delicious_backup')
shutil.move('c:\\delicious', 'c:\\delicious_backup')



# delete a file
os.unlink()

# delete a folder and all its contents
shutil.rmtree()



# Walking a directory tree
os.walk('c:\\')