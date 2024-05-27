from fileinput import filename
import logging
import os
import cv2
import numpy as np

from utils import Args, get_absolute_filepaths


def run_script(args: Args):
    logging.basicConfig(level=args.loglevel)
    qcd = cv2.QRCodeDetector()
    result = []

    files = get_absolute_filepaths(args.input_directory)
    for file in files:
        img = cv2.imread(file)

        if img is None:
            logging.warn(f"{file} is not a valid image, Igonred.")
            continue

        is_qr_present, decoded_info = [False, []]
        try:
            is_qr_present, decoded_info, _, _ = qcd.detectAndDecodeMulti(img)
        except Exception as e:
            logging.warn(
                f"{file} couldn't be processesed by the opencv2 qr code detector.")

        if not is_qr_present:
            logging.warn(f"{file} doesn't contain a QR code.")
            continue

        print(is_qr_present, decoded_info)

        for txt in decoded_info:
            if len(txt) is not 0:
                result.append(txt)
    
    args.output_file.write('\n'.join(result))
