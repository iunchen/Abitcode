#python3.6
#按8开始，按9结束，但进程不会自己关闭，需要手动关闭

import win32api,time,win32con

def main():
    while True:
        if win32api.GetAsyncKeyState(56) != 0:
            while True:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                time.sleep(0.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                if win32api.GetAsyncKeyState(57) != 0:
                    break
        time.sleep(1)
        
if __name__=="__main__":
    main()
