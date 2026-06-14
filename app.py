import streamlit as st
# import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

# @st.cache_data
# def load_data():
#     movies = pickle.load(open("movies.pkl", "rb"))
#     similarity = pickle.load(open("similarity.pkl", "rb"))
#     return movies, similarity

@st.cache_data
def load_data():

    movies = pd.read_csv(
        "data/processed_movies.csv"
    )

    tfidf = TfidfVectorizer(
        max_features=5000,
        stop_words="english"
    )

    vectors = tfidf.fit_transform(
        movies["tags"]
    ).toarray()

    similarity = cosine_similarity(vectors)

    return movies, similarity

movies, similarity = load_data()

# ==========================================
# RECOMMENDATION FUNCTION
# ==========================================

def recommend(movie_name, top_n=5):

    try:

        movie_index = movies[
            movies['title'] == movie_name
        ].index[0]

        distances = similarity[movie_index]

        movie_list = sorted(
            list(enumerate(distances)),
            key=lambda x: x[1],
            reverse=True
        )[1:top_n+1]

        recommendations = []

        for i in movie_list:

            recommendations.append({
                "title": movies.iloc[i[0]].title,
                "score": round(i[1] * 100, 2)
            })

        return recommendations

    except:
        return []


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("⚙ Settings")

top_n = st.sidebar.slider(
    "Number of Recommendations",
    min_value=5,
    max_value=20,
    value=5
)

show_score = st.sidebar.checkbox(
    "Show Similarity Score",
    value=True
)

# ==========================================
# HEADER
# ==========================================

st.title("🎬 Movie Recommendation System")

# st.markdown("""
# Get movie recommendations using **Content-Based Filtering**
# powered by **NLP**, **Vectorization**, and **Cosine Similarity**.
# """)

st.divider()

# ==========================================
# DATASET STATS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Movies",
        f"{len(movies):,}"
    )

with col2:
    st.metric(
        "Recommendation Engine",
        "Content Based"
    )

with col3:
    st.metric(
        "Algorithm",
        "Cosine Similarity"
    )

st.divider()

# ==========================================
# SEARCH MOVIE
# ==========================================

search_text = st.text_input(
    "🔍 Search Movie",
    placeholder="Type movie name..."
)

selected_movie = None

if search_text:

    filtered_movies = movies[
        movies['title'].str.contains(
            search_text,
            case=False,
            na=False
        )
    ]['title'].tolist()

    if len(filtered_movies) > 0:

        selected_movie = st.selectbox(
            "Select Movie",
            filtered_movies
        )

    else:

        st.warning(
            "No matching movie found."
        )

# ==========================================
# RECOMMEND BUTTON
# ==========================================

if selected_movie:

    if st.button(
        "🎯 Get Recommendations",
        use_container_width=True
    ):

        with st.spinner(
            "Finding similar movies..."
        ):

            recommendations = recommend(
                selected_movie,
                top_n
            )

        st.success(
            f"Movies similar to '{selected_movie}'"
        )

        st.divider()

        cols = st.columns(5)

        for idx, movie in enumerate(recommendations):

            with cols[idx % 5]:

                st.markdown(
                    f"### 🎬 {movie['title']}"
                )

                if show_score:

                    st.progress(
                        min(
                            int(movie['score']),
                            100
                        )
                    )

                    st.write(
                        f"Match Score: {movie['score']}%"
                    )

