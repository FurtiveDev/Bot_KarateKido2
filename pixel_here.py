from PIL import Image

def check_pixel_color(image, target_color):
    # Открыть изображение
    img = Image.open(image)

    # Получить размеры изображения
    width, height = img.size

    # Пройти по каждому пикселю
    for x in range(width):
        for y in range(height):
            # Получить цвет пикселя
            pixel = img.getpixel((x, y))
            if pixel == target_color:
                print("Цвет найден!")
                return 1;
    print("Цвет не найден!") #опциональные выводы
    return 0;
                

def main():
    check_pixel_color('image1.png', (167, 92, 42))
    check_pixel_color('image2.png', (167, 92, 42))
    check_pixel_color('image3.png', (167, 92, 42))
if __name__ == '__main__':
    main()
