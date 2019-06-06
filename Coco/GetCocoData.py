from pycocotools.coco import COCO
import cv2

class GetCocoData:

    def __init__(self, pathAnnotationFile: str, category: str, pathDirImage: str):
        self.__pathAnnotationFile = pathAnnotationFile
        self.__category = category
        self.__pathDirImage = pathDirImage

        # init COCO apiD
        self.__coco = COCO(pathAnnotationFile)

        # extract the category ids using the label
        self.__catIds = self.__coco.getCatIds(catNms=self.__category)

        # extract the image ids using the catTds
        self.__imgIds = self.__coco.getImgIds(catIds=self.__catIds)

    def getDetailImage(self):
        # print number of image with tag
        print('number of image with tag ', self.__category, ' : ', len(self.__imgIds))

        # return details of image (get image id with imgIds[0])
        return self.__imgIds

    def getAnnIds(self, imgDetail):
        # extract the annotation id
        annIds = self.__coco.getAnnIds(imgIds=imgDetail['id'], catIds=self.__catIds, iscrowd=None)

        # load the annotation
        anns = self.__coco.loadAnns(annIds)

        # return the annotation of image
        return anns

    def getImage(self, imageId):
        # extract the details of image with img id
        imgDetails = self.__coco.loadImgs(self.__imgIds[imageId])[0]

        # load image using the location of the file
        img = cv2.imread(self.__pathDirImage + imgDetails['file_name'])

        return img, imgDetails

    def getMask(self, anns, annsId):
        # get mask
        mask = self.__coco.annToMask(anns[annsId])

        # value in mask are 0 and 1 for display i change to 0 and 255
        for i in range(len(mask)):
            for j in range(len(mask[0])):
                if (mask[i, j] != 0):
                    mask[i, j] = 255

        return mask

    def __findMaxContour(self, contours):
        maxcontourArea = cv2.contourArea(contours[0])
        index = 0
        for i in range(len(contours)):
            contourArea = cv2.contourArea(contours[i])
            if (maxcontourArea < contourArea):
                maxcontourArea = contourArea
                index = i

        return contours[index]

    def __getBoundingBox(self, mask):
        # find edged on mask
        edged = cv2.Canny(mask, 100, 200)

        # find contours of mask
        _, contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # if have many contours find the biggest contour because mask maybe have some noise

        contour = self.__findMaxContour(contours)

        # get bounding box of rectangle
        epsilon = 0.01*cv2.arcLength(contour, True)
        contour_poly = cv2.approxPolyDP(contour, epsilon, True)
        boundRect = cv2.boundingRect(contour_poly)

        # return rectangle
        return boundRect

    def cropImageWithMask(self, image, mask):
        # get bounding box of object in image
        boundRect = self.__getBoundingBox(mask)

        #crop image
        crop_img = image[int(boundRect[1]):int(boundRect[1]+boundRect[3]), int(boundRect[0]):int(boundRect[0]+boundRect[2])]

        #return cropped image
        return crop_img