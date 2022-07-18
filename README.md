# Delete-empty-directories
This program is designed to detect and then delete folders that are smaller than the size specified in the code snack.

Originally created to remove only empty folders, but later modified to include a number.

At startup the program automatically works in a current folder, but after updating you also can simply enter the path to another directory (in the command line) to delete the folders in it.

Usage
===========
```
py main.py [path]

Optional argument:
  path                   The operation of this program will be
                         performed on the entered path instead of the current

```

Examples:
-----
For Linux:
```
py main.py 

py main.py C:\Users\Me\Desktop
```

For Windows:
```
py main.py 

py main.py C:\\Users\\Me\\Desktop

py main.py 'C:\Users\Me\Desktop'

py main.py C:/Users/Me/Desktop
```