# save content in clipboard to a file
# reference: https://stackoverflow.com/questions/45014501/trying-to-write-copied-data-in-a-text-file-in-python

import pyperclip
s = pyperclip.paste() 

with open('new.txt','w') as g:
   g.write(s)