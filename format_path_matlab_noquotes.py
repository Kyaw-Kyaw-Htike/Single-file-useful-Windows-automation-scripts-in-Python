import win32clipboard as w

w.OpenClipboard()
txt = w.GetClipboardData()
txt = txt.replace('\\', '/');
txt = txt.replace('"', '');
txt = txt.replace('\'', '');
w.EmptyClipboard()
w.SetClipboardText(txt)
w.CloseClipboard()
