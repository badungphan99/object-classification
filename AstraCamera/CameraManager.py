import cv2
import numpy as np
from openni import openni2
from openni import _openni2 as c_api
import datetime


class Astra:

    def __init__(self, path: str):
        openni2.initialize(dll_directories= path)
        self.dev = openni2.Device.open_any()

    def depthStream(self):
        depth_stream = self.dev.create_depth_stream()
        depth_stream.start()
        depth_stream.set_video_mode( c_api.OniVideoMode(pixelFormat=c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM,
                                                        resolutionX=640, resolutionY=480, fps=30))

        while True:
            # Grab a new depth frame
            frame = depth_stream.read_frame()
            frame_data = frame.get_buffer_as_uint16()
            # Put the depth frame into a numpy array and reshape it
            img = np.frombuffer(frame_data, dtype=np.uint16)
            img.shape = (1, 480, 640)
            img = np.concatenate((img, img, img), axis=0)
            img = np.swapaxes(img, 0, 2)
            img = np.swapaxes(img, 0, 1)

            # Display the reshaped depth frame using OpenCV
            cv2.imshow("Depth Image", img)
            key = cv2.waitKey(1) & 0xFF

            # If the 'c' key is pressed, break the while loop
            if key == ord("q"):
                break

        # Close all windows and unload the depth device
        openni2.unload()
        cv2.destroyAllWindows()

    def colorStream(self, pathDir:str):
        color_stream = self.dev.create_color_stream()
        color_stream.start()
        color_stream.set_video_mode( c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = 640,
                                                        resolutionY = 480, fps = 30))

        while True:
            frame = color_stream.read_frame()
            frame_data = frame.get_buffer_as_uint8()

            img = np.frombuffer(frame_data, dtype=np.uint8)
            img.shape = (307200, 3)
            b = img[:, 0].reshape(480, 640)
            g = img[:, 1].reshape(480, 640)
            r = img[:, 2].reshape(480, 640)

            rgb = (r[..., np.newaxis], g[..., np.newaxis], b[..., np.newaxis])
            img = np.concatenate(rgb, axis=-1)

            cv2.imshow("Color Image", img)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

            if key == ord("c"):
                filename = pathDir +  str(datetime.datetime.now()) + ".png"
                cv2.imwrite(filename, img)

        openni2.unload()
        cv2.destroyAllWindows()

