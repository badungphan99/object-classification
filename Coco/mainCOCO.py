from Coco.GetCocoData import *
from Coco.StatisticalData import *
from Coco.SelectData import *
from collections import Counter

def writeLog(log:str):
    if os.path.isfile('log.txt'):
        file = open('log.txt', 'a')
        file.write(log+'\n')
        file.close()
    else:
        file = open('log.txt', 'w')
        file.write(log + '\n')
        file.close()

def cropImage():

    pathAnnotationFile = '/home/dungpb/DataTranning/annotations_trainval2014/annotations/instances_train2014.json'
    category = ['bicycle', 'car', 'motorcycle', 'bus', 'train', 'truck', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'cat', 'dog', 'person']
    pathDirImage = '/home/dungpb/DataTraining/train2014/'
    pathDesDir = '/home/dungpb/DataTraining/crop_train2014/'

    for cat in category:
        count = 0
        pathDesDirCat = pathDesDir + cat + '/'
        if os.path.isdir(pathDesDirCat):
            writeLog("File %s exists" % pathDesDirCat)
        else:
            try:
                os.mkdir(pathDesDirCat)
            except OSError:
                writeLog("Creation of the directory %s failed" % pathDesDirCat)
            else:
                writeLog("Successfully created the directory %s " % pathDesDirCat)

        img_error = []

        coco = GetCocoData(pathAnnotationFile, cat, pathDirImage)

        imgIds = coco.getDetailImage()

        numImg = len(imgIds)

        print('______', cat, '______')

        writeLog('______'+cat+'______')

        for i in range(numImg):

            img, imgDet = coco.getImage(i)

            anns = coco.getAnnIds(imgDet)

            print(cat, ' :cropped ', i, ' image of ', numImg, 'images')
            writeLog(cat + ' :cropped '+ str(i) + ' image of '+ str(numImg) + ' images')

            for j in range(len(anns)):

                imgFileName = pathDesDirCat + imgDet['file_name'].split('.')[0]

                try:
                    imgFileName = imgFileName + '_' + str(j) + '.png'

                    mask = coco.getMask(anns, j)

                    crop_img = coco.cropImageWithMask(img, mask)

                    cv2.imwrite(imgFileName, crop_img)

                    count += 1

                except:
                    img_error.append(i)
                finally:
                    j += 1

        print(cat, ': id image error: ', img_error)
        writeLog('number image write success: ' + str(count))
        writeLog(cat + ': id image error: '+ str(img_error))

def overviewData():

    pathDirImage = '/home/dungpb/Downloads/Data tranning/img_crop/car/'

    overviewData = StatisticalData(pathDirImage)

    overviewData.vTData(1000)

def mouseCropImg():
    pathDirImage = "../ColorImage/"
    desDir = "/home/dungpb/Dropbox/Dev/classificationObject/ColorImage/crop/"
    crop = SelectData(pathDirImage)
    crop.mouseCropImg(desDir)
def sizeCropImg():
    category = ['car/', 'motorcycle/', 'train/', 'truck/', 'traffic light/', 'fire hydrant/', 'stop sign/',
                'parking meter/', 'cat/', 'dog/', 'person/']

    srcDir = "/home/dungpb/DataTraining/crop_train2014/"
    desDir = "/home/dungpb/DataTraining/data_train2014/"

    for i in category:
        os.mkdir(desDir + i)
        desDirResize = desDir + i + "selected/"
        os.mkdir(desDirResize)
        desDirSkip = desDir + i + "skip/"
        os.mkdir(desDirSkip)
        crop = SelectData("/home/dungpb/DataTraining/crop_train2014/" + i)
        crop.sizeCropImg(3000, 100000, desDirResize, desDirSkip)

def showSize():
    statiscal = StatisticalData('/home/dungpb/Dropbox/Dev/classificationObject/ColorImage/crop/')
    statiscal.getSize()

if __name__ == "__main__":
    sizeCropImg()