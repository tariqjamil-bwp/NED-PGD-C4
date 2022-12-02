import streamlit as st
import pandas as pd

x_slider = st.slider('ABC')
st.write(x_slider, 'NED Machine Learning Application', x_slider*x_slider)