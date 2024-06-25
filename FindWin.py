import pywinauto.findwindows
from pywinauto import Application

if __name__ == '__main__':
    app = Application().connect(title='打开')
    window = app.window(title='打开')
    children = window.children()
    buttons = [child for child in children if child.window_text()]
    for button in buttons:
        if button.element_info.name.find('打开') != -1:
            print(button)

