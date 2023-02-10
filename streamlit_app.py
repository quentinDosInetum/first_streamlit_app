import streamlit as stl
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

my_cnx = snowflake.connector.connect(**stl.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()

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
fruits_selected = stl.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
stl.dataframe(fruits_to_show)

stl.header("Fruityvice Fruit Advice!")

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{this_fruit_choice}")
  # normalize json response
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  
  return fruityvice_normalized

try:
  
  fruit_choice = stl.text_input('What fruit would you like information about?')
  
  if not fruit_choice:
    stl.error("Please select fruit to get information.")
    
  else:
    # display response as table
    stl.dataframe(get_fruityvice_data(fruit_choice))
    
except URLError as e:
  
  stl.error()

stl.stop()

stl.header("The fruit load list contains")
stl.dataframe(my_data_rows)

# allow user to add afruitto the list

add_my_fruit = stl.text_input('What fruit would you like to add ?')
stl.write('Thank you for adding ', add_my_fruit)

my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('From streamlit')")
