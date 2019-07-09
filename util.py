import numpy as np

# input 
# 1.rgb_img: array of size H*W*3, representing a normalized jpg image
# output
# three normalized YCBCR images, each containing only one corresponding channel
def rgb_to_ycbcr(rgb_img):
	height, width = rgb_img.shape[0], rgb_img.shape[1]
	YImage = np.zeros((height,width))
	CbImage = np.zeros((height,width))
	CrImage = np.zeros((height,width))
	for h in range(0, height):
		for w in range(0, width):
			YImage[h][w]  =     +    0.299 * rgb_img[h][w][0] + 0.587    * rgb_img[h][w][1] + 0.114    * rgb_img[h][w][2]
			CbImage[h][w] = 128 - 0.168736 * rgb_img[h][w][0] - 0.331264 * rgb_img[h][w][1] + 0.5      * rgb_img[h][w][2]
			CrImage[h][w] = 128 +      0.5 * rgb_img[h][w][0] - 0.418688 * rgb_img[h][w][1] - 0.081312 * rgb_img[h][w][2]
	return YImage, CbImage, CrImage


mat = np.array(
    [[ 65.481, 128.553, 24.966 ],
     [-37.797, -74.203, 112.0  ],
     [  112.0, -93.786, -18.214]])
mat_inv = np.linalg.inv(mat)
offset = np.array([16, 128, 128])
 
def rgb2ycbcr(rgb_img):
    ycbcr_img = np.zeros(rgb_img.shape)
    for x in range(rgb_img.shape[0]):
        for y in range(rgb_img.shape[1]):
            ycbcr_img[x, y, :] = np.round(np.dot(mat, rgb_img[x, y, :] * 1.0 / 255) + offset)
    return ycbcr_img

def ycbcr2rgb(ycbcr_img):
    rgb_img = np.zeros(ycbcr_img.shape, dtype=np.uint8)
    for x in range(ycbcr_img.shape[0]):
        for y in range(ycbcr_img.shape[1]):
            [r, g, b] = ycbcr_img[x,y,:]
            rgb_img[x, y, :] = np.maximum(0, np.minimum(255, np.round(np.dot(mat_inv, ycbcr_img[x, y, :] - offset) * 255.0)))
    return rgb_img


def ycbcr_to_rgb(ycbcr_img):
	return

# input : 1-D vector
# output ： mean value of input
def mean_vec(vec):
    return