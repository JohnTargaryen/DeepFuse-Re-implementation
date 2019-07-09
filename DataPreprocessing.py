import tensorflow as tf
import os
import tensorflow.contrib.eager as tfe
#tfe.enable_eager_execution()

dataset_floder_path = './DataSet/DataSet_Part1'
under_exposed_photo_name = '/1.JPG'
over_exposed_photo_name = '/7.JPG'
NumOfFolders = 360

class DataPreprocessing(object):
	"""docstring for DataPreprocessing"""
	def __init__(self):
		super(DataPreprocessing, self).__init__()

	def read_one_image(slef, file_path) :
		image = tf.io.read_file(file_path)
		image = tf.image.decode_jpeg(image, channels = 3)
		return image

	def read_one_imagepair(folderpath) :
		return

	def testimport():
		print("test\n")
		return

	def _parse_function(self, filenames1, filenames7):
		image_string1 = tf.io.read_file(filenames1)
		image_string7 = tf.io.read_file(filenames7)
		image_decoded1 = tf.image.decode_jpeg(image_string1)
		image_decoded7 = tf.image.decode_jpeg(image_string7)
	  	# image_resized = tf.image.resize_images(image_decoded, [28, 28])
		return image_decoded1, image_decoded7

	# input
	# 1.folderpath: eg:"./DataSet/DataSet_Part1/", whose subdirectories are folders that contains the images
	# 2.num : eg:360, to construct strings of path names from 1 to num
	# ------------------
	# output
	# two lists containing filenames of 1.JPG and 7.JPG accordingly
	def NameConstruct(self, folderpath, num):
		filenames1 = []
		filenames7 = []
		tempstr1 = ""
		for i in range(1, num+1):
			tempstr1 = folderpath + '/' + str(i) + under_exposed_photo_name
			tempstr7 = folderpath + '/' + str(i) + over_exposed_photo_name
			filenames1.append(tempstr1)
			filenames7.append(tempstr7)
		return filenames1, filenames7

	def ConstructDataset(self):
		filenames1, filenames7 = self.NameConstruct(dataset_floder_path, NumOfFolders)
		# dataset = tf.data.Dataset.from_tensor_slices((filenames1, filenames7))
		# dataset = dataset.map(self._parse_function)
		# return dataset
		OverExposedImages = []
		UnderExposedImages = []
		for filepath in filenames1:
			tempimage = self.read_one_image(filepath)
			UnderExposedImages.append(tempimage)
		for filepath in filenames7:
			tempimage = self.read_one_image(filepath)
			OverExposedImages.append(tempimage)
		return UnderExposedImages, OverExposedImages

	# # 图片文件的列表
	# filenames = tf.constant(["/var/data/image1.jpg", "/var/data/image2.jpg", ...])
	# # label[i]就是图片filenames[i]的label
	# labels = tf.constant([0, 37, ...])

	# # 此时dataset中的一个元素是(filename, label)
	# dataset = tf.data.Dataset.from_tensor_slices((filenames, labels))

	# # 此时dataset中的一个元素是(image_resized, label)
	# dataset = dataset.map(_parse_function)

	# # 此时dataset中的一个元素是(image_resized_batch, label_batch)
	# dataset = dataset.shuffle(buffersize=1000).batch(32).repeat(10)
