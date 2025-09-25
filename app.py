import streamlit as st
import pickle
import pandas as pd
import requests

api_key = st.secrets["tmdb"]["key"]

# ---------------- Functions ----------------
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        )
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except:
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        if i[0] >= len(movies):
            continue
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# ---------------- Load Data ----------------
movies_dict = pickle.load(open('movies_dict_new.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity_new.pkl','rb'))

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# Centered Title with Theater Icon
st.markdown(
    "<h1 style='text-align: center; color: white;'>🎬 Movie Recommender System</h1>",
    unsafe_allow_html=True
)

# Movie selection dropdown
option = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

# Show recommendations
if st.button("Show Recommendations"):
    names, posters = recommend(option)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        if idx >= len(names):
            break
        with col:
            # Always go to YouTube trailer
            query = names[idx].replace(" ", "+") + "+trailer"
            youtube_link = f"https://www.youtube.com/results?search_query={query}"

            # Clickable title with YouTube link
            st.markdown(f"[{names[idx]}]({youtube_link})")
            st.image(posters[idx])
