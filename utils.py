import keyboard
import pyautogui  # 图像识别组件
import pyperclip  # 键盘组件
import time  # 时间组件
import random  # 随机数组件
import sys
import os


# 图像识别方法
# img:待识别图片
# return:是否识别成功
def ocr(img):
    return pyautogui.locateCenterOnScreen(img, confidence=0.89)


# 鼠标点击方法
# pyautogui库用法 https://blog.csdn.net/qingfengxd1/article/details/108270159
# img:待识别图片
# clickTimes:点击次数(单击/双击)
# clickType:点击方式(左键单击/右键单击)
# reTry:重试查找方法(True:无限次数重试查找,False:有效次数重试查找)
def mouseClickMethod(img, clickTimes, lOrR, reTry, offsetX, offsetY):
    result = 0
    i = 0
    if reTry == True:
        while True:
            # 找到图片位置
            location = ocr(img)
            if location is not None:
                pyautogui.click(location.x + offsetX + random.random() * 5,
                                location.y + offsetY + random.random() * 5,
                                clicks=clickTimes,
                                interval=0.2,
                                duration=0.2,
                                button=lOrR)
                break
            print("未找到匹配图片，0.1秒后重试，当前尝试次数：", i)
            i += 1
    else:
        # 设置尝试次数
        # while i < 3:
        location = ocr(img)
        if location is not None:
            pyautogui.click(location.x + offsetX,
                            location.y + offsetY,
                            clicks=clickTimes,
                            interval=0.2,
                            duration=0.2,
                            button=lOrR)
            #break
        print("未找到匹配图片:", img)

        # if i == 4:
        #     print("尝试", i + 1, "次后仍无法匹配待识别图片，执行下一个方法。")
        #     break
        # i += 1
    time.sleep(0.2)


# 键盘复制粘贴方法
# value:待复制粘贴内容
def keyboardCopyAndPaste(value):
    pyperclip.copy(value)
    pyautogui.hotkey('ctrl', 'v')
    print("输入内容：", value)


# 鼠标滚轮方法
# distance:滚动距离
def mouseScroll(distance):
    pyautogui.scroll(int(distance))
    print("滚轮滑动距离：", int(distance), "px")


# 键盘控制程序停止方法
def keyboardCallback(key):
    space = keyboard.KeyboardEvent('down', 27, 'esc')
    if key.event_type == 'down' and key.name == space.name:
        pid = os.getpid()
        cmd = 'taskkill /pid ' + str(pid) + ' /f'
        os.system(cmd)
        sys.exit()
        os._exit()
