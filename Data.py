import streamlit as st
import pandas as pd

st.set_page_config(
   page_title="Movie Explorer",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.markdown("<h1 style='text-align: center;'>Movie Analysis</h1>", unsafe_allow_html=True)
movies_df = pd.read_csv('movies2.csv',lineterminator='\n')
movies_df = movies_df.drop(columns=movies_df.columns[0])
movies_df = movies_df[movies_df['Release Date'] < "2022-01-01"]
st.write(movies_df)
st.caption("Data Source: TMDB")
cast_df = pd.read_csv('movie_cast.csv')

