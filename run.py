import click
import cv2
import numpy as np

import io_txt
from config import CFG, LOG
from postprocess import PostProcessor
from preprocess import PreProcessor
from text_recognition import text_recognition


@click.command()
@click.option('--input', prompt='Input_directory',default='./test.pdf', help='Path to the input file')
@click.option('--output', prompt='Output_directory',default='./output.text',
              help='Path to the output file')
@click.option('--verbose', count=True,
              help='Output detailed logs')

def run(input,output,verbose):
    imgs = io_txt.read_file(input)
    texts =[]
    
    if verbose == 0:
        LOG.logger.disabled = True
    pre = PreProcessor(CFG)
    tesser = text_recognition(lang = 'eng')
    post = PostProcessor(CFG)
    for i in imgs:
        image, _ = pre.preprocess(i)
        txt = tesser.get_text(image)
        txt = post.postprocess(txt)
        texts.append(txt)
    io_txt.write_file(output, texts)
if __name__ == '__main__':
    run()