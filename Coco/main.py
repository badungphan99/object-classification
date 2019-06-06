from Coco.GetCocoData import *
from Coco.OverviewData import *
from collections import Counter


def cropImage():

    pathAnnotationFile = '/home/dungpb/Downloads/Data tranning/annotations_trainval2014/annotations/instances_train2014.json'
    category = 'car'
    pathDirImage = '/home/dungpb/Downloads/Data tranning/train2014/'
    pathDesDir = '/home/dungpb/Downloads/Data tranning/car/'

    img_error = []

    coco = GetCocoData(pathAnnotationFile, category, pathDirImage)

    imgIds = coco.getDetailImage()

    numImg = len(imgIds)

    for i in range(1772,numImg):

        img, imgDet = coco.getImage(i)

        anns = coco.getAnnIds(imgDet)

        imgFileName = pathDesDir + imgDet['file_name'].split('.')[0]

        print('cropped ', i, ' image of ', numImg, 'images')

        for j in range(len(anns)):

            try:
                imgFileName = imgFileName + '_' + str(j) + '.png'

                mask = coco.getMask(anns, j)

                crop_img = coco.cropImageWithMask(img, mask)

                cv2.imwrite(imgFileName, crop_img)

            except:
                img_error.append(i)
            finally:
                j += 1

    print('id image error: ', img_error)


def overviewData():

    pathDirImage = ( '/home/dungpb/Downloads/Data tranning/car/')

    overviewData = OverviewData(pathDirImage)

    overviewData.vTData(10)

def testCropImage():

    img_error = []

    pathAnnotationFile = '/home/dungpb/Downloads/Data tranning/annotations_trainval2014/annotations/instances_train2014.json'
    category = 'car'
    pathDirImage = '/home/dungpb/Downloads/Data tranning/train2014/'

    coco = GetCocoData(pathAnnotationFile, category, pathDirImage)

    imgIds = coco.getDetailImage()

    img, imgDet = coco.getImage(1773)
    cv2.imshow('img', img)

    anns = coco.getAnnIds(imgDet)

    mask = coco.getMask(anns, 0)
    cv2.imshow('mask', mask)


    try:
        crop_img = coco.cropImageWithMask(img, mask)
    except:
        img_error.append(1773)
    finally:
        j += 1

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
