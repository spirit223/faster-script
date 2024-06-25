import os
import time
from pywinauto.application import Application

if __name__ == '__main__':
    # C:\Users\22355\Desktop\upload
    print('输入待上传文件路径: ')
    # file_dir = input()
    file_dir = 'C:\\Users\\22355\Desktop\\upload'
    file_list = os.listdir(file_dir)
    # for file_name in file_list:
    #     print(file_name, end='\n')

    filename = file_dir + '\\' + file_list[0]
    print(filename)
    app = Application().connect(title_re='打开', class_name='#32770')  # 根据窗口的标题和类名调整
    dlg = app.window(title_re='打开', class_name='#32770')
    dlg['Edit'].set_edit_text(filename)
    time.sleep(2)
    # 点击“打开”按钮
    dlg['Button2'].click()
