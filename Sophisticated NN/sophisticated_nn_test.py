import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sophisticated_nn import x_test, y_test

model = tf.keras.models.load_model('sophisticated_nn.keras')

loss, accuracy = model.evaluate(x_test, y_test)

print(loss)
print(accuracy)
