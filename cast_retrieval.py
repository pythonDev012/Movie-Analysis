import requests as req
import pandas as pd
from Data import movies_df
from conf import api_key

ses = req.session()

crew = []
ids = []
for movie_id in movies_df['Id']:
    ids.append(movie_id)
    cast_api = "https://api.themoviedb.org/3/movie/" + str(movie_id) + '/credits?api_key=' + api_key + '&language=en-US'
    c = ses.get(cast_api)
    casts = c.json()
    movie_cast = []
    try:
        count = 0
        for i in casts["cast"]:
            if count < 5:
                movie_cast.append(i['name'])
                count += 1
        crew.append(movie_cast)
    except:
        crew.append("N/A")
cast_df = pd.DataFrame({"Movie Id":ids, "Cast": crew})
cast_df.to_csv("movie_cast.csv")

