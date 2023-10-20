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
            # print(pixel)
            if pixel == target_color:
            # if (target_color[0] - 3 <= pixel[0] <= target_color[0] + 3) and (target_color[1] - 3 <= pixel[1] <= target_color[1] + 3) and (target_color[2] - 3 <= pixel[2] <= target_color[2] + 3):
                print("Цвет найден!")
                return 1
    print("Цвет не найден!") #опциональные выводы
    return 0;
                

def main():
    # Проверить цвета, тут можно протестить
    print("1")
    check_pixel_color('image2.png', (211, 135, 85))
    print("2")
    check_pixel_color('image2.png', (132, 141, 164))
    print("3")
    check_pixel_color('image2.png', (209, 178, 153))
    print("4")
    check_pixel_color('image2.png', (170, 150, 171))
    print("5")
    check_pixel_color('image1.png', (240, 239, 239))
    print("6")
    check_pixel_color('image1.png', (245, 212, 221))
if __name__ == '__main__':
    main()
