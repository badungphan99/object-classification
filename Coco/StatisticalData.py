import cv2
import os
from collections import Counter
import matplotlib.pyplot as plt


class StatisticalData:

    def __init__(self, pathDirImage: str):
        self.__pathDirImage = pathDirImage

        self.__files = os.listdir(self.__pathDirImage)

        self.__area = []

        self.__horizontal_imgs = 0

        self.__vertical_imgs = 0

    def __statisticalData(self):

        # read images in dir
        for i in self.__files:

            img = cv2.imread(self.__pathDirImage + i)

            rows = len(img)

            cols = len(img[0])

            if (rows >= cols):
                self.__vertical_imgs += 1
            if (rows < cols):
                self.__horizontal_imgs += 1

            self.__area.append(rows*cols)

    def vTData(self, numCols):

        self.__statisticalData()

        self.__area.sort()

        counter = Counter(self.__area)

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

        print('number horizontal imgs: ', self.__horizontal_imgs)
        print('number vertical imgs: ', self.__vertical_imgs)

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

    def getSize(self):
        for i in range(len(self.__files)):
            img = cv2.imread(self.__pathDirImage + self.__files[i])
            print(str(img.shape) + "area: "+ str(img.shape[0]*img.shape[1]))