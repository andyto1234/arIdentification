# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# # plt.style.use('classic')
# #############################################################
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
# from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
# #from keras import backend as K
# ####################################################
import os
# import cv2
# from PIL import Image
# import numpy as np


# Web download requirements
###################################################
import urllib.request
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import multiprocessing as mp



link = 'https://stereo.gsfc.nasa.gov/beacon/latest_256/ahead_euvi_171_latest.jpg'
link = 'https://stereo.gsfc.nasa.gov/beacon/latest_256/ahead_euvi_171_latest.jpg'

image_directory = '/Users/ato/scripts/python_code/arIdentification/data/training_171/'
ar_images = os.listdir(image_directory + 'AR/')
noar_images = os.listdir(image_directory + 'noAR/')
# for i, imageName in enumerate(ar_images):
#         try:
#                 timing = imageName.split('.')[0]
#                 date = timing[0:8]
#                 stereo195 = "https://stereo.gsfc.nasa.gov/browse//"+date[0:4]+"/"+date[4:6]+'/'+date[6:8]+"/ahead/euvi/195/256/"+date+'_000530_n4euA_195.jpg'
#                 print(stereo195)
#                 filename = "/Users/ato/scripts/python_code/arIdentification/data/training_195/AR/"+date+'_000530_n4euA_195.jpg'
#                 urllib.request.urlretrieve(stereo195, filename=filename)
#         except:
#                 continue

from datetime import datetime, timedelta

date1 = datetime(day=1, month=1, year=2007)
date2 = datetime(day=31, month=12, year=2007)

timediff = date2 - date1
print(timediff.days)



def fetch(diff):
        try:
                fetchDate = date1 + timedelta(days = diff)
                stereo195 = "https://stereo.gsfc.nasa.gov/browse//"+str(fetchDate.year)+"/"+str(f'{fetchDate.month:02d}')+'/'+str(f'{fetchDate.day:02d}')+"/ahead/euvi/195/256/"+str(fetchDate.date()).replace('-', '')+'_000530_n4euA_195.jpg'
                print(stereo195)

                filename = "/Users/ato/scripts/python_code/arIdentification/data/training_195/dataFetch/"+str(fetchDate.date()).replace('-', '')+'_000530_n4euA_195.jpg'
                urllib.request.urlretrieve(stereo195, filename=filename)
        except:
                print(fetchDate)
        # try:
        #         timing = imageName.split('.')[0]
        #         date = timing[0:7]
        #         stereo195 = "https://stereo.gsfc.nasa.gov/browse//"+date[0:4]+"/"+date[4:6]+'/'+date[6:8]+"/ahead/euvi/195/256/"+date+'_000530_n4euA_195.jpg'
        #         filename = "/Users/ato/scripts/python_code/arIdentification/data/training_195/noAR/"+date+'_000530_n4euA_195.jpg'
        #         urllib.request.urlretrieve(stereo195, filename=filename)
        # except:
        #         continue
# today = date.today()

pool = mp.Pool(processes=4)

mylist = list(range(timediff.days))
pool.map(fetch, mylist)