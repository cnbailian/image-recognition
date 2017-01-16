"""
图像转为8*8像素的小图,然后比对
适用于缩略图查找大图
"""
from PIL import Image
from PIL import ImageOps


def average(images, size):
    pixel = []
    cp = []

    for x in range(0, size[0]):
        for y in range(0, size[1]):
            pixel.append(images.getpixel((x, y)))

    avg = sum(pixel) / len(pixel)

    for px in pixel:
        if px > avg:
            cp.append(1)
        else:
            cp.append(0)

    return cp


def hamming(code1, code2):
    num = 0
    for index in range(0, len(code1)):
        if code1[index] != code2[index]:
            num += 1
    return num


def aHash(thumbnail, images):
    size = (8, 8)
    thumbnail = ImageOps.equalize(thumbnail.resize(size).convert('L'))
    images = ImageOps.equalize(images.resize(size).convert('L'))

    num = hamming(average(thumbnail, size), average(images, size))
    print(num)


aHash(Image.open('E:\Images\shan1.jpg'), Image.open('E:\Images\shan2.jpg'))
