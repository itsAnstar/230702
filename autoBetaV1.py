import tkinter as tk
import threading
import ctypes
import pyautogui
import time
import pyperclip
from tkinter import ttk
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener

# 初始化鼠标活跃状态变量
mouse_active = False

# 初始化全局坐标变量
global coord_x1, coord_y1, coord_x2, coord_y2, coord_x3, coord_y3
coord_x1, coord_y1, coord_x2, coord_y2, coord_x3, coord_y3 = 0, 0, 0, 0, 0, 0

# 鼠标移动事件处理
def on_move(x, y):
    global mouse_active
    mouse_active = True

# 鼠标停止移动事件处理
def on_stop(x, y):
    global mouse_active
    time.sleep(3)  # 等待3秒
    mouse_active = False

# 启动鼠标监听
mouse_listener = MouseListener(on_move=on_move, on_stop=on_stop)
mouse_listener.start()

# 主程序
def your_program():
    pyautogui.FAILSAFE = False

    time.sleep(5)

    try:
        global end_time
        end_time = time.time() + 240*60  
        start_time = time.time()  # 记录开始时间
        while time.time() < end_time:

            if mouse_active:  # 如果鼠标活跃，暂停进程
                continue
            try:
                global coord_x1, coord_y1, coord_x2, coord_y2, coord_x3, coord_y3
                # 移动到第一次点击的坐标并点击
                pyautogui.moveTo(coord_x1, coord_y1)
                pyautogui.click()

                # 移动到第二次点击的坐标并点击
                pyautogui.moveTo(coord_x2, coord_y2)
                pyautogui.click()
                time.sleep(5)  

                # 移动到第三次点击的坐标并点击
                pyautogui.moveTo(coord_x3, coord_y3)
                pyautogui.click()
                time.sleep(1)  

            except pyautogui.FailSafeException:
                while True:
                    time.sleep(5)  
                    if mouse.position == (coord_x1, coord_y1) and not keyboard_active:
                        break
                    keyboard_active = False  
                continue

    except KeyboardInterrupt:
        return(0)

# 鼠标点击事件处理
def on_click(x, y, button, pressed):
    if pressed:
        global coord_x1, coord_y1, coord_x2, coord_y2, coord_x3, coord_y3
        # 记录第一次点击的坐标
        if coord_x1 == coord_y1 == 0:
            coord_x1, coord_y1 = x, y
            coord_label1.config(text="x: {}, y: {}".format(coord_x1, coord_y1), bg="#FFDAB9")
        # 记录第二次点击的坐标
        elif coord_x2 == coord_y2 == 0:
            coord_x2, coord_y2 = x, y
            coord_label2.config(text="x: {}, y: {}".format(coord_x2, coord_y2), bg="#FFDAB9")
        # 记录第三次点击的坐标
        else:
            coord_x3, coord_y3 = x, y
            coord_label3.config(text="x: {}, y: {}".format(coord_x3, coord_y3), bg="#FFDAB9")
            return False  

# 启动鼠标监听
def copy_coord():
    listener = MouseListener(on_click=on_click)
    listener.start()  

# 启动程序
def start_program():
    threading.Thread(target=your_program).start()
    start_timer()

# 停止程序
def stop_program():
    global end_time
    end_time = time.time()
    stop_timer()

keyboard = KeyboardController()
mouse = MouseController()

# 主程序
def your_program():
    pyautogui.FAILSAFE = False

    time.sleep(5)

    try:
        global end_time,is_program_running
        end_time = time.time() + 240*60  
        is_program_running = True
        while time.time() < end_time and is_program_running:
            try:
                global coord_x1, coord_y1, coord_x2, coord_y2, coord_x3, coord_y3
                # 移动到第一次点击的坐标并点击
                pyautogui.moveTo(coord_x1, coord_y1)
                pyautogui.click()

                # 移动到第二次点击的坐标并点击
                pyautogui.moveTo(coord_x2, coord_y2)
                pyautogui.click()
                time.sleep(5)  

                # 移动到第三次点击的坐标并点击
                pyautogui.moveTo(coord_x3, coord_y3)
                pyautogui.click()
                time.sleep(1)  

            except pyautogui.FailSafeException:
                while True:
                    time.sleep(5)  
                    if mouse.position == (coord_x1, coord_y1) and not keyboard_active:
                        break
                    keyboard_active = False  
                continue

    except KeyboardInterrupt:
        return(0)

# 键盘按键事件处理
def on_press(key):
    global end_time,is_program_running
    if key == Key.esc:  # 如果按下的是ESC键
        end_time = time.time()  # 将end_time设为当前时间，以停止your_program中的循环
        is_program_running = False  # 设置is_program_running为False
        stop_timer()#停止倒计时
        return False


# 在新线程中启动键盘监听
keyboard_listener = KeyboardListener(on_press=on_press)
keyboard_listener.start()

def update_timer():
    global time_elapsed
    #倒计时总时长
    total_seconds=  14400

    #获取当前剩余秒数
    remaining_seconds = total_seconds - time_elapsed

     # 将剩余秒数转换成分钟和秒
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

     # 格式化显示时间为mm:ss
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

    # 继续更新倒计时，直到计时结束
    if remaining_seconds > 0 and not is_timer_stopped:
        time_elapsed += 1
        root.after(1000, update_timer)
    else:
        timer_label.config(text="请重启脚本")

# 定义开始计时函数
def start_timer():
    global is_timer_stopped, time_elapsed
    is_timer_stopped = False
    time_elapsed = 0
    update_timer()

# 定义停止计时函数
def stop_timer():
    global is_timer_stopped
    is_timer_stopped = True
    timer_label.config(text="请重启脚本")



# 创建GUI窗口
root = tk.Tk()

# 锁定窗体大小，使其不可缩放
root.resizable(False, False)

root.title("中控助手-alphaV2")

root.attributes('-topmost', 1)

root.minsize(450, 250)

# 在窗体上方居左创建一个长140像素，宽30像素的红色框
frame = tk.Frame(root, width=140, height=30,)
frame.place(relx=0.15, rely=0.05, anchor='nw')

# 创建显示倒计时的标签
timer_label = tk.Label(frame, text="240:00", bg="#dedede", fg="#0892d0", font=("Helvetica", 14))
timer_label.pack()

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')  

coord_label1 = tk.Label(root, text="[2链] x: 0, y: 0", bg="#dedede")
coord_label1.place(relx=0.25, rely=0.3, anchor='center')  
coord_label2 = tk.Label(root, text="[1链] x: 0, y: 0", bg="#dedede")
coord_label2.place(relx=0.25, rely=0.5, anchor='center')  
coord_label3 = tk.Label(root, text="查询 x: 0, y: 0", bg="#dedede")
coord_label3.place(relx=0.25, rely=0.7, anchor='center')    

frame = tk.Frame(root)
frame.place(relx=0.75, rely=0.43, anchor='center') 

# 创建选择坐标按钮
copy_button = tk.Button(frame, text="选择坐标", command=copy_coord)
copy_button.pack(side=tk.TOP, pady=(50, 10))  

start_button = tk.Button(frame, text="开始", command=start_program)
start_button.pack(side=tk.TOP, pady=(10, 10))  
stop_button = tk.Button(frame, text="停止", command=stop_program)
stop_button.pack(side=tk.TOP, pady=(10, 50))

# 创建一个标签显示“按下ESC键终止进程”
esc_label = tk.Label(root, text="运行中按下ESC键可终止进程", fg="lightcoral")
esc_label.pack(side=tk.BOTTOM)

# 启动GUI主循环
root.mainloop()