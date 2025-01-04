import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import cv2
import os
import tempfile
from sophisticated_nn_test import model

# Streamlit App
st.title("28x28 Pixel Number Drawing")
st.write("Draw a number in the enlarged 28x28 pixel space below, and hit 'Predict' to see the prediction.")

# Temporary file setup
TEMP_FILE_PATH = tempfile.NamedTemporaryFile(delete=False, suffix=".png").name

# Layout with columns
col1, col2 = st.columns([2, 1])

with col1:
    # Drawing canvas
    canvas_result = st_canvas(
        fill_color="#FFFFFF",  # White canvas background
        stroke_width=10,  # Increased stroke width for better visibility
        stroke_color="#000000",  # Black drawing color
        background_color="#FFFFFF",  # Canvas background
        update_streamlit=True,
        height=28 * 10,  # Enlarged canvas size
        width=28 * 10,  # Enlarged canvas size
        drawing_mode="freedraw",
        display_toolbar=True,  # Display toolbar
        key="canvas",
    )

if canvas_result.image_data is not None:
    with col2:
        # Resize canvas to 28x28
        img = cv2.resize(canvas_result.image_data.astype(np.uint8), (28, 28))
        # Rescale image for display
        img_rescaling = cv2.resize(img, dsize=(200, 200), interpolation=cv2.INTER_NEAREST)

        # Display the rescaled image
        st.image(img_rescaling, caption="Rescaled Image", width=200)

        # Save temporary image file
        cv2.imwrite(TEMP_FILE_PATH, img)

    # Predict on button click
    if st.button("Predict"):
        img = cv2.imread(TEMP_FILE_PATH)[:,:,0]  # Convert to grayscale
        img = np.invert(np.array([img]))
        pred = model.predict(img)
        pred = np.argmax(pred)

        st.title(f"Predicted Number: {pred}")

        # Delete the previous temporary file
        if os.path.exists(TEMP_FILE_PATH):
            os.remove(TEMP_FILE_PATH)
