# Retrieve data from TMDB using API

import requests as req
import pandas as pd
from conf import api_key

ses = req.session()

genre_api = 'https://api.themoviedb.org/3/genre/movie/list?api_key=' + api_key + '&language=en-US&page=1'

g = ses.get(genre_api)
genres = g.json()
g_id = []
g_name = []
for i in genres['genres']:
    g_id.append(i['id'])
    g_name.append(i['name'])

ids = []
titles = []
desc = []
pop = []
rate = []
date = []
resp = []
genre = []
rev = []


for k in range(1,500): # Returns 7387 movies as data
    api = 'https://api.themoviedb.org/3/movie/popular?api_key=' + api_key + '&language=en-US&page='+str(k)
    data = ses.get(api)
    j = data.json()
    for i in j['results']:
        if i['original_language'] == 'en':
            try:
                ids.append(i['id'])
            except:
                ids.append(None)
            try:
                titles.append(i['title'])
            except:
                titles.append(None)
            try:
                desc.append(i['overview'])
            except:
                desc.append(None)
            try:
                pop.append(i['popularity'])
            except:
                pop.append(None)
            try:
                rate.append(i['vote_average'])
            except:
                rate.append(None)
            try:
                date.append(i['release_date'])
            except:
                date.append(None)
            try:
                resp.append(i['vote_count'])
            except:
                resp.append(None)
            try:
                p = []
                for u in range(len(i['genre_ids'])):
                    if i['genre_ids'][u] in g_id:
                        p.append(g_name[g_id.index(i['genre_ids'][u])])
                genre.append(p)
            except:
                genre.append(None)
            try:
                rev_api = 'https://api.themoviedb.org/3/movie/' + str(i['id']) + '?api_key=' + api_key + '&language=en-US'
                r = ses.get(rev_api)
                re = r.json()
                rev.append(re['revenue'])
            except:
                rev.append(None)

df = pd.DataFrame({'Id':ids, 'Title':titles,'Description':desc,'Popularity':pop,'Genres':genre,'Release Date': date,'Rating':rate,'Vote Count':resp,'Revenue':rev})
df.to_csv('movies2.csv')