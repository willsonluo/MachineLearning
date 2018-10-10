# -*-coding:utf-8-*-
from PIL import Image
import cv2
import os
import time
# img = Image.open('yzm_data'+ os.sep + '1538183310741170.jpg')


def clean(image_clean):
    img = cv2.imread(image_clean, 0)  # 直接读为灰度图像
    ret, thresh1 = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY)
    cv2.imwrite(image_clean, thresh1)


img_list = os.listdir('yzm_data')
for abc in range(len(img_list)):
    clean('yzm_data' + os.sep + img_list[abc])
    img = Image.open('yzm_data'+ os.sep + img_list[abc])
    im = img.convert("L")
    a = np.array(im)
    pd.DataFrame(a.sum(axis=0)).plot.line() # 画出每列的像素累计值
    plt.imshow(a,cmap='gray') # 画出图像


   # 核心代码，注意调整要切割的线
    split_lines = [4,20,32,46,60]
    vlines = [plt.axvline(i, color='r') for i in split_lines] # 画出分割线
    plt.show()
    y_min=1
    y_max=23
    ims=[]
   # c=1
    for x_min,x_max in zip(split_lines[:-1],split_lines[1:]):
       im.crop([x_min,y_min,x_max,y_max] ).save('yzm_test'+os.sep + '000_%s.jpeg' % (int(time.time() * 1000000)), 'jpeg') # (str(c)+'.jpeg')
       # crop()函数是截取指定图像！
       # save保存图像！
       # c=c+1
    #for i in range(1,5):
    #   file_name="{}.jpeg".format(i)
    #   plt.subplot(8,3,i)
    #   im=Image.open(file_name).convert("1")
    #   #im=img.filter(ImageFilter.MedianFilter(size=3))
    #   plt.imshow(im)
    #   # 显示截取的图像！
    # plt.show()