import streamlit as st
import cv2
import numpy as np
from datetime import datetime
from PIL import Image

st.set_page_config(layout="wide")
st.title("📷 Webcam Filter App")
st.sidebar.header("⚙️ Controls")

# Filter options
filter_type = st.sidebar.selectbox("Choose Filter", ["None", "Grayscale", "Canny Edge", "Face Detection"])
low_threshold = st.sidebar.slider("Canny Low Threshold", 0, 100, 30)
high_threshold = st.sidebar.slider("Canny High Threshold", 100, 300, 150)

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Webcam input
st.info("📸 Take a picture using your webcam")
camera_input = st.camera_input("Take a snapshot")

if camera_input is not None:
    image = Image.open(camera_input)
    frame = np.array(image)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Apply filter
    if filter_type == "Grayscale":
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
    elif filter_type == "Canny Edge":
        edges = cv2.Canny(frame, low_threshold, high_threshold)
        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    elif filter_type == "Face Detection":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show processed image
    st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), caption="🖼️ Processed Image", use_container_width=True)
