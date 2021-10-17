import cv2
import pytesseract

from config import LOG

try:
    from PIL import Image
except ImportError:
    import Image
    
    
class text_recognition:
    
    def __init__(self, lang = None):
        self.lang = lang
        
    def get_text(self,img):
        LOG.logger.info("<<<< Start Text Recognition >>>>")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if self.lang is None:
            text = pytesseract.image_to_string(Image.fromarray(img), config='--psm 1')
        else:
            text = pytesseract.image_to_string(Image.fromarray(img), config='--psm 1', lang = self.lang)
        return text
