import streamlit as stl
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

stl.title('My parents new healthy diner')

stl.header('Breakfast menu')

stl.text('🥣 Omega 3 & Blueberry oatmeal')
stl.text('🥗 Kale, spinach & rocket smothie')
stl.text('🐔 Hard-boiled free-range egg')
stl.text('🥑🍞 Avocado toast')

stl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

stl.dataframe(my_fruit_list)
