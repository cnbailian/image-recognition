"""
tesseract

也不能识别 费用
还是要自己实现一个简单的啊
"""
import pytesseract
from PIL import Image

img = Image.open("./Images/sj3.jpg")
text = pytesseract.image_to_string(img)
print(text)
