import tensorflow_hub as hub
import cv2
import numpy
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

width = 1028
height = 1028
img = cv2.imread('image_2.jpg')
inp = cv2.resize(img, (width , height ))
rgb = cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)
rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.uint8)
rgb_tensor = tf.expand_dims(rgb_tensor , 0)
