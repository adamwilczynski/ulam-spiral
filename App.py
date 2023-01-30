import streamlit as st
from PIL import ImageColor

import utils

st.title("Ulam Spiral Generator")

st.header("Ulam")

WHITE = "#ffffff"
composite_color = ImageColor.getcolor(st.color_picker("Composite", WHITE), "RGB")

BLACK = "#000000"
prime_color = ImageColor.getcolor(st.color_picker("Primes", BLACK), "RGB")

SIZE = 1_00

st.image(utils.SpiralImage(SIZE, utils.PrimeColorMap(composite_color=composite_color, prime_color=prime_color)).get_spiral_image())
