import streamlit as st
from Data import movies_df, cast_df

st.header("Find Data by Movie Title")
name = st.selectbox("Enter Movie Name", movies_df["Title"].tolist())
id = movies_df.index[movies_df['Title'] == name]
st.write("### Description")
st.write(movies_df[movies_df['Title'] == name]['Description'].tolist()[0])
st.write("### Movie ID")
st.write(str(movies_df[movies_df['Title'] == name]['Id'].tolist()[0]))
st.write('### Movie Genres')
genre_list = movies_df[movies_df['Title'] == name]['Genres'].tolist()[0].lstrip('[').rstrip(']').split(",")
s = ''
for i in genre_list:
    i = i.strip().strip("\'")
    s += "<li>" + i + "</li>"

st.markdown("<ul>"+s+"</ul>",unsafe_allow_html=True)
st.write('### Release Date')
date, format = st.tabs(["Date","Format"])
with date:
    st.write(movies_df[movies_df['Title'] == name]['Release Date'].tolist()[0])
with format:
    st.caption('YYYY-MM-DD')


st.write("### Ratings")
rating, vote_count = st.tabs(["Ratings","Vote Count"])
with rating:
    st.markdown("<p style = 'font-size: 16px;'>"+str(movies_df[movies_df['Title'] == name]['Rating'].tolist()[0])+"/10"+"</p>", unsafe_allow_html = True)
with vote_count:
    st.write(str(movies_df[movies_df['Title'] == name]['Vote Count'].tolist()[0]))

st.write("### Revenue (in USD)")
if movies_df[movies_df['Title'] == name]['Revenue'].tolist()[0] != 0:
    st.markdown("<p style = 'font-size: 18px'>$ " + str(movies_df[movies_df['Title'] == name]['Revenue'].tolist()[0])+'</p>', unsafe_allow_html = True)
else:
    st.write("The revenue is unknown or N/A")

st.write("### Movie Cast")
movie_id = movies_df[movies_df["Title"] == name]["Id"].tolist()[0]
cast_list = eval(cast_df[cast_df["Movie Id"] == movie_id]['Cast'].tolist()[0])

if not cast_list:
    st.write("Cast is not yet available")

s = ''
for i in cast_list:
    s += "<li style='font-size: 16px; display: inline-block;'>" + i + "</li>"

st.markdown("<ol>"+s+"</ol>", unsafe_allow_html = True)
