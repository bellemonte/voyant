#! /bin/python

import argparse
import datetime

from picamera import PiCamera
from time import sleep

AP = argparse.ArgumentParser()
AP.add_argument("-l", "--length", help="Video clip length in seconds.")
AP.add_argument("-p", "--path", default="/tmp/", help="Video clip path.")
ARGS = vars(AP.parse_args())

def main():
    camera = PiCamera()

    while True:
        # camera.start_preview()
        path = ARGS.get("path", "/tmp/") + str(datetime.datetime.now()) + ".h264"
        camera.start_recording(path)
        sleep(ARGS.get("length", 10))
        camera.stop_recording()
        # camera.stop_preview()

if __name__ == "__main__":
    main()
