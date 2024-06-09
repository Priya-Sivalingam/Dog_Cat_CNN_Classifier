import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np

model = load_model(r'C:\Users\Admin\Downloads\Assignment\Image Classify.keras')
data_cat = ['Dogs', 'Cats']
img_height = 256
img_width = 256
st.header('Image Classification Model')
st.write('design by:2020e122')
image = st.text_input('Enter Image file path')
image_load = tf.keras.preprocessing.image.load_img(image, target_size=(img_height, img_width))
img_arr = tf.keras.preprocessing.image.img_to_array(image_load)
img_bat = tf.expand_dims(img_arr, 0)
predict = model.predict(img_bat)
score = tf.nn.softmax(predict)
st.image(image)
st.write('Dog/Cat in image is '+data_cat[np.argmax(score)])
st.write('with accuracy of '+str(np.max(score)*100))

