import os
import sys

with open("./qlist.txt", 'r') as f:
    fileName = f.read()
    filelist = fileName.split('\n')
    for file in filelist:
        newName = ''.join(file.split(' '))
        with open(newName+'.java', 'w') as f2:
            f2.write('import java.io.*;\nimport java.util.*;\nclass' + ' '+newName + ' {\n\n\tpublic static void main(String[] args) throws IOException {\n\n\t}\n}')