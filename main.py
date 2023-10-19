import win32api, win32con
import time
from quickGrab import screenGrab
from pixel_here import check_pixel_color


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
     
def get_cords(): # с помощью данной функции получаем координаты справа и слева от дерева в
    x,y = win32api.GetCursorPos()
    print (x,y) #624 568; 927 568 

def main():
    global wood_lower
    screenGrab()
    ice = check_pixel_color('image2.png', (234, 234, 235))
    wood_middle = check_pixel_color('image2.png', (167, 92, 42))
    metal_middle = check_pixel_color('image2.png', (104, 114, 143))
    semi_metal_middle = check_pixel_color ('image2.png', (209, 178, 152))
    some_material = check_pixel_color('image2.png', (129, 113, 130))
    
    if wood_middle or metal_middle or semi_metal_middle or some_material:
        click(927, 568)
        click(927, 568)
        time.sleep(0.3)
        if ice:
            time.sleep(0.2)
            click(927,568)
    else:
        click(624, 568)
     #get_cords()

if __name__ == '__main__':
    i = 0
    wood_lower = 0
    while i!=1000:
        print(i)
        i = i + 1
        main()