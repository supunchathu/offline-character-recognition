from input_data import *
mnist = read_data_sets("E:\projects\CO542", one_hot=True)
train_images = mnist.train._images
print(type(train_images))
train_labels = mnist.train._labels
print(type(train_labels))
