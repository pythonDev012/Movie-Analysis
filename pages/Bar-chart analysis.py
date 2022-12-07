import streamlit as st
from Data import movies_df
import altair as alt

sort_by = st.selectbox("Select criteria to sort by",('Revenue','Rating','Popularity'))
if sort_by== 'Revenue':
    n = st.slider('Select a value',5, 20, 10)
    st.subheader(f'Top {n} Movies by Revenue (in USD)')
    st.altair_chart(alt.Chart(movies_df.sort_values(by = "Revenue", ascending=False).head(n)).mark_bar().encode(x = alt.X('Title', title = "Movie Title", axis= alt.Axis(labelAngle = -45)), color = 'Revenue', y = alt.Y('Revenue', title = 'Revenue')).properties(width = 790,height = 500).configure_scale(bandPaddingInner=0.2))
    
elif sort_by == 'Rating':
    n = st.slider('Select a value',5, 20, 10)
    st.subheader(f'Top {n} Movies/TV Shows by Rating (out of 10)')
    st.altair_chart(alt.Chart(movies_df.sort_values(by = "Rating", ascending=False).head(n)).mark_bar().encode(x = alt.X('Title', title = "Movie Title", axis= alt.Axis(labelAngle = -45)), color = 'Rating', y = alt.Y('Rating', title = 'Rating')).properties(width = 790,height = 500).configure_scale(bandPaddingInner=0.2))
    
elif sort_by == 'Popularity':
    n = st.slider('Select a value',5, 20, 10)
    st.subheader(f'Top {n} Movies by Popularity')
    st.altair_chart(alt.Chart(movies_df.sort_values(by = "Popularity", ascending=False).head(n)).mark_bar().encode(x = alt.X('Title', title = "Movie Title", axis= alt.Axis(labelAngle = -45)), color = 'Popularity', y = alt.Y('Popularity', title = 'Popularity')).properties(width = 790,height = 500).configure_scale(bandPaddingInner=0.2))

ops = st.multiselect("Select genres",['Action','Animation','Adventure','Fantasy','Horror','Crime','Thriller','Mystery','Drama','Comedy','History','TV Movie','Western','Science Fiction','Romance'])
if len(movies_df[movies_df['Genres'] == str(list(ops))]) != 0:
    st.write(movies_df[movies_df['Genres'] == str(list(ops))])
else:
    st.write("No movie with given genres")