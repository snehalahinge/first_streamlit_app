import streamlit

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & blueberry Oatmeal')
streamlit.text(' 🥗 kale ,spinch & Rocket smoothy')
streamlit.text('🐔 Hard-boil  Free-Range Egg')               
streamlit.text('🥑🍞 Avacado Toast ')               
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
                 
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
