import os
import re

import cv2
import neuspell
import numpy as np
from neuspell import SclstmChecker

from config import LOG


class PostProcessor:
    
    def __init__(self, CFG):
        self.CHARS = CFG.chars
    # remove emplty lines from the txt recognized by Tesseract 
    def removeEmptyLines(self, txt):
        LOG.logger.info("<<<< Removing Empty Lines >>>>")
        lines = txt.split('\n')
        non_empty_lines = [line for line in lines if line.strip() != ""]
        string_without_empty_lines = ""
        for line in non_empty_lines:
            string_without_empty_lines += line.replace('\n', '').replace('\r', '').replace('\n+e', '') + "\n"
        return string_without_empty_lines
    # Remove Undefined Characters, replacing @ by a and
    # replacing some characters with .
    def cleanText(self, txt):
        LOG.logger.info("<<<< Cleaning Text >>>>")
        txt = re.sub(self.CHARS, ' ', txt)
        txt2 = ''
        for idx, i in enumerate(txt):
            if i == '@':
                txt2+= 'a'
                continue
            if idx < 4:
                txt2 += i
                continue
            if txt2[idx-4:idx] == '....' and txt[idx] != '.' and txt[idx] != ' ':
                txt2 += '.'
            else:
                txt2 += i
        return txt2
    # Use Bert checker to fix spelling errors see https://github.com/neuspell/neuspell
    def spellingCheck(self, txt):
        LOG.logger.info("<<<< Check Spelling Using Bert >>>>")
        checker = SclstmChecker()
        checker = checker.add_("bert", at="output")  # "elmo" or "bert", "input" or "output"
        checker.from_pretrained()
        return checker.correct(txt)

    def postprocess(self, txt):
        LOG.logger.info("<<<< Start Postprocessing >>>>")
        txt = self.removeEmptyLines(txt)
        txt = self.cleanText(txt)
        #txt = self.spellingCheck(txt)
        return txt
    
        