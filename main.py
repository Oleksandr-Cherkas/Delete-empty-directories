import os, sys, shutil
needed_size = None
temp = False
folderSize = 0
def getSize(start_path = '.'):
    folderSize = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                folderSize += os.path.getsize(fp)
    return folderSize
print("Welcome to the program for deleting folders by size.\nIf you run it by accident - type 'exit'\n")
while ((temp == False)) :
    try:
        needed_size = input("I want to delete all folders smaller than (bytes): ")
        if needed_size.lower() == "exit":
            print("Bye!")
            sys.exit()
        needed_size = int(needed_size)
        if (int(needed_size) < 0):
            raise ValueError
        else: 
            temp = True
    except ValueError:
        print("Type an integer value that bigger than 0!\n")

listOfDirs = []
for root, dirs, files in os.walk(".", topdown = False): 
   for name in dirs:
       if getSize(os.path.join(root, name)) <= needed_size:
           print(os.path.join(root, name), folderSize, 'bytes')
           listOfDirs.append(os.path.join(root, name))
if len(listOfDirs) > 0:
    delete = input('Delete?\ny - yes\nn - no\n').lower() 
    if delete == 'y':
        for i in listOfDirs:
            shutil.rmtree(i)
            print('deleted %s' % i)
    elif delete == 'n':
        print('Exit.\nBye!')
        sys.exit()
else:
    print('No directories found with your criteria.')
    sys.exit()