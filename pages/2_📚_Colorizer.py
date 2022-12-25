import streamlit as st
from PIL import Image
import requests
import base64
import os
import streamlit as st
from streamlit_image_comparison import image_comparison
def footer():
	st.markdown("""
	* * *
	Built with ❤️ by [Mabud Alam](https://Pavel401.github.io/)
	""")
	st.success("Rehan uddin (Hardly-Human)👋😉")
	

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">[ Download Image ]</a>'
    return href


################################################################################
# main()
################################################################################


def main():
  
	st.title("Image Colorization App")
	# st.text("Built with gluoncv and Streamlit")
	# st.markdown("### [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Hardly-Human/Image-Colorization-App)\
	# `            `[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://lbesson.mit-license.org/)")

	image_file = st.file_uploader("Upload Image", type = ['jpg','png','jpeg'])

	if image_file is None:
		st.warning("Upload Image and Colorize")

	if image_file is not None:
		image1 = Image.open(image_file)
		rgb_im = image1.convert('RGB') 
		image = rgb_im.save("saved_image.jpg")
		image_path = "saved_image.jpg"
		st.image(image1,width = 700)
	if st.button("Colorize"):
		if image_file is not None:
			st.warning("Please Wait⌛....Artistic Work in progress 🎨🎭👨‍🎨 ")
			r = requests.post(
			    "https://api.deepai.org/api/colorizer",
			    files={
			        'image': open('saved_image.jpg', 'rb'),
			    },
			    headers={'api-key': '8f0499fe-bf0f-455d-9f4b-3acb442b49c4'}
			)

			color_image_url = r.json()["output_url"]

			img_data = requests.get(color_image_url).content
			with open('color_image.jpg', 'wb') as handler:
				handler.write(img_data)
			st.success("Image Colorization Successfull 🙌🥳🎉")
			color_image = Image.open('color_image.jpg')

			st.subheader("Colorized Image")
			st.image(color_image)
          
			st.markdown(get_binary_file_downloader_html('color_image.jpg', 'Picture'), unsafe_allow_html=True)

		else:
			st.error("Please Upload Image!!!")


if __name__== "__main__":
	main()
	footer()