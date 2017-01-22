"""
根据轮廓极值截取出轮廓例子
"""
import imutils
import cv2


img = cv2.imread('./Images/hand.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

# 在二值化图片中寻找轮廓，然后抓取最大的一个
contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 判断当前openCV环境
contours = contours[0] if imutils.is_cv2() else contours[1]
# 神奇
c = max(contours, key=cv2.contourArea)

# RGB存储为三维矩阵  灰度图像存储为二维矩阵
# 矩阵其中的2个维度是用来表示图片上的各个的像素点，说的通俗点，就是形成平面。 x y
# 另一个维度是用来表示RGB（红绿蓝）各个色 的分量。 三个值为 r g b
# 而灰度图片的RGB分量都是等值的，所以灰度图片的数据可以简化成二维矩阵。 rgb相等 [42, 42, 42] == 42
# print(img)
# print(gray)

# 那么问题来了,轮廓为什么是三维的 有一个维度表示 x y ,其他的表示什么呢

# 沿着轮廓确定更多的极值点
# 左上
extLeft = tuple(c[c[:, :, 0].argmin()][0])
# 右下
extRight = tuple(c[c[:, :, 0].argmax()][0])
# 右上
extTop = tuple(c[c[:, :, 1].argmin()][0])
# 左下
extBot = tuple(c[c[:, :, 1].argmax()][0])

# 开始行数 选择左上与右上中最小的Y轴
sH = min(extLeft[1], extTop[1])
# 结束行数 左下与右下中最大的Y轴
eH = max(extBot[1], extRight[1])
# 开始列数 左上与左下中最小的x轴
sL = min(extLeft[0], extBot[0])
# 结束列数 右上与右下中最大的x轴
eL = max(extTop[0], extRight[0])

# 取出轮廓
img = img[sH:eH, sL:eL]

# 输出显示image
# cv2.imshow("Image", img)
# cv2.waitKey(0)
