"""
转为黑白图片识别相似图片
附带一个局部匹配加权
"""
import cv2


def monochrome(image, size):
    # 读取图像,转为灰度
    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    # 缩小图像尺寸
    image = cv2.resize(image, size)
    # threshold 转为黑白 使用 OTSU 算法
    (T, thresh) = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
    return thresh


# 遍历为一维列表 0黑 255白
def average(image):
    cp = []
    size = image.shape
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            pixel = image[x, y]
            cp.append(pixel)
    return cp


# 计算汉明距离 值越大表示差别越大
def hamming(code1, code2):
    num = 0
    for index in range(0, len(code1)):
        if code1[index] != code2[index]:
            num += 1
    return num / len(code1)


def segmentation(image, size):
    # 总数
    total = size[0]
    # 中值
    median = int((total / 2))
    # 主体外边距
    margin = int(median / 2)
    # 定义存储字典
    data = dict()
    # 左上区
    data['ul'] = image[0:median, 0:median]
    # 左下区
    data['ll'] = image[median:, 0:median]
    # 右上区
    data['ur'] = image[0:median, median:]
    # 右下区
    data['lr'] = image[median:, median:]
    # 主体区
    data['body'] = image[margin:total - margin, margin:total - margin]
    return data


def score(originally, contrasts):
    # 四块区: 左上, 左下, 右上, 右下 汉明距离小于10%,增加20%
    four = ['ul', 'll', 'ur', 'lr']
    # 主体区 汉明距离小于10%,增加30%
    body = 'body'
    # 加权初始化
    weighting = 0
    for x in originally:
        ham = hamming(average(originally[x]), average(contrasts[x]))
        if x in four:
            if ham <= 0.1:
                weighting += 0.2
        if x == body:
            if ham <= 0.1:
                weighting += 0.3

    return weighting


def features(originally, contrasts):
    size = (50, 50)
    ori_mon = monochrome(originally, size)
    con_mon = monochrome(contrasts, size)
    cv2.imshow('img1', ori_mon)
    cv2.imshow('img2', con_mon)
    cv2.waitKey(0)
    originally = average(ori_mon)
    contrasts = average(con_mon)
    result = hamming(originally, contrasts)
    print("加权前汉明距离:" + str(result))
    # 如果汉明距离超过20% 则进行分块评分
    if result > 0.2:
        ori_seg = segmentation(ori_mon, size)
        con_seg = segmentation(con_mon, size)
        result -= score(ori_seg, con_seg)
        print("加权汉明距离:" + str(score(ori_seg, con_seg)))
    # 综合评定 如果汉明距离小于20%,则认定为相似
    if result <= 0.2:
        print("汉明距离为" + str(result) + " 判定结果为:相似图片")
    else:
        print("汉明距离为" + str(result) + " 判定结果为:不是相似图片")


features('./Images/box_img1.png', './Images/box_img2.png')
