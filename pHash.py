# 失败,原因,不了解dct

import cv2
import numpy as np


def pHash(thumbnail, images):
    size = (32, 32)
    # thumbnail = thumbnail.resize(size).convert('L')
    # images = images.resize(size).convert('L')

    thumbnail = cv2.resize(thumbnail, size)
    rows, cols = thumbnail.shape[:2]

    # 获取某个块的值
    # y1 = cv2.medianBlur(thumbnail, 3)

    # 不明白为什么要转float32 还要除一下255.0
    # 但是不这样做的话,不能dct
    imf = np.float32(thumbnail) / 255.0
    # print(imf)

    trans = cv2.dct(imf)
    # print(trans)

    # 转换回去
    dct1 = np.uint8(trans) * 255

    print(dct1)

    # narrow = cv2.medianBlur(dct1, 3)


pHash(cv2.imread('./Images/box_img3.png', cv2.IMREAD_GRAYSCALE), cv2.imread('./Images/img2.png', cv2.IMREAD_GRAYSCALE))
