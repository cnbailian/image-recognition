"""
定位例子2
根据轮廓定位答题卡已答题部分
笨方法 有待优化
"""
import imutils
import cv2


def loc(images, cns):
    # 左上
    left = tuple(cns[cns[:, :, 0].argmin()][0])
    # 右下
    right = tuple(cns[cns[:, :, 0].argmax()][0])
    # 右上
    top = tuple(cns[cns[:, :, 1].argmin()][0])
    # 左下
    bot = tuple(cns[cns[:, :, 1].argmax()][0])

    # 开始行数 选择左上与右上中最小的Y轴
    sh = min(left[1], top[1])
    # 结束行数 左下与右下中最大的Y轴
    eh = max(bot[1], right[1])
    # 开始列数 左上与左下中最小的x轴
    sl = min(left[0], bot[0])
    # 结束列数 右上与右下中最大的x轴
    el = max(top[0], right[0])

    # 取出轮廓
    return images[sh:eh, sl:el]


# 判断是否为涂写
def scrawl(data):
    black = 0
    white = 0
    for i in data:
        for val in i:
            if val == 255:
                white += 1
            else:
                black += 1
    return black / (black + white)


# 读取
img = cv2.imread('./Images/card.png')
# 转为灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 高斯模糊
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# 边缘检测
edged = cv2.Canny(blurred, 75, 200)

# 大津法 二值化
thresh = cv2.threshold(edged, 0, 255, cv2.THRESH_OTSU)[1]
# 二值化没有边缘检测过的图片
thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]

# 从边缘图中寻找轮廓，然后初始化答题卡对应的轮廓
contours = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if imutils.is_cv2() else contours[1]

# 对每一个轮廓进行循环处理
for c in contours:
    # 计算轮廓的边界框，然后利用边界框数据计算宽高比
    (x, y, w, h) = cv2.boundingRect(c)
    ar = w / float(h)
    # 为了辨别一个轮廓是一个气泡，要求它的边界框不能太小，在这里边至少是20个像素，而且它的宽高比要近似于1
    if w >= 20 and h >= 20 and 1.1 >= ar >= 0.9:
        images = loc(thresh1, c)
        value = scrawl(images)
        if value > 0.4:
            cv2.imshow("Image" + str(value), loc(img, c))

cv2.waitKey(0)
