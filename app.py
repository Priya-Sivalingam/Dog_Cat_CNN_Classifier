import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np
from PIL import Image

# Load the model
model = load_model('/path/to/model/Image_Classify.keras')  # Update with correct path
data_cat = ['Dogs', 'Cats']
img_height = 256
img_width = 256

# Streamlit interface
st.header('Image Classification Model')
st.write('Designed by: 2020e122')

# Upload image using Streamlit's file uploader
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    # Open and preprocess the image
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Convert image to array and preprocess
        image = image.resize((img_height, img_width))
        img_arr = tf.keras.preprocessing.image.img_to_array(image)
        img_bat = tf.expand_dims(img_arr, 0)  # Add batch dimension

        # Predict and display the result
        predict = model.predict(img_bat)
        score = tf.nn.softmax(predict)
        st.write('Dog/Cat in image is ' + data_cat[np.argmax(score)])
        st.write('with accuracy of {:.2f}%'.format(np.max(score) * 100))
    except Exception as e:
        st.error(f"An error occurred while processing the image: {e}")
