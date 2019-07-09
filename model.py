
class DeepFuseNet(object):
    """docstring for DeepFuseNet"""
    def __init__(self, arg):
        super(DeepFuseNet, self).__init__()
        self.arg = arg
        # Create the neural network
    def feature_extraction_layer(Y_k, n_classes, dropout, reuse, is_training):

        # Define a scope for reusing the variables
        with tf.variable_scope('feature_extraction', reuse=reuse):
            # TF Estimator input is a dict, in case of multiple inputs
            x = x_dict['images']

            # data preprocessing
            
            conv1 = tf.layers.conv2d(Y_k, 16, 5) # Convolution Layer with 16 filters and a kernel size of 5 (C11/C12)
            
            conv2 = tf.layers.conv2d(conv1, 32, 7) # Convolution Layer with 32 filters and a kernel size of 7 (C21/C22)

        return conv2
      
    def fusion_layer(F_1, F_2):
        return F_1 + F_2
      
    def reconstruction_layer(F_m):
        conv3 = tf.layers.conv2d(F_m, 32, 7) # Convolution Layer with 16 filters and a kernel size of 5 (C3)
            
        conv4 = tf.layers.conv2d(conv3, 16, 5) # Convolution Layer with 32 filters and a kernel size of 7 (C4)
        
        conv5 = tf.layers.conv2d(conv4, 1, 5) # Convolution Layer with 32 filters and a kernel size of 5 (C5)
        
        return conv5

    def Inference(Y_1, Y_2):
        F_1 = feature_extraction_layer(Y1)
        F_2 = feature_extraction_layer(Y2)
        F_m = fusion_layer(F_1, F_2)
        Y_Fused = reconstruction_layer(F_m)
        return Y_Fused
