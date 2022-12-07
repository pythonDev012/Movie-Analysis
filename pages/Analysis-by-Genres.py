import streamlit as st
from Data import movies_df
import altair as alt
import pandas as pd

ops = ['Action']
rev_action = 0
rev_adv = 0
rev_hor = 0
rev_anim = 0
rev_fant = 0
rev_crim = 0
rev_thr = 0
rev_mys = 0
rev_dr = 0
rev_comic = 0
rev_his = 0
rev_tv = 0
rev_wes = 0
rev_sci = 0
rev_rom = 0

for i in movies_df['Genres']:
    if 'Action' in i:
        rev_action += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Adventure' in i:
        rev_adv += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Animation' in i:
        rev_anim += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Horror' in i:
        rev_hor += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Fantasy' in i:
        rev_fant += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Crime' in i:
        rev_crim += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Mystery' in i:
        rev_mys += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Comedy' in i:
        rev_comic += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'History' in i:
        rev_his += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'TV Show' in i:
        rev_tv += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Western' in i:
        rev_wes += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Science Fiction' in i:
        rev_sci += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Romance' in i:
        rev_rom += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Thriller' in i:
        rev_thr += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
    elif 'Drama' in i:
        rev_dr += int(movies_df[movies_df['Genres'] == i]['Revenue'].tolist()[0])
# TV Shows are not included because revenue of TV Shows is 0 or unknown.
revenue = [rev_dr,rev_action,rev_adv,rev_anim,rev_wes,rev_mys,rev_crim,rev_his,rev_comic,rev_fant,rev_rom,rev_sci,rev_thr,rev_hor]
genres = ['Drama','Action','Adventure','Animation','Western','Mystery','Crime','History','Comedy','Fantasy','Romance','Science Fiction','Thriller','Horror']
gen_rev = pd.DataFrame({'Genres':genres, 'Revenue':revenue})

st.altair_chart(alt.Chart(gen_rev).mark_bar().encode(x = alt.X('Genres', title = "Movie Genre", axis= alt.Axis(labelAngle = -45)), y = alt.Y('Revenue', title = 'Revenue (in USD)')).properties(width = 800,height = 500).configure_scale(bandPaddingInner=0.2))

st.altair_chart(alt.Chart(movies_df).mark_bar().encode(x = alt.X('Rating', title = "Ratings", axis= alt.Axis(labelAngle = -45)), y = alt.Y('Revenue', title = 'Revenue (in USD)')).properties(width = 800,height = 500).configure_scale(bandPaddingInner=0.2))
