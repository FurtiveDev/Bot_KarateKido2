from PIL import ImageGrab
import os
import time
 
def screenGrab():
    #Первый скрин
    box = (840,610,900,640) #поменять для своего экрана
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\image1' + '.png', 'PNG') #Cохраняет снимок экрана в формате PNG. Файл сохраняется в текущей рабочей директории.
    #Второй скрин
    box = (840,700,900,725) #поменять для своего экрана
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\image2' + '.png', 'PNG') 
    #Третий скрин
    box = (840,780,900,825) #поменять для своего экрана
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\image3' + '.png', 'PNG') 
    time.sleep(0.3)

def main():
    screenGrab()
 
if __name__ == '__main__':
    main()
