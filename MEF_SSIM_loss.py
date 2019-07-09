# input : two image patches y1、y2, and the corresponding image patch output by CNN yf, all in the form of 1D-vector
# output : Score of this patch
def Score(y1, y2. yf) :
	C = 0.0001

	# μ_yk
	y1_mean = tf.reduce_mean(y1)
	y2_mean = tf.reduce_mean(y2)

	# y_k upperwave
	y1_mean_sub = y1 - y1_mean
	y2_mean_sub = y2 - y2_mean

	# c_k and c^(c_upperArrow)
	c1 = tf.norm(y1)
	c2 = tf.norm(y2)
	if c1 > c2 :
		c_upperArrow = c1
	else:
		c_upperArrow = c2

	# s_k	
	s1 = y1_mean_sub / c1
	s2 = y2_mean_sub / c2

	# s upper dash
	s_upperDash = 

	# s^
	s_upperArrow = s_upperDash / tf.norm(s_upperDash)

	# y^
	y_upperArrow = c_upperArrow * s_upperArrow


def Loss() :
	for all patches in trainingset : 
		