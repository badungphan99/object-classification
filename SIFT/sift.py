img = cv2.imread("test1.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

kp = sift.detect(imgGray, None)

print(len(kp))

for i in kp[:]:
    if(i.pt[1] <= 150):
        kp.remove(i)

print(len(kp))

for i in kp[:]:
    print(i.response)
# print(kp)
# for i in range(len(kp)):
#     if (kp[i].pt[1] >= 150):
#         print(kp[i].pt[1])
#     else:
#         print("not")
#         # print(kp[i].pt[1])
# print(kp)
img = cv2.drawKeypoints(img, kp, imgGray)

cv2.imshow("testsift",img)

cv2.waitKey(0)

cv2.destroyAllWindows()