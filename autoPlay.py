from ctypes import util
import utils  # utils组件
import pyautogui  # 图像识别组件
import time
import pyperclip  # 键盘组件
import keyboard
import _thread

fileBase = "resources/"  # 文件路径前缀

def zdtk():
    while True:
        # 首先找到定位符
        mark = utils.ocr(fileBase + "wkw.png")
        # 是否播放标识
        if mark is not None:
            # 移动到定位符位置
            pyautogui.moveTo(mark.x,mark.y)
            print('正在查找待播放课程')
            # 是否已翻到页面底部
            if utils.ocr(fileBase + "bottom.png"):
                print('视频观看结束，停止执行')
                break
            # 显示达到当日达到最大课时则停止执行
            if utils.ocr(fileBase + "max_jg.png"):
                print('当日已达到最大播放课时')
                break
            # 当前页面因网络原因卡顿停止播放
            if utils.ocr(fileBase + "kd.png"):
                print('检测到页面卡顿，即将重新刷新页面')
                pyautogui.hotkey('f5')
                continue
            # 出现防刷课提示
            if utils.ocr(fileBase + "ts.png"):
                print('检测到开启防刷课提示，执行确定操作')
                utils.mouseClickMethod(fileBase + "qd.png", 1, "left", False, 0, 0)
            # 如果当前页面未显示播放按钮则代表正在播放
            if utils.ocr(fileBase + "bf.png") is None:
                print('当前课程正在播放，5秒后再次检测当前状态。')
                time.sleep(5)
                continue
            # 当前视频未播放则查找播放内容
            if utils.ocr(fileBase + "wkw.png"):
                # 点击未看完按钮
                utils.mouseClickMethod(fileBase + "wkw.png", 1, "left", False, 0, 0)
                # 页面上回滚
                utils.mouseScroll(3000)
                time.sleep(1)
                # 点击播放按钮
                utils.mouseClickMethod(fileBase + "bf.png", 1, "left", False, 0, 0)
                print('开始播放未看完课程')
            elif utils.ocr(fileBase + "wk.png"):
                # 点击未看课程
                utils.mouseClickMethod(fileBase + "wk.png", 1, "left", False, 0, 0)
                # 页面上回滚
                utils.mouseScroll(3000)
                time.sleep(1)
                # 点击播放按钮
                utils.mouseClickMethod(fileBase + "bf.png", 1, "left", False, 0, 0)
                print('开始播放未看课程')
            else:
                print('未找到待播放课程，继续下滑页面')
                utils.mouseScroll(-500)# 未找到目标课程则继续下滑
                time.sleep(1)
    else:
        print('未找到定位标识，检查当前课程页面是否被遮盖')
# 主函数
if __name__ == '__main__':
    try:
        # 开启一个线程执行主方法
        _thread.start_new_thread(zdtk,())
        # 开启另一个线程执行键盘监听方法，esc中止程序执行
        _thread.start_new_thread(keyboard.wait('esc'),())
    except KeyboardInterrupt:
        print('键盘按键意外中止了程序的执行')