import time
from PIL import ImageGrab

time.sleep(5)

for i in range(10):
    img = ImageGrab.grab()
    img.save(r"C:\Users\lhs-DT\Downloads\image{}.png".format(i))
    time.sleep(2)
