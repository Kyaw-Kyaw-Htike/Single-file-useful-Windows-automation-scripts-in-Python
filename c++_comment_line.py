# get a nicely formatted C++ comment line for dividing sessions in the clipboard

import win32clipboard as w
import sys

w.OpenClipboard()
cdata = w.GetClipboardData()

try:
	line_type = int(cdata)
except ValueError:
	w.EmptyClipboard()
	w.SetClipboardText('/'*50)
	w.CloseClipboard()	
	sys.exit(1)
	
w.EmptyClipboard()
if line_type == 1:
	w.SetClipboardText('/'*50)
elif line_type == 2:
	w.SetClipboardText('/'*20 + ' '*20 + '/'*20)
else:
	w.SetClipboardText('/'*50)
	
w.CloseClipboard()