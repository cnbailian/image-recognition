"""
寻找轮廓极值的例子
"""
import imutils
import cv2

# 载入图片，将格式转换为灰阶图像,并做轻微模糊化
image = cv2.imread("./Images/hand.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# 二值化图像，然后进行腐蚀扩张，以去除噪点
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)

# 在二值化图片中寻找轮廓，然后抓取最大的一个
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 判断当前openCV环境
contours = contours[0] if imutils.is_cv2() else contours[1]
c = max(contours, key=cv2.contourArea)

# 沿着轮廓确定更多的极值点
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

# 画出对象的外轮廓，然后画出极值点，左点使用红色，右点使用绿色，上点是蓝色，下点是兰绿色
cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
cv2.circle(image, extLeft, 8, (0, 0, 255), -1)
cv2.circle(image, extRight, 8, (0, 255, 0), -1)
cv2.circle(image, extTop, 8, (255, 0, 0), -1)
cv2.circle(image, extBot, 8, (255, 255, 0), -1)

# 输出显示image
cv2.imshow("Image", image)
cv2.waitKey(0)
