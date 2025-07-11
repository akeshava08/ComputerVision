import streamlit as st
from utils import *
from PIL import Image

# Your Streamlit app goes here!
st.title('Traffic Detection with Computer Vision')

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file) # Use Image.open to open the image
    st.image(image, caption='Uploaded Image.', use_container_width=True) # use_column_width is optional, just helps for Display

    # Use the detect_image function to process the uploaded image
    result_image = detect_image(image)
    st.image(result_image, caption='Image with Detections', use_container_width=True)
