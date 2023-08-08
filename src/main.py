from PIL import Image
from shutil import move
from os import listdir
import edit

Image.MAX_IMAGE_PIXELS = None


def show(im):
    """Уменьшает разрешение переданного изображения и показывает его пользователю"""
    new_height = 675
    new_width = int(new_height * 16 / 9)

    _img_tmp = im.resize((new_width, new_height))

    _img_tmp.show()


while True:
    command = input().split(' ')

    if command[0] == 'open':
        # Открываем первое изображение из папки с фото
        img_name = listdir('D:/обои для переработки/')[0]
        img = Image.open(f'D:/обои для переработки/{img_name}')

        # Если изображение вертикальное, делаем холст высотой с изображение и помещает изображение в центр
        # чтобы затем в коде добавились черные полосы слева и справа
        if img.height > img.width:
            canvas_height = img.height
            canvas_width = int(canvas_height * 16 / 9)
        # Если изображение горизонтальное, делает холст шириной с изображение и помещает
        # изображение в центре
        # Если изображение вылезает сверху и снизу, обрезаем
        # Если изображение не дотягивается до верхнего и нижнего края, будут добавлены черные полосы
        else:
            canvas_width = img.width
            canvas_height = int(canvas_width / 16 / 9)

        # Вычисляем где должны быть углы изображения на холсте чтобы изображение было в центре
        cornerx = canvas_width / 2 - img.width / 2
        cornery = canvas_height / 2 - img.height / 2

        print(f'Открыл изображение {img_name}')

        show(img)

    if not img:
        print('Вы еще не открыли изображения')
        continue

    if command[0] == '-':
        # Увеличиваем холст (следовательно изображение уменьшается)
        dwidth = canvas_width / 1000 * int(command[1])
        dheight = canvas_height / 1000 * int(command[1])
        canvas_width += dwidth
        canvas_height += dheight
        # Сдвигаем центр чтобы изображение не уехало
        cornerx += dwidth / 2
        cornery += dheight / 2

        print(
            f'Вы уменьшили изображение на {dwidth, dheight}\"')

    if command[0] == '+':
        # Уменьшаем холст (следовательно изображение увеличивается)
        dwidth = canvas_width / 1000 * int(command[1])
        dheight = canvas_height / 1000 * int(command[1])
        canvas_width -= dwidth
        canvas_height -= dheight
        # Сдвигаем центр чтобы изображение не уехало
        cornerx -= dwidth / 2
        cornery -= dheight / 2

        print(
            f'Вы увеличили изображение на {dwidth, dheight}\"')

    if command[0] == '4':
        # Дивгаем изображение на холсте налево на n тысячных долей холста
        dx = canvas_width / 1000 * int(command[1])
        cornerx -= dx

        print(f'Сдвинули изображение влево на {command[1]}')

    if command[0] == '8':
        # Дивгаем изображение на холсте наверх на n тысячных долей холста
        dy = canvas_width / 1000 * int(command[1])
        cornery -= dy

        print(f'Сдвинули изображение вверх на {command[1]}')

    if command[0] == '6':
        # Дивгаем изображение на холсте направо на n тысячных долей холста
        dx = canvas_width / 1000 * int(command[1])
        cornerx += dx

        print(f'Сдвинули изображение вправо на {command[1]}')

    if command[0] == '2':
        # Дивгаем изображение на холсте вниз на n тысячных долей холста
        dy = canvas_width / 1000 * int(command[1])
        cornery += dy

        print(f'Сдвинули изображение вниз на {command[1]}')

    if command[0] == 'show':
        # Делаем изображение с нужными параметрами и показываем пользователю
        img_changed = edit.process(img, int(canvas_width), int(canvas_height), int(cornerx), int(cornery))

        show(img_changed)

    if command[0] == 'centery':
        # Заново вычисляем где нужно установить центр чтобы изображение было посередине холста по y
        cornery = canvas_height / 2 - img.height / 2

        print('Поместил изображение по центру на оси y')

    if command[0] == 'centerx':
        # Заново вычисляем где нужно установить центр чтобы изображение было посередине холста по x
        cornerx = canvas_width / 2 - img.width / 2

        print('Поместил изображение по центру на оси x')

    if command[0] == 'write':
        # Пишем заданный текст в левом верхнем углу холста и показываем пользователю получившееся
        img_changed = edit.process(img, int(canvas_width), int(canvas_height), int(cornerx), int(cornery))
        img_txt = edit.write(img_changed, ' '.join(command[1:]))

        show(img_txt)

    if command[0] == 'save':
        # Если пользователь ничего не написал, обрабатываем изображение
        if not img_txt:
            img_txt = edit.process(img, int(canvas_width), int(canvas_height), int(cornerx), int(cornery))
        # Сохраняем по нужному адресу и двигаем в папку с сырыми обоями
        img_txt.save(f'D:/обои/{" ".join(command[1:])}.png')
        move(f'D:/обои для переработки/{img_name}', f'D:/обои сырые/{img_name}')

        print(f'Сохранил по адресу D:/обои/{" ".join(command[1:])}.png')
