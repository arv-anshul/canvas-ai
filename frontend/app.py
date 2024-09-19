import json

import httpx
import streamlit as st
from PIL import Image
from src import api
from src.constants import BACKEND_API_BASE_URL

st.set_page_config("Canvas AI - arv-anshul", "🖼️")

CLIENT = httpx.Client(base_url=BACKEND_API_BASE_URL)
api.check_api_running(CLIENT)

st.title("Canvas AI", help="By arv-anshul")
st.caption("Parse and Analyse your Canvas/Image with AI")
st.divider()

st.subheader("One-Shot Canvas Analyser")
input_way = st.selectbox("How to provide image?", ("Upload Image", "Draw on Canvas"))

if input_way == "Draw on Canvas":
    # FIXME: make this work
    st.info("This feature does not work yet.", icon="🙇")
    st.stop()

    # TODO: Move the import statement to top after fixing the issue
    from streamlit_drawable_canvas import st_canvas

    _image_caption = "Image from Canvas"
    _, col, _ = st.columns([0.1, 2, 0.1])
    with col:
        image_array = st_canvas(
            fill_color="#fff",
            stroke_color="red",
            stroke_width=7,
            background_color="#1e1e1e",
        ).image_data
    if image_array is None:
        st.stop()
    image_bytes = Image.fromarray(image_array).tobytes()
elif input_way == "Upload Image":
    _image_caption = "Your Uploaded Image"
    uploaded_file = st.file_uploader(
        "Upload a image containing mathematical expression or problem",
        [".png", ".jpg", ".jpeg"],
    )
    if not uploaded_file:
        st.stop()
    image_bytes = uploaded_file.read()
    uploaded_file.close()
else:
    st.error("Selected 'way of input' is not supported.")
    st.stop()

if not st.button("Submit", use_container_width=True):
    st.stop()

_, col, _ = st.columns([0.3, 0.4, 0.3])
col.image(image_bytes, _image_caption)

with st.spinner("Requesting to API..."):
    response = api.one_shot(CLIENT, image_bytes)
st.code(json.dumps(response, indent=4), "json")
st.balloons()
