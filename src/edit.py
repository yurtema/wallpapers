from PIL import Image, ImageDraw, ImageFont


def process(image, wd, hg, cx, cy):
    img = Image.new("RGB", (wd, hg))
    img.paste(image, (cx, cy))
    return img


def write(image, text):
    img = image.copy()
    # Конвертируем изображение в формат, который можно редактировать
    d1 = ImageDraw.Draw(img)

    # Вычисляем размер шрифта как процент от высоты изображения
    font_size = int(img.height * 0.014)
    line_spacing = font_size * 1.05
    x = img.width/192
    y = img.height/108

    # Выбираем шрифт из загруженного файла
    font = ImageFont.truetype('calibri.ttf', font_size)

    for i in text.split('\\n '):
        d1.text((x, y), i, fill=(255, 255, 255), font=font)
        y += line_spacing

    return img


