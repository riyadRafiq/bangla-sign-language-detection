import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

## Make canvas and set the color
img = np.zeros((200,400,3),np.uint8)
b,g,r,a = 255,255,255,0




## Use simsum.ttc to write Chinese.
fontpath = "./fonts/SolaimanLipi_22-02-2012.ttf" # <== 这里是宋体路径 
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 80),  "আশীর্বাদ", font = font, fill = (b, g, r, a))
img = np.array(img_pil)

cv2.imshow("res", img);cv2.waitKey();cv2.destroyAllWindows()

