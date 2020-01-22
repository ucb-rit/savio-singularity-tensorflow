# Simple script to check that TensorFlow is working with GPU support
# Use only with Tensorflow >= 2.0.0

import tensorflow as tf
print(tf.__version__)
# Check if GPU is available
print(tf.config.list_physical_devices('GPU'))
