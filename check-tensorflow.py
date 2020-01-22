# Simple script to check that TensorFlow is working with GPU support
# Use only with Tensorflow < 2.0.0 as API changed in Tensorflow 2.

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
print(tf.__version__)
print('GPU is available: ', tf.test.is_gpu_available())
