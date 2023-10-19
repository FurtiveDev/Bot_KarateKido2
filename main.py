import win32api, win32con
import time
from quickGrab import screenGrab
from pixel_here import check_pixel_color


def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
     
def get_cords(): # с помощью данной функции получаем координаты справа и слева от дерева в
    x,y = win32api.GetCursorPos()
    print (x,y) #624 568; 927 568 

def main():
    screenGrab()
    wood_upper = check_pixel_color('image1.png', (167, 92, 42))
    wood_middle = check_pixel_color('image2.png', (167, 92, 42))
    wood_lower = check_pixel_color('image3.png', (167, 92, 42))
    if wood_middle:
        click(927, 568)
    elif wood_lower and not wood_upper:
        click(927, 568)
    elif wood_lower and wood_upper:
        click(927, 568)
    elif wood_lower and wood_middle:
        click(927, 568)
    else:
        click(624, 568)
        time.sleep(0.2)
     #get_cords()

if __name__ == '__main__':
    i = 0
    while i!=100:
        i = i + 1
        main()