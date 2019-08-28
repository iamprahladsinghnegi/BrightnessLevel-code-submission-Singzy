#Importing packeges
import os
import sys
import math
import numpy as np
import cv2
from PIL import Image, ImageStat




'''defining functions to calculate brightness'''

# method 1

# Convert image to greyscale, return average pixel brightness
def get_brightness_method1( im_file ):
    im = Image.open(im_file).convert('L')
    stat = ImageStat.Stat(im)
    mean_bright = stat.mean[0]
    ans = get_brightness(mean_bright)
    return ans



# method 2

# Convert image to greyscale, return RMS pixel brightness
def get_brightness_method2( im_file ):
    im = Image.open(im_file).convert('L')
    stat = ImageStat.Stat(im)
    rms_bright = stat.rms[0]
    #print(rms_bright)
    ans = get_brightness(rms_bright)
    return ans



#method 3

# Average pixels, then transform to perceived brightness
def get_brightness_method3( im_file ):
    im = Image.open(im_file)
    stat = ImageStat.Stat(im)
    r,g,b = stat.mean
    mean_bright = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    ans = get_brightness(mean_bright)
    return ans



# method 4

# RMS of pixels, then transform to perceived brightness
def get_brightness_method4( im_file ):
    im = Image.open(im_file)
    stat = ImageStat.Stat(im)
    r,g,b = stat.rms
    rms_bright = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    ans = get_brightness(rms_bright)
    return ans



# method 5

# Calculate perceived brightness of pixels, then return average.
def get_brightness_method5( im_file ):
    im = Image.open(im_file)
    stat = ImageStat.Stat(im)
    gs = (math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)) 
         for r,g,b in im.getdata())
    avg_bright = sum(gs)/stat.count[0]
    ans = get_brightness(avg_bright)
    return ans




# method 6

# average pixel brightness
def get_brightness_method6( im_file ):
    img = cv2.imread(im_file, 1)
   # print("Image shape : ", img.shape)
    while img.size > 777600 *3:
      #  print("resizing image")
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
      #  print("Image shape : ", img.shape)
    R = B = G = 0
    pixel = 0
    summ = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixel +=1
            B += img[i][j][0]
            G += img[i][j][1]
            R += img[i][j][2]
            #summ += (B+G+R)/3

    #print(B, G, R)
    summ = B + G + R
    #print(summ)
    total_pixel = 3 * img.shape[0] * img.shape[1]
    #print(total_pixel)
    avg_bright = summ / total_pixel
    #print(brightness)
    ans = get_brightness(avg_bright)
    return ans




# function to get brightness leve
def get_brightness_level(avg_b):
    if avg_b > 231.8179:
        return 10
    elif avg_b > 208.6362:
        return 9
    elif avg_b > 185.4544:
        return 8
    elif avg_b > 162.27259:
        return 7
    elif avg_b > 139.0908:
        return 6
    elif avg_b > 115.9089:
        return 5
    elif avg_b > 92.7272:
        return 4
    elif avg_b > 69.5454:
        return 3
    elif avg_b > 46.3636:
        return 2
    elif avg_b > 23.1818:
        return 1
    else:
        return 0

def get_brightness(brightness):
    bright_level = get_brightness_level(brightness)
    print("bright_level : ", bright_level)
    return bright_level


def final_brightness_level(ls):
    return max(set(ls), key = ls.count)



    
if __name__ =="__main__":
    def_file = os.getcwd()+"\\test.jpg"
    file = str(sys.argv[1]) if len(sys.argv) > 1 else def_file
    ls = []
    print("Opening file :", file)
    print("***** Method1 *****")
    ls.append(get_brightness_method1(file))
    #print(ls[0])
    
    print("***** Method2 *****")
    ls.append(get_brightness_method2(file))
    #print(ls[1])
    
    
    print("***** Method3 *****")
    ls.append(get_brightness_method3(file))
    #print(ls[2])
    
    print("***** Method4 *****")
    ls.append(get_brightness_method4(file))
    #print(ls[3])
    
    print("***** Method5 *****")
    ls.append(get_brightness_method5(file))
    #print(ls[4])
    
    print("***** Method6 *****")
    ls.append(get_brightness_method6(file))
    #print(ls[5])
    
    #print(ls)
    ans = final_brightness_level(ls)
    print("Final Brightness Level is : ", ans)
