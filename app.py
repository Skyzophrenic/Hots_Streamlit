import streamlit as st 
import pandas as pd 

st.set_page_config(layout="wide")

blue, center, red = st.columns([5,2,5])

with blue:
  b1 = st.selectbox(
    "b1",
    ("Abathur","Alarak","Alexstrasza"))
  b2 = st.selectbox(
    "b2",
    ("Abathur","Alarak","Alexstrasza"))
  b3 = st.selectbox(
    "b3",
    ("Abathur","Alarak","Alexstrasza"))
  b4 = st.selectbox(
    "b4",
    ("Abathur","Alarak","Alexstrasza"))
  b5 = st.selectbox(
    "b5",
    ("Abathur","Alarak","Alexstrasza"))

with red:
  r1 = st.selectbox(
    "r1",
    ("Abathur","Alarak","Alexstrasza"))
  r2 = st.selectbox(
    "r2",
    ("Abathur","Alarak","Alexstrasza"))
  r3 = st.selectbox(
    "r3",
    ("Abathur","Alarak","Alexstrasza"))
  r4 = st.selectbox(
    "r4",
    ("Abathur","Alarak","Alexstrasza"))
  r5 = st.selectbox(
    "r5",
    ("Abathur","Alarak","Alexstrasza"))


with center:
  st.button('Reset', use_container_width=True)
  st.button('Bot Pick', use_container_width=True)
  map = st.selectbox("map",("Infernal","Towers","Tomb"))
  map_picture = st.image('tomb.jpg')














