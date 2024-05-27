from fileinput import filename
import logging
import os
import cv2
import numpy as np

from utils import Args, get_absolute_filepaths


def run_script(args: Args):
    qcd = cv2.QRCodeDetector()

    files = get_absolute_filepaths(args.input_directory)
    for file in files:
        img = cv2.imread(file)

        if img is None:
            logging.info(f"{file} is not a valid image, Igonred.")
            continue
    
        # Threshhold the image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        cv2.imshow("img", thresh)
        cv2.waitKey(0)

        res = qcd.detectAndDecodeMulti(thresh)
        print(res)

