import cv2
import os
import random
from collections import Counter
import matplotlib.pyplot as plt

class Sift:

    def __init__(self, pathDir: str):
        self.__pathDir = pathDir
        self.__files = os.listdir(self.__pathDir)

    def overviewSift(self):
        perFile = 10
        numCols = 10
        numFile = int(perFile * len(self.__files) / 100)
        print(numFile)
        lenKp = []
        for i in range(numFile):
            print('load ',i,' of ', numFile)
            name = random.choice(self.__files)
            path = self.__pathDir + name
            img = cv2.imread(path)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            sift = cv2.xfeatures2d_SIFT.create()
            kp = sift.detect(imgGray, None)
            lenKp.append(len(kp))
        lenKp.sort()
        counter = Counter(lenKp)

        x = [*counter.keys()]
        y = [*counter.values()]

        len_x = len(x)

        max_x = x[len_x - 1]

        new_x = []

        new_y = []

        temp = int(max_x / numCols)

        for i in range(numCols):
            new_x.append(temp * i)
        new_x.append(max_x)

        for i in range(1, len(new_x)):
            temp_y = 0
            for j in range(len(y)):
                if x[j] > new_x[i - 1] and x[j] <= new_x[i]:
                    temp_y += y[j]

            new_y.append(temp_y)

        new_x.remove(new_x[0])

        print(new_x)
        print(new_y)

        tuple(new_x)

        plt.bar(new_x, new_y, align='center')  # A bar chart
        plt.xlabel('Area')
        plt.ylabel('Frequency')
        for i in range(len(new_y)):
            plt.hlines(new_y[i], 0, new_x[i])
        plt.show()

    def getDataSift(self, numKeypoint: int):

        pass

    def siftImage(self):
        for i in range(len(self.__files)):
            path = self.__pathDir + self.__files[i]
            img = cv2.imread(path)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            sift = cv2.xfeatures2d.SIFT_create()
            kp, descriptors = sift.detectAndCompute(imgGray, None)
            img = cv2.drawKeypoints(img, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv2.imshow(self.__files[i], img)
            print(descriptors)
            cv2.waitKey(0)

    def randomSiftImage(self, numImg:int, pathDir:str):
        for i in range(numImg):
            name = random.choice(self.__files)
            path = self.__pathDir + name
            pathtxt = pathDir + name + ".txt"
            img = cv2.imread(path)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            sift = cv2.xfeatures2d.SIFT_create()
            kp, descriptors = sift.detectAndCompute(imgGray, None)
            img = cv2.drawKeypoints(img, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv2.imshow(self.__files[i], img)
            for i in range(len(descriptors)):
                for j in range(len(descriptors[0])):
                    print(descriptors[i, j])
                    file = open(pathtxt, "a")
                    file.write(str(descriptors[i, j]) + '|')
                file = open(pathtxt, "a")
                file.write('\n')
            cv2.waitKey(0)

    def descriptorSift(self):
        path = '/home/dungpb/DataTraining/data_train2014/dog/selected/2019-06-21 11:34:27.314954.png'
        img = cv2.imread(path)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()
        kp, descriptors = sift.detectAndCompute(imgGray, None)
        img = cv2.drawKeypoints(img, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow("test", img)
        for i in range(len(descriptors)):
            for j in range(len(descriptors[0])):
                print(descriptors[i,j])
                file = open("demofile2.txt", "a")
                file.write(str(descriptors[i,j]) + '|')
            file = open("demofile2.txt", "a")
            file.write('\n')
        cv2.waitKey(0)