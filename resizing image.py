from PIL import Image
import os
import glob
import numpy as np
#import matplotlib.pylab as plt

path = "D:\AI\Images"
dirs = os.listdir( path )

def resize():
    marr = np.zeros([20,200,200,3])
    i = 0
    for filename in glob.iglob(path + '**/*.jpg', recursive=True):
        print(filename)
        print("Resizing...")
        im = Image.open(filename)
        #%matplotlib inline
        #im1 = plt.imread(filename)
        #print("current shape: "im1.shape)
        f, e = os.path.splitext(path+filename)
        imResize = im.resize((200,200), Image.ANTIALIAS)
        imResize.save(filename , 'JPEG', quality=90)
        print("Completed...")
        #im2 = plt.imread(filename)
        #print("Resized Shape: "im2.shape)
        marr[i] = imResize
        print(marr)
        i += 1

resize()