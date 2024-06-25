import win32gui as win

# if find the windows, window_handle is not be zero
window_handle = win.FindWindow(None, '打开')
# left, right, top, bottom = win.GetWindowRgn(window_handle)
# print(left, right, top, bottom)
print(window_handle)

