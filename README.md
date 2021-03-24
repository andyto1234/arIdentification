# Solar Active Region Identification

This project involves three key ingredients, and it's constructed with two codes with two different tools (Not sure why I did that... D:):

- Training (mainTraining.ipynb)
- Predicting and Sending e-mails (main.py)

## Training

The training code is writting using Jupyter Notebook (mainTraining.ipynb). You will need a folder called data to put all your training data.

## Predicting

The CNN model I use for the daily AR prediction is provided in the models folder. Simply replace it with your model if needed:D

I have configured the model to read image from a folder called latest_images. You can input any STEREO-A 195 image (256x256) and get a prediction out of it!

## Sending e-mails

The last part of the code involves fetching the latest image everyday and sending it to the mailing list. You will need an .env file to read your email, password, and mailing list in order for it to work.

## Set-up

```
python main.py
```