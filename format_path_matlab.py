import win32clipboard as w

w.OpenClipboard()
txt = w.GetClipboardData()
txt = txt.replace('\\', '/');
txt = txt.replace('"', '\'');
if txt[0] != '\'':
	txt = '\'' + txt
if txt[len(txt)-1] != '\'':
	txt = txt + '\''
w.EmptyClipboard()
w.SetClipboardText(txt)
w.CloseClipboard()
