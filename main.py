import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# plt.style.use('classic')
#############################################################
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import normalize
#from keras import backend as K
####################################################
import os
import cv2
from PIL import Image
import numpy as np

# Download the latest image
############################################################################
from datetime import date
import urllib.request
today = date.today()
d1 = today.strftime("%d_%m_%y")
url = "https://stereo.gsfc.nasa.gov/beacon/latest_256/ahead_euvi_195_latest.jpg"
filename = "/Users/ato/scripts/python_code/arIdentification/latest_images/"+d1+'.jpg'
urllib.request.urlretrieve(url, filename=filename)

# Read Image
##########################################################################
dataset= []
image = cv2.imread("/Users/ato/scripts/python_code/arIdentification/latest_images/"+d1+'.jpg')
image = Image.fromarray(image, 'RGB')
SIZE = 150
image = image.resize((SIZE, SIZE))
dataset.append(np.array(image))
dataset=np.array(dataset)
X_test = normalize(dataset, axis=1)
todayImage = X_test[0]


# Model Prediction
#############################################################################
model = load_model('/Users/ato/scripts/python_code/arIdentification/models/AR_model_40epochs_195_test_92_67.h5')
input_img = np.expand_dims(todayImage, axis=0)
prediction = model.predict(input_img)[0]*100
prediction = f'{prediction[0]:.2f}'
print("The prediction for this image is: ", prediction,"%")
# print(model.pre)

# Set email configuration
###############################################################
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
from dotenv import load_dotenv

load_dotenv()

recipient = os.environ.get("RECIPIENT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


def send_email(email_recipient, email_subject, email_message, attachment_location = ''):

    email_sender = f'{username}'

    msg = MIMEMultipart()

    for i in email_recipient:
        msg['From'] = email_sender
        msg['To'] = i
        msg['Subject'] = email_subject

        msg.attach(MIMEText(email_message, 'plain'))
        if attachment_location != '':
            filename = os.path.basename(attachment_location)
            attachment = open(attachment_location, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)
        try:
            server = smtplib.SMTP('smtp.office365.com', 587)
            server.ehlo()
            server.starttls()
            server.login(f'{username}', f'{password}')
            text = msg.as_string()
            server.sendmail(email_sender, email_recipient, text)
            print('email sent')
            server.quit()
        except:
            print("SMPT server connection error")
        return True

subject = "Daily STEREO-A Prediction: "+str(prediction) + "% of having a sunspot (" + today.strftime("%d/%m")+ ")"
attachmentLocation = "/Users/ato/scripts/python_code/arIdentification/latest_images/"+d1+'.jpg'
message = "Dear all,\n\nThanks for being the first people to try out our sunspot prediction bot!!\n\nThe bot has a 90% accuracy (1 in 10 will be false), so please don't rely on the percentage for important observations!:)\n\nAlso, do give me a shout if you can think of any new features!!\n\nUpdate v2.1: You can now find my code in https://github.com/andyto1234/arIdentification! Have a great day:D\n\nBest wishes,\nAndy\n"
recipients = [k for k in recipient.split(",")]
send_email(recipients, subject, message, attachment_location = attachmentLocation)