from SIFT.Sift import *


def siftImg():
    sift = Sift('/home/dungpb/Dropbox/Dev/classificationObject/ColorImage/crop/')
    sift.siftImage()

def randomSiftImg():
    sift = Sift('/home/dungpb/DataTraining/data_train2014/dog/selected/')
    pathDir = '/home/dungpb/DataTraining/data_train2014/dog/descriptor/'
    sift.randomSiftImage(100, pathDir)

def test():
    sift = Sift('/home/dungpb/Dropbox/Dev/classificationObject/ColorImage/crop/')
    sift.descriptorSift()

if __name__ == "__main__":
    randomSiftImg()