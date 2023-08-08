from PIL import Image
from shutil import move
from os import listdir
import edit

Image.MAX_IMAGE_PIXELS = None

img_txt = None
img = None
img_name = None
centerx = 0
centery = 0
width = 0
height = 0


def show(im):
    new_width = 1260
    new_height = int(new_width * 1080 / 1920)

    _img_tmp = im.resize((new_width, new_height))

    _img_tmp.show()


while True:
    command = input().split(' ')

    if command[0] == 'open':
        img_name = listdir('D:/обои для переработки/')[0]
        img = Image.open(f'D:/обои для переработки/{img_name}')
        img_txt = img.copy()

        if img.height > img.width:
            height = img.height
            width = int(height * (1920 / 1080))
        else:
            width = img.width
            height = int(width / (1920 / 1080))

        centerx = width / 2 - img.width / 2
        centery = height / 2 - img.height / 2

        print(f'Открыл изображение {img_name}')

        show(img)

    if not img:
        print('Вы еще не открыли изображения')
        continue

    if command[0] == '-':
        dwidth = width / 1000 * int(command[1])
        dheight = height / 1000 * int(command[1])
        width += dwidth
        height += dheight
        centerx += dwidth / 2
        centery += dheight / 2

        print(
            f'Вы уменьшили изображение на {dwidth, dheight}\"')

    if command[0] == '+':
        dwidth = width / 1000 * int(command[1])
        dheight = height / 1000 * int(command[1])
        width -= dwidth
        height -= dheight
        centerx -= dwidth / 2
        centery -= dheight / 2

        print(
            f'Вы увеличили изображение на {dwidth, dheight}\"')

    if command[0] == '4':
        dx = width / 1000 * int(command[1])
        centerx -= dx

        print(f'Сдвинули изображение влево на {command[1]}')

    if command[0] == '8':
        dy = width / 1000 * int(command[1])
        centery -= dy

        print(f'Сдвинули изображение вверх на {command[1]}')

    if command[0] == '6':
        dx = width / 1000 * int(command[1])
        centerx += dx

        print(f'Сдвинули изображение вправо на {command[1]}')

    if command[0] == '2':
        dy = width / 1000 * int(command[1])
        centery += dy

        print(f'Сдвинули изображение вниз на {command[1]}')

    if command[0] == 'show':
        img_changed = edit.process(img, int(width), int(height), int(centerx), int(centery))

        show(img_changed)

    if command[0] == 'centery':
        centery = height / 2 - img.height / 2

        print('Поместил изображение по центру на оси y')

    if command[0] == 'centerx':
        centerx = width / 2 - img.width / 2

        print('Поместил изображение по центру на оси x')

    if command[0] == 'write':
        img_changed = edit.process(img, int(width), int(height), int(centerx), int(centery))
        img_txt = edit.write(img_changed, ' '.join(command[1:]))

        show(img_txt)

    if command[0] == 'save':
        img_txt.save(f'D:/обои/{" ".join(command[1:])}.png')
        move(f'D:/обои для переработки/{img_name}', f'D:/обои сырые/{img_name}')

        print(f'Сохранил по адресу D:/обои/{" ".join(command[1:])}.png')
