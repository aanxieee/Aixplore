import streamlit as st
from PIL import Image

def show():
    st.header("Upload a Photo")

    file = st.file_uploader("Upload food / textile / monument photo", type=["jpg", "jpeg", "png"])

    if file:
        img = Image.open(file)
        st.image(img, caption="Your uploaded image", use_column_width=True)

        st.info("Mock classification: Food\nMock description: Famous local street food.")
