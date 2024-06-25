from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import pyautogui
import os


def open_browser(introduction='视频简介'):
    files = os.listdir('C:/Users/Administrator/upload')
    filter_files = []
    for file in files:
        if file.endswith(".mp4"):
            filter_files.append(file)
    if len(filter_files) == 0:
        print('没有待上传mp4文件, 程序即将退出')
        return
    else:
        print('扫描到' + str(int(len(filter_files))) + '个待上传文件')

    # open browser
    expected_url = 'https://cp.kuaishou.com/article/publish/video'
    browser = webdriver.Chrome()
    browser.get('https://cp.kuaishou.com/')
    # wait scan code
    WebDriverWait(browser, 60).until(EC.url_to_be(expected_url))
    # wait page directive
    sleep(3)
    # find upload file
    upload_button = browser.find_element(By.XPATH,
                                         '//*[@id="app"]//*[@class="complete"]//*[@class="container"]/main//*[@class="main-content"]/*[@class="main-content__body"]//*[@class="content-card"]/div//*[@id="root-video-publish"]/haploid-html/haploid-body//*[@id="onvideo_creator_platform"]//*[@class="ant-tabs-content-holder"]//button')
    upload_button.click()
    sleep(2)
    filename = 'upload\\' + filter_files[0]
    pyautogui.typewrite(filename)
    sleep(2)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    sleep(1)
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
    counter = 1
    print('第' + str(counter) + '个文件上传成功')
    for file in filter_files:
        if file == filter_files[0]:
            continue
        # wait page directive
        sleep(3)
        upload_button = browser.find_element(By.XPATH,
                                             '//*[@id="app"]//*[@class="complete"]//*[@class="container"]/main//*[@class="main-content"]/*[@class="main-content__body"]//*[@class="content-card"]/div//*[@id="root-video-publish"]/haploid-html/haploid-body//*[@id="onvideo_creator_platform"]//*[@class="ant-tabs-content-holder"]//button')
        upload_button.click()
        sleep(2)
        # here are opening file choose dialog
        # catch file url input by pyautogui
        sleep(1)
        # D:/desktop/可上传/1.mp4
        pyautogui.typewrite(file)
        sleep(2)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        sleep(40)
        # close tips
        # tips = browser.find_element(By.XPATH, '//*[@id="react-joyride-step-0"]/div/div/div[1]/button/span')
        # tips.click()
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


def show_tips():
    print('请确保视频文件为mp4格式放置在C:/Users/Administrator/upload中')
    print('输入视频简介后按回车：')
    intro = input()
    return intro


if __name__ == '__main__':
    introduction_input = show_tips()
    open_browser(introduction_input)
    print('done')
