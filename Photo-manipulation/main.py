import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance

st.title("🖼️ Advanced Photo Manipulator")

# Image Upload
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    
    # Filters
    brightness = st.slider("Brightness", 0.5, 2.0, 1.0)
    contrast = st.slider("Contrast", 0.5, 2.0, 1.0)
    saturation = st.slider("Saturation", 0.5, 2.0, 1.0)
    sharpness = st.slider("Sharpness", 0.5, 2.0, 1.0)

    grayscale = st.checkbox("Grayscale")
    sepia = st.checkbox("Sepia Effect")
    invert = st.checkbox("Invert Colors")

    # Apply Filters
    img = ImageEnhance.Brightness(image).enhance(brightness)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Color(img).enhance(saturation)
    img = ImageEnhance.Sharpness(img).enhance(sharpness)

    # Convert to OpenCV format
    img_cv = np.array(img)

    if grayscale:
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
    
    if sepia:
        kernel = np.array([[0.272, 0.534, 0.131], 
                           [0.349, 0.686, 0.168], 
                           [0.393, 0.769, 0.189]])
        img_cv = cv2.transform(img_cv, kernel)
        img_cv = np.clip(img_cv, 0, 255)

    if invert:
        img_cv = cv2.bitwise_not(img_cv)

    # Convert back to PIL
    final_image = Image.fromarray(img_cv)

    # Display Image
    st.image(final_image, caption="Edited Image", use_container_width=True)

    # Download Button
    st.download_button(
        label="Download Edited Image",
        data=final_image.tobytes(),
        file_name="edited_image.png",
        mime="image/png"
    )
