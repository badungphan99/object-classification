from AstraCamera.CameraManager import *

if __name__ == "__main__":

    astra = Astra("/home/dungpb/OpenNI-Linux-x64-2.3/Redist")
    astra.colorStream("/home/dungpb/Dropbox/Dev/classificationObject/ColorImage/")
    # astra.depthStream()
