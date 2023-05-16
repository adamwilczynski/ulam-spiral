import streamlit as st
from PIL import ImageColor

import utils

PAGE_TITLE = "Ulam Spiral Generator"

st.set_page_config(page_title=PAGE_TITLE, layout="wide")

st.title(PAGE_TITLE)

st.header("Ulam")

WHITE = "#ffffff"
composite_color = ImageColor.getcolor(st.color_picker("Composite", WHITE), "RGB")

BLACK = "#000000"
prime_color = ImageColor.getcolor(st.color_picker("Primes", BLACK), "RGB")

size = st.slider("Specify square size", min_value=0, max_value=utils.MAX_SIZE)

st.image(
    utils.SpiralImage(
        size,
        composite_color=composite_color,
        prime_color=prime_color
        ).get_spiral_image()
)
