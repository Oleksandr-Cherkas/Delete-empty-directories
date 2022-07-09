import os, sys, shutil

def getSize(start_path = '.'):
    folderSize = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                folderSize += os.path.getsize(fp)
    return folderSize

def main():
    needed_size = None
    print("Welcome to the program for deleting folders by size.\nIf you run it by accident - type 'exit'\n")
    while True:
        try:
            needed_size = input("I want to delete all folders smaller than (bytes): ")
            if needed_size.lower() == "exit":
                print("Bye!")
                sys.exit()
            needed_size = int(needed_size)
            if (needed_size < 0):
                raise ValueError
            else:
                break
        except ValueError:
            print("Type an integer value that bigger than 0!\n")

    listOfDirs = []
    startDirectory = "."
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]) == False:
            print('No directories found with your criteria.')
            sys.exit()
        startDirectory = sys.argv[1]

    currentFolderSize = getSize(os.path.join(startDirectory))
    if currentFolderSize < needed_size:
        print(os.path.join(startDirectory), currentFolderSize, 'bytes')
        listOfDirs.append(os.path.join(startDirectory))
    else:
        for root, dirs, files in os.walk(startDirectory, topdown = False): 
           for name in dirs:
               folderSize = getSize(os.path.join(root, name))
               if folderSize <= needed_size:
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


if __name__ == '__main__':
    main()
