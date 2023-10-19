from PIL import ImageGrab
import os
 
def screenGrab(): # Каждый скрин соответствует определенному дереву, например image1 соответствует высшей ветке дерева
    #Первый скрин
    # box = (840,610,900,640) #поменять для своего экрана
    # im = ImageGrab.grab(box)
    # im.save(os.getcwd() + '\\image1' + '.png', 'PNG') #Cохраняет снимок экрана в формате PNG. Файл сохраняется в текущей рабочей директории.
    #Второй скрин
    box = (820,700,920,725) #поменять для своего экрана
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\image2' + '.png', 'PNG') 
    #Третий скрин
    # box = (840,780,900,825) #поменять для своего экрана
    # im = ImageGrab.grab(box)
    # im.save(os.getcwd() + '\\image3' + '.png', 'PNG') 

def main():
    screenGrab()
 
if __name__ == '__main__':
    main()
