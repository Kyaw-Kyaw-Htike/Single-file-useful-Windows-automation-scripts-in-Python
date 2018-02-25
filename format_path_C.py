# given a full path copied in the clipboard, change it to all the backslashes escaped.
# this is useful when writing code where copying and pasting of paths have to be 
# performed a lot.

import win32clipboard as w

w.OpenClipboard()
txt = w.GetClipboardData()
txt = txt.replace('\\', '\\\\');
txt = txt.replace('\'', '"');
if txt[0] != '"':
	txt = '"' + txt
if txt[len(txt)-1] != '"':
	txt = txt + '"'
w.EmptyClipboard()
w.SetClipboardText(txt)
w.CloseClipboard()

	