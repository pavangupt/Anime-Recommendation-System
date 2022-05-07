import streamlit as st
import pickle

movies_list = pickle.load(open("movies.pkl", "rb"))
movies = movies_list.index
knn_model = pickle.load(open("knn_model.pkl", "rb"))


def recommend(movie):
    user_list = movies_list[movies_list.index == movie]
    distances, indices = knn_model.kneighbors(user_list.values.reshape(1, -1), n_neighbors=6)
    for i in range(0, len(distances.flatten())):
        if i == 0:
            print("\033[1m", "These are the following 5 movies recommeded for--{0}:\n".format(
                movies_list[movies_list.index == movie][0]))
        else:
            print(i, "--", movies_list.index[indices.flatten()[i]])


st.title("Anime Recommendation System")
selected_movies_name = st.selectbox(
    "Select The Movies", movies)

if st.button('Recommend'):
    recommend(selected_movies_name)
    for i in list(recommend(selected_movies_name)):
        st.write(i)
