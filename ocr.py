"""
pyocr 库 实践

实践后发现不能识别法力水晶中数字
"""
from pyocr import pyocr
from PIL import Image

tools = pyocr.get_available_tools()[:]

print(tools[0].image_to_string(Image.open('./Images/7364.png'), lang='eng'))
print(tools[0].image_to_string(Image.open('./Images/jiguanghoverli.png'), lang='eng'))
print(tools[0].image_to_string(Image.open('./Images/sj3.jpg'), lang='eng'))
