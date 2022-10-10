import streamlit
import pandas
/*streamlit.title('My Parents New Healthy Diner')*/
streamlit.title('Dear Jyoti, Your Healthy Diet Plan is here')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' (🥗 3 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 4 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
