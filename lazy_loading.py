import tensorflow as tf

# Normal Loading
x = tf.Variable(10, name = 'x')
y = tf.Variable(20, name = 'y')
z = tf.add(x,y)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(10):
        sess.run(z)

# Lazy loading
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(10):
        sess.run(tf.add(x,y)) # Adding the operation multiple times creates muliple graphs and bloated up.
