import cv2 
import streamlit as st

img = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)
st.write(img)
