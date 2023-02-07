import streamlit as stl
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

stl.title('My parents new healthy diner')

stl.header('Breakfast menu')

stl.text('🥣 Omega 3 & Blueberry oatmeal')
stl.text('🥗 Kale, spinach & rocket smothie')
stl.text('🐔 Hard-boiled free-range egg')
stl.text('🥑🍞 Avocado toast')

stl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
stl.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# Display the table on the page.
stl.dataframe(my_fruit_list)
