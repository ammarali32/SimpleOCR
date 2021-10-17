import os

import cv2
import numpy as np

from config import LOG
from denoise_photos_nn import denoisingModel


class PreProcessor:
    
    def __init__(self,CFG):
        self.DModel = denoisingModel()
        self.DModel.load_weights(CFG.encoder_decoder_weights)
    # Adjust image in case it was rotated a little 
    def fixRotation(self,img):
        LOG.logger.info("<<<< Fixing Image Rotation>>>>")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (h, w) = img.shape[:2]
        gray = cv2.bitwise_not(gray)
        thresh = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        coords = np.column_stack(np.where(thresh > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(img, M, (w, h),
        flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated
    # If there are multiple colors in the image not close to black and white use the denoising model
    # This is inefficient method to choose if to use or not the best solution is a simple binary classifier
    # Binarize the image by making the values 0 ot 255
    def denoiseAndBinarize(self,img):
        original_img = img.copy()
        num_dark_pixels = len(np.argwhere(original_img <= (50,50,50)))
        num_light_pixels = len(np.argwhere(original_img > (200,200,200)))
        if num_dark_pixels + num_light_pixels < 0.95 *  original_img.shape[0] * original_img.shape[1] * original_img.shape[2]:
            img = self.DModel.forward(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            LOG.logger.info("<<<< Denoising Image >>>>")
        else:
            img =  cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    if img[i][j] < 160:
                        img[i][j] = 0
                    else:
                        img[i][j]= 255
            LOG.logger.info("<<<< Binarizing Image >>>>")
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        return img
    
    # In case there were lines in the text image, we need to remove them
    def removeLines(self, image):
        LOG.logger.info("<<<< Removing Lines >>>>")
        result = image.copy()
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # Remove horizontal lines
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20,1))
        remove_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
        cnts = cv2.findContours(remove_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            cv2.drawContours(result, [c], -1, (255,255,255), 1)
        vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,20))
        remove_vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
        cnts = cv2.findContours(remove_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            cv2.drawContours(result, [c], -1, (255,255,255), 1)
        return result
    
    def preprocess(self, img):
        LOG.logger.info("<<<< Start Preprocessing >>>>")
        original_img = img.copy()
        img = self.removeLines(img)
        img = self.denoiseAndBinarize(img)
        img = self.fixRotation(img)       
        return img, original_img

    