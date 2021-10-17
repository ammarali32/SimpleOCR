import glob
import os

import cv2
import imageio
import imgaug as ia
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from imgaug import augmenters as iaa
from tensorflow.keras import backend as kb
from tensorflow.keras import regularizers
from tensorflow.keras.callbacks import (EarlyStopping, LearningRateScheduler,
                                        ModelCheckpoint)
from tensorflow.keras.layers import (Activation, BatchNormalization, Conv2D,
                                     Dense, Dropout, Flatten, Input, LeakyReLU,
                                     MaxPooling2D, UpSampling2D)
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import image

from config import CFG

# Simple Model for removing noise from images (waterMarks, old papers and others)
# This Model was Train on The Data from Kaggle https://www.kaggle.com/c/denoising-dirty-documents

class denoisingModel:
    def __init__(self):
        input_layer = Input(shape=(None,None,1))
        # encoder
        e = Conv2D(32, (3, 3), padding='same')(input_layer)
        e = LeakyReLU(alpha=0.3)(e)
        e = BatchNormalization()(e)
        e = Conv2D(64, (3, 3), padding='same')(e)
        e = LeakyReLU(alpha=0.3)(e)
        e = BatchNormalization()(e)
        e = Conv2D(64, (3, 3), padding='same')(e)
        e = LeakyReLU(alpha=0.3)(e)
        e = MaxPooling2D((2, 2), padding='same')(e)
        # decoder
        d = Conv2D(64, (3, 3), padding='same')(e)
        d = LeakyReLU(alpha=0.3)(d)
        d = BatchNormalization()(d)
        d = Conv2D(64, (3, 3), padding='same')(d)
        d = LeakyReLU(alpha=0.3)(d)
        d = UpSampling2D((2, 2))(d)
        d = Conv2D(32, (3, 3), padding='same')(d)
        d = LeakyReLU(alpha=0.2)(d)
        output_layer = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(d)
        self.model = Model(input_layer,output_layer)

    def forward(self,bsb):
        gray_image = cv2.cvtColor(bsb, cv2.COLOR_RGB2GRAY) /255.0
        x,y = gray_image.shape
        gpred = self.model.predict(gray_image.reshape(1,x,y,1))
        _,x2,y2,_ = gpred.shape
        gpred = gpred.reshape(x2,y2)
        res =cv2.convertScaleAbs(gpred, alpha=(255.0))
        for i in range(res.shape[0]):
                for j in range(res.shape[1]):
                    if res[i][j] < 200:
                        res[i][j] = 0
                    else:
                        res[i][j]= 255
        return cv2.cvtColor(res, cv2.COLOR_GRAY2BGR)
    
    def load_weights(self,weights_path):
        self.model.load_weights(weights_path)

