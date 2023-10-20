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
    wood_middle = check_pixel_color('image2.png', (211, 135, 85))
    if not wood_middle:
        metal_middle = check_pixel_color('image2.png', (133, 142, 164))
        if not metal_middle:
                metal_middle = check_pixel_color('image2.png', (132, 141, 164))
        semi_metal_middle = check_pixel_color ('image2.png', (209, 178, 153))
        if not semi_metal_middle:
                semi_metal_middle = check_pixel_color('image2.png', (209, 178, 152))
        some_material = check_pixel_color('image2.png',(170, 150, 171))
    ice = check_pixel_color('image1.png', (240, 239, 239))
    if not ice :
        ice = check_pixel_color('image1.png', (245, 243, 243))
    if wood_middle or metal_middle or semi_metal_middle or some_material:
        click(927, 568)
        if ice:
            time.sleep(0.2)
            click(927,568)
        wood_lower = 1
    elif wood_lower:
        wood_lower = 0
        click(927, 568)
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