# Deep-Learning-Projects
3 **Introduction**
This report outlines the process of building and tuning a Convolutional Neural Network (CNN) 
classifier to distinguish between images of dogs and cats. The model was trained using TensorFlow 
and Keras, and hyperparameter tuning was performed using Weights & Biases (W&B) to optimize the 
model's performance.
# **Dataset**
The dataset used consists of images of dogs and cats, with separate directories for training and 
testing data. The data was loaded using TensorFlow's image_dataset_from_directory function.
• Image Loading: The dataset is loaded using tf.keras.utils.image_dataset_from_directory
from the specified directories for training and testing data
