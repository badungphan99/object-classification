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
