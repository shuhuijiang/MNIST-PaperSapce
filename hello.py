#save this file as hello.py in your repo
import tensorflow as tf

# Simple hello world using TensorFlow
hello = tf.constant('Hello, TensorFlow second time!')

# Start tf session
sess = tf.Session()

# Run the op
print(sess.run(hello))