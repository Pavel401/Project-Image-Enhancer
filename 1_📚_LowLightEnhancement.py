import os
import streamlit as st
from app_funcs import *
import streamlit as st
from streamlit_image_comparison import image_comparison
#streamlit run 1_📚_LowLightEnhancement.py   
st.set_page_config(
    page_title="Low Light Image Enhancer",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
)
main_image = Image.open('static/main_banner.png')

upload_path = "uploads/"
download_path = "downloads/"

st.image(main_image, use_column_width='auto')
st.title("✨ Low Light Image Enhancer 🖼 ")
st.info('✨ Supports all popular image formats 📷 - PNG, JPG, BMP 😉')

uploaded_file = st.file_uploader(
    "Upload Image 🖼", type=["png", "jpg", "bmp", "jpeg"])

if uploaded_file is not None:
    with open(os.path.join(upload_path, uploaded_file.name), "wb") as f:
        f.write((uploaded_file).getbuffer())

    with st.spinner(f"Enhancing... 💫"):
        uploaded_image = os.path.abspath(
            os.path.join(upload_path, uploaded_file.name))
        downloaded_image = os.path.abspath(os.path.join(
            download_path, str("enhanced_"+uploaded_file.name)))
        enhance_image(uploaded_image, downloaded_image)

        final_image = Image.open(downloaded_image)
        print("Opening ", final_image)
        st.markdown("---")
        image_comparison(
            img1=uploaded_image,
            img2=final_image,
            label1="Input Image",
            label2="Output Image",
            width=700,
            starting_position=50,
            show_labels=True,
            make_responsive=True,
            )
        # st.image(final_image, caption='This is how your enhanced image looks like 😉')
        with open(downloaded_image, "rb") as file:
            if uploaded_file.name.endswith('.jpg') or uploaded_file.name.endswith('.JPG'):
                if st.download_button(
                    label="Download Enhanced Image 📷",
                    data=file,
                    file_name=str("enhanced_"+uploaded_file.name),
                    mime='image/jpg'
                ):
                    download_success()

            if uploaded_file.name.endswith('.jpeg') or uploaded_file.name.endswith('.JPEG'):
                if st.download_button(
                    label="Download Enhanced Image 📷",
                    data=file,
                    file_name=str("enhanced_"+uploaded_file.name),
                    mime='image/jpeg'
                ):
                    download_success()

            if uploaded_file.name.endswith('.png') or uploaded_file.name.endswith('.PNG'):
                if st.download_button(
                    label="Download Enhanced Image 📷",
                    data=file,
                    file_name=str("enhanced_"+uploaded_file.name),
                    mime='image/png'
                ):
                    download_success()

            if uploaded_file.name.endswith('.bmp') or uploaded_file.name.endswith('.BMP'):
                if st.download_button(
                    label="Download eEhanced Image 📷",
                    data=file,
                    file_name=str("enhanced_"+uploaded_file.name),
                    mime='image/bmp'
                ):
                    download_success()
else:
    st.warning('⚠ Please upload your Image file 😯')


st.markdown("<br><hr><center>Made with ❤️ by <a href='pavelalam401@gmail.com?subject=Low Light Image Enhancement WebApp!&body=Please specify the issue you are facing with the app.'><strong>Mabud Alam</strong></a></center><hr>", unsafe_allow_html=True)
