# Reading and Writing Files with Python
# -------------------------------------

# Windows vs OS X & Linux on Backward\/Forward slashes
    # Windows uses \ as a separator
    # OS X & Linux use /
    # Multi-platform scripts will need to be able to handle both.
import os
os.path.join('usr', 'bin', 'spam')
    # This will return a path that uses the correct separators, no matter what OS you're running
    # Note: backslashes will be doubled due to \ being a special character, thus needing an extra one to escape

    # This can also be used with a path to append something onto the end, i.e. a filename
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))
    # C:\Users\asweigart\accounts.txt
    # C:\Users\asweigart\details.csv
    # C:\Users\asweigart\invite.docx