import numpy as np 
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
import nltk
x=np.zeros((5,5))
X=tf.compat.v1.placeholder(shape=(5,5), name='X', dtype='float32')
with tf.compat.v1.Session() as sess:
    print(sess.run(X, feed_dict={X:x}))