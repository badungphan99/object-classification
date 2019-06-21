import cv2

value = 0
def trackbar_callback(val):
    value = val
    img = cv2.imread('/home/dungpb/Dropbox/Dev/classificationObject/ColorImage/2019-06-17 10:37:37.407167.png', 0)

    for i in range(len(img)):
        for j in range(len(img[0])):
            img[i,j] += val
    cv2.imshow("test", img)
if __name__ == '__main__':
    print("abc")

    cv2.namedWindow("test")
    cv2.createTrackbar("TestTrackbar","test",0,255,trackbar_callback)
    # trackbar_callback(value)
    # print(value)
    cv2.waitKey(0)