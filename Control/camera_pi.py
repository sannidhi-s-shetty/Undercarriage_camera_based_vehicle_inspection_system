#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  camera_pi.py
#
#
#
import time
import io
import threading
# import picamera

import cv2


class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(cls):
        # with picamera.PiCamera() as camera:
        with cv2.VideoCapture(0) as camera:
            # camera setup
            camera.resolution = (320, 240)
            camera.hflip = True
            camera.vflip = True

            # let camera warm up
            camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # store frame
                stream.seek(0)
                cls.frame = stream.read()
                # to record

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                if time.time() - cls.last_access > 10:
                    break
        cls.thread = None
# ----------------------------------------------------------------------------------------------------------------------
#
# # this is for laptop camera
# import cv2
# import numpy as np
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
#

# class Camera(object):
#     def __init__(self):
#         self.video = cap
#
#     def __del__(self):
#         self.video.release()
#
#     def ret_frame(self):
#         ret,frame = self.video.read()
#         return ret,frame
#
#     def get_frame(self):
#         ret, frame = self.ret_frame()
#         self.record()
#         # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
#
#         ret, jpeg = cv2.imencode('.jpg', frame)
#
#         return jpeg.tobytes()
# # -----------------------------------------------------------------------------------------------------------------------
#     def record(self):
#         fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#         size = (int(self.video.get(3)), int(self.video.get(4)))
#         out = cv2.VideoWriter('output.avi', fourcc, 20.0, size)
#         while True:
#             ret,frame = self.video.read()
#             hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#             out.write(frame)
#             # time.sleep(5)
#             # cv2.imshow('Original', frame)
#             cv2.imshow('frame', hsv)
#             # Wait for 'a' key to stop the program
#             if cv2.waitKey(1) & 0xFF == ord('a'):
#                 # Close the window / Release webcam
#                 self.video.release()
#
#                 # After we release our webcam, we also release the output
#                 out.release()
#
#                 # De-allocate any associated memory usage
#                 cv2.destroyAllWindows()
#     #



