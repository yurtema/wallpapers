from PIL import Image, ImageDraw, ImageFont
import config


def process(image, wd, hg, cx, cy):
    """Создает черный холст с нужными размерами и добавляет изображение в нужные координаты.
    Возвращает полученный объект"""
    img = Image.new("RGB", (wd, hg))
    img.paste(image, (cx, cy))
    return img


def write(image, text):
    """Пишет в левом верхнем углу текст. Возвращает полученный объект"""

    # Копируем изображение чтобы не трогать исходное
    img = image.copy()
    # Добавляем объект для "рисования" на изображении
    d1 = ImageDraw.Draw(img)

    # Вычисляем размер шрифта как процент от высоты изображения чтобы размер букв был одинакновым на всех разрешениях
    font_size = int(img.canvas_height * config.font_size)
    # Вычисляем межстрочный интервал как процент от размера шрифта по тем же причинам
    line_spacing = font_size * config.line_spacing
    # Вычисляем координаты текста как процент от размеров изображения по тем же причинам
    x = img.width * 0.00521
    y = img.height * 0.00926

    # Выбираем шрифт из загруженного файла
    font = ImageFont.truetype('font.ttf', font_size)

    # Делим текст на строки и каждую строку пишем на изображении со смещением вниз
    for i in text.split('\\n '):
        d1.text((x, y), i, fill=(255, 255, 255), font=font)
        y += line_spacing

    return img


