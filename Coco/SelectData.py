import cv2

class SelectData:
	def __init__(self, path:str):
		self.path = path
		self.refPt = []
		self.cropping = False
	def click_and_crop(self, event, x, y, flags, param):

		if event == cv2.EVENT_LBUTTONDOWN:
			self.refPt = [(x, y)]
			self.cropping = True

		elif event == cv2.EVENT_LBUTTONUP:
			self.refPt.append((x, y))
			self.cropping = False

	image = cv2.imread("../ColorImage/2019-06-17 10:37:22.526296.png")
	clone = image.copy()
	cv2.namedWindow("image")
	cv2.setMouseCallback("image", click_and_crop)

	while True:
		# display the image and wait for a keypress
		cv2.imshow("image", image)
		key = cv2.waitKey(1) & 0xFF

		# if the 'r' key is pressed, reset the cropping region
		if key == ord("r"):
			image = clone.copy()

		# if the 'c' key is pressed, break from the loop
		elif key == ord("c"):
			break

	# if there are two reference points, then crop the region of interest
	# from teh image and display it
	if len() == 2:
		roi = clone[serefPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
		cv2.imshow("ROI", roi)
		cv2.waitKey(0)

	# close all open windows
	cv2.destroyAllWindows()