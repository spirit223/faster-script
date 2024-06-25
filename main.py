from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pywinauto.application import Application
import os

global browser
expected_url = 'https://cp.kuaishou.com/article/publish/video'


def open_browser():
    print('打开浏览器中...')
    # open browser
    browser = webdriver.Chrome()
    browser.get('https://cp.kuaishou.com/')
    print('等待扫码登录并切换至视频上传页面...')
    # wait scan code
    WebDriverWait(browser, 60).until(EC.url_to_be(expected_url))
    print('发现视频上传页面')


def locate_introduction() -> str:
    """
    接收用户输入的视频简介
    :return: str
    """
    print('输入视频简介后按回车：')
    intro = input()
    return intro


def locate_file_dir():
    """
    接收用户输入的绝对路径, 对绝对路径进行校验后查看是否存在错误
    如果路径输入正确则对视频文件进行过滤后存储在列表中返回
    :return: 文件上传路径 ,文件名称列表
    """
    print('输入上传文件的绝对路径: ')
    upload_dir = input()
    try:
        files = os.listdir(upload_dir)
    except FileNotFoundError as e:
        print('路径文件读取失败, 请检查文件路径. 当前文件路径为: ' + upload_dir)
        exit()

    filter_files = []
    for file in files:
        if file.endswith(".mp4"):
            filter_files.append(file)
    if len(filter_files) == 0:
        print('没有待上传mp4文件, 程序即将退出')
        exit()
    else:
        print('扫描到' + str(int(len(filter_files))) + '个待上传文件')
    return upload_dir, files


def handle_upload(base_url: str, file_list: list[str], introduction: str):
    """
    处理视频上传
    :return:
    """
    counter = 1
    print('正在处理第' + str(counter) + '个文件')
    # wait page directive
    sleep(3)
    # find upload file
    upload_button = browser.find_element(By.XPATH,
                                         '//*[@id="app"]//*[@class="complete"]//*[@class="container"]/main//*[@class="main-content"]/*[@class="main-content__body"]//*[@class="content-card"]/div//*[@id="root-video-publish"]/haploid-html/haploid-body//*[@id="onvideo_creator_platform"]//*[@class="ant-tabs-content-holder"]//button')
    upload_button.click()
    sleep(1)
    # handle file choose
    app = Application().connect(title_re='打开', class_name='#32770')  # 根据窗口的标题和类名调整

    filename = base_url + '\\' + file_list[counter - 1]
    dlg = app.window(title_re='打开', class_name='#32770')
    dlg['Edit'].set_edit_text(filename)
    sleep(1)
    # 点击“打开”按钮
    # todo: please check this button whether open button, maybe open button is Button1 in win10 or in selenium
    # in selenium, Button2 is cancel button
    button_ = dlg['Button1']
    button_.print_control_identifiers()
    while button_:
        button_.click()
        sleep(1)
    sleep(30)
    # tips
    tips = browser.find_element(By.XPATH, '//*[@id="react-joyride-step-0"]/div/div/div[1]/button/span')
    # find input area
    input_area = browser.find_element(By.XPATH,
                                      '/html/body/div[1]/div[1]/div[1]/main/div/div/div[1]/div/div/haploid-html/haploid-body/div/div/div/div/div[1]/div/div[4]/div/div[4]/div[2]/div[1]/div/div/div')
    # find push button
    push = browser.find_element(By.XPATH,
                                '/html/body/div[1]/div[1]/div[1]/main/div/div/div[1]/div/div/haploid-html/haploid-body/div/div/div/div/div[1]/div/div[4]/div/div[4]/div[2]/div[9]/button[1]/span')
    # close tips
    tips.click()
    # waiting for file upload
    sleep(3)
    # focus and input message
    input_area.click()
    # input introduction
    input_area.send_keys(introduction)
    # push video
    push.click()
    # directive upload page
    browser.get(expected_url)

    print('第' + str(counter) + '个文件上传成功')
    for file in file_list:
        if file == file_list[0]:
            continue
        # wait page directive
        sleep(3)
        upload_button = browser.find_element(By.XPATH,
                                             '//*[@id="app"]//*[@class="complete"]//*[@class="container"]/main//*[@class="main-content"]/*[@class="main-content__body"]//*[@class="content-card"]/div//*[@id="root-video-publish"]/haploid-html/haploid-body//*[@id="onvideo_creator_platform"]//*[@class="ant-tabs-content-holder"]//button')
        upload_button.click()
        sleep(1)
        # here are opening file choose dialog
        app = Application().connect(title_re='打开', class_name='#32770')  # 根据窗口的标题和类名调整

        filename = base_url + '\\' + file
        dlg = app.window(title_re='打开', class_name='#32770')
        dlg['Edit'].set_edit_text(filename)
        sleep(1)
        # 点击“打开”按钮 todo please check this button whether open button, maybe open button is Button1 in win10
        button_ = dlg['Button2']
        button_.print_control_identifiers()
        button_.click()
        sleep(40)
        # input introduction
        input_area = browser.find_element(By.XPATH,
                                          '/html/body/div[1]/div[1]/div[1]/main/div/div/div[1]/div/div/haploid-html/haploid-body/div/div/div/div/div[1]/div/div[4]/div/div[4]/div[2]/div[1]/div/div/div')
        # find push button
        push = browser.find_element(By.XPATH,
                                    '/html/body/div[1]/div[1]/div[1]/main/div/div/div[1]/div/div/haploid-html/haploid-body/div/div/div/div/div[1]/div/div[4]/div/div[4]/div[2]/div[9]/button[1]/span')

        # waiting for file upload
        sleep(5)
        # focus and input message
        input_area.click()
        # input introduction
        input_area.send_keys(introduction)
        # push video
        push.click()
        # directive upload page
        browser.get(expected_url)
        print('第' + str(++counter) + '个文件上传成功')

    sleep(1)
    print('文件上传完成，上传文件总数: ' + str(++counter))


if __name__ == '__main__':
    # 确定上传的文件路径
    base_url, to_upload_file_list = locate_file_dir()
    # 确定所有视频的简介
    introduction_input = locate_introduction()
    # 开启浏览器, 登录后切换至视频上传页面
    open_browser()
    # 处理文件上传
    handle_upload(base_url, to_upload_file_list, introduction_input)
    print('done')
