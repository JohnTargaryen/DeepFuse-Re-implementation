from DataPreprocessing import *
from util import *
import numpy as np
from PIL import Image

def main():
	DP = DataPreprocessing()
	UnderExposedImages, OverExposedImages = DP.ConstructDataset()
	UnderExposedYCbCrImages = [[], [], []]
	OverExposedYCbCrImages = [[], [], []]
	with tf.Session() as sess:
		for img in UnderExposedImages:
			Image_Array = img.eval()
			#Image_Array = Image_Array / 255 # normalization
			YImage, CbImage, CrImage = rgb_to_ycbcr(Image_Array)
			
			UnderExposedYCbCrImages[0].append(YImage)
			UnderExposedYCbCrImages[1].append(CbImage)
			UnderExposedYCbCrImages[2].append(CrImage)
			print("test")
		# Image.fromarray(np.asarray(OverExposedImages[0].eval())).show()
	return

main()

