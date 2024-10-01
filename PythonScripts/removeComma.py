# write code to remove comma from a file

import os


def removeComma(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        for line in lines:
            f.write(line.replace(',', ' '))
    print('Comma removed successfully')
    
for i in range(1,4):
    filename = "../Registration/Groups/group" + str(i) + ".txt"
    if os.path.exists(filename):
        removeComma(filename)
        
# Output:

    