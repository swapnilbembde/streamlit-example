import streamlit as st
from PIL import Image

def crop_image(img, coords):
    return img.crop(coords)

st.title("Image Cropping App")

uploaded_file = st.file_uploader("Upload an image...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    st.write("Set cropping coordinates:")
    x1 = st.slider('x1', 0, image.width, 0)
    y1 = st.slider('y1', 0, image.height, 0)
    x2 = st.slider('x2', x1, image.width, image.width)
    y2 = st.slider('y2', y1, image.height, image.height)

    if st.button("Crop Image"):
        cropped_img = crop_image(image, (x1, y1, x2, y2))
        st.image(cropped_img, caption='Cropped Image.', use_column_width=True)
