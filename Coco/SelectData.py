import cv2
import os
import datetime
import math

class SelectData:
	def __init__(self, pathDir:str):
		self.pathDir = pathDir
		self.refPt = []
		self.cropping = False


	def mouseCropImg(self, desDir):
		files = [f for f in os.listdir(self.pathDir) if os.path.isfile(os.path.join(self.pathDir, f))]
		if not os.path.exists(desDir):
			os.mkdir(desDir)
		else:
			print("Dir already exists")

		for file in files:
			self.__cropWithMouse(self.pathDir + "/" + file, desDir)

	def __click_and_crop(self, event, x, y, flags, param):
		if event == cv2.EVENT_LBUTTONDOWN:
			self.refPt = [(x, y)]
			self.cropping = True

		elif event == cv2.EVENT_LBUTTONUP:
			self.refPt.append((x, y))
			self.cropping = False
			print(self.refPt)

	def __cropWithMouse(self, fileName:str, desName:str):
		pathimg = self.pathDir + fileName
		image = cv2.imread(pathimg)
		clone = image.copy()
		cv2.namedWindow("image")
		cv2.setMouseCallback("image", self.__click_and_crop)
		if len(self.refPt) == 2:
			cv2.rectangle(image, self.refPt[0], self.refPt[1], (0, 255, 0), 2)

		while True:
			if len(self.refPt) == 2:
				cv2.rectangle(image, self.refPt[0], self.refPt[1], (0, 255, 0), 2)
			# display the image and wait for a keypress
			cv2.imshow("image", image)
			key = cv2.waitKey(1) & 0xFF

			# if the 'r' key is pressed, reset the cropping region
			if key == ord("r"):
				image = clone.copy()
				self.refPt = []
			# if the 'c' key is pressed, break from the loop
			elif key == ord("c"):
				break

		# if there are two reference points, then crop the region of interest
		# from teh image and display it
		if len(self.refPt) == 2:
			roi = clone[self.refPt[0][1]:self.refPt[1][1], self.refPt[0][0]:self.refPt[1][0]]
			print("area: " + str(roi.size))
			print("shape: " + str(roi.shape))
			cv2.imwrite(desName + str(datetime.datetime.now()) + ".png", roi)
		# close all open windows
		cv2.destroyAllWindows()

	def sizeCropImg(self, size):
		length = int(math.sqrt(size))
		print(length)
		pass