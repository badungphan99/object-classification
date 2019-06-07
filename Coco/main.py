from Coco.GetCocoData import *
from Coco.OverviewData import *
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

    pathAnnotationFile = '/home/dungpb/Downloads/Data tranning/annotations_trainval2014/annotations/instances_train2014.json'
    category = ['bicycle', 'car', 'motorcycle', 'bus', 'train', 'truck', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'cat', 'dog', 'person']
    pathDirImage = '/home/dungpb/Downloads/Data tranning/train2014/'
    pathDesDir = '/home/dungpb/Downloads/Data tranning/img_crop/'

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

    pathDirImage = ('/home/dungpb/Downloads/Data tranning/car/')

    overviewData = OverviewData(pathDirImage)

    overviewData.vTData(20)

def testCropImage():

    pathAnnotationFile = '/home/dungpb/Downloads/Data tranning/annotations_trainval2014/annotations/instances_train2014.json'
    category = 'car'
    pathDirImage = '/home/dungpb/Downloads/Data tranning/train2014/'

    coco = GetCocoData(pathAnnotationFile, category, pathDirImage)

    imgIds = coco.getDetailImage()

    img, imgDet = coco.getImage(3761)
    cv2.imshow('img', img)

    anns = coco.getAnnIds(imgDet)

    mask = coco.getMask(anns, 0)
    cv2.imshow('mask', mask)

    crop_img = coco.cropImageWithMask(img, mask)

    cv2.imshow('show', crop_img)
    cv2.imshow('mask', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def test():
    a = [25, 1, 1, 0, 0, 2, 3, 7, 7, 23]



    counter = Counter(a)

    print(counter)

if __name__ == "__main__":

    cropImage()
