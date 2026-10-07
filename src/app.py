import streamlit as st
import pickle
import io
import pandas as pd
import requests


url = "https://huggingface.co/0xabdo404/movie-recommendation-system/resolve/main/models/similarity.pkl"

response = requests.get(url)
similarity = pickle.load(io.BytesIO(response.content))

st.set_page_config(
    page_title="MovieRec",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Markdown for custom CSS styling
st.markdown("""
<style>

    /* Main application */
    .stApp {
        background: #0e1117;
    }

    /* Main title */
    .main-title {
        font-size: 46px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #9ca3af;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* Section title */
    .section-title {
        font-size: 26px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 18px;
    }

    /* Movie card */
    .movie-card {
        background: #171a21;
        border: 1px solid #282c36;
        border-radius: 14px;
        padding: 12px;
        min-height: 100px;
    }

    .movie-card:hover {
        border-color: #6366f1;
    }

    .movie-title {
        font-size: 16px;
        font-weight: 700;
        margin-top: 10px;
        line-height: 1.3;
    }

    .movie-meta {
        color: #9ca3af;
        font-size: 13px;
        margin-top: 6px;
    }

    .similarity {
        color: #818cf8;
        font-weight: 700;
        font-size: 14px;
        margin-top: 5px;
    }

    /* Selected movie */
    .movie-details {
        background: #171a21;
        border: 1px solid #282c36;
        border-radius: 18px;
        padding: 25px;
    }

    .movie-details h1 {
        font-size: 34px;
        margin-bottom: 10px;
    }

    .overview {
        color: #c4c7ce;
        line-height: 1.7;
        font-size: 15px;
    }

    /* Stats */
    .stat-card {
        background: #171a21;
        border: 1px solid #282c36;
        border-radius: 14px;
        padding: 18px;
        text-align: center;
    }

    .stat-number {
        font-size: 28px;
        font-weight: 800;
    }

    .stat-label {
        color: #9ca3af;
        font-size: 13px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #11141b;
    }

</style>
""", unsafe_allow_html=True)

# API key for The Movie Database (TMDB) API
try:
    TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
except:
    
    TMDB_API_KEY = "f1e2150fed90bb65d97cb10fb7cf5959"

# Load the pre-trained model and data
@st.cache_resource
def load_model():

    movies_dict = pickle.load(
        open(
            "models/movie_dict.pkl",
            "rb"
        )
    )

    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(
        open(
            "models/similarity.pkl",
            "rb"
        )
    )

    return movies, similarity


movies, similarity = load_model()

# Fetch movie details from TMDB API with caching to reduce API calls
@st.cache_data(ttl=3600)
def get_movie_details(movie_id):

    url = (
        f"https://api.themoviedb.org/3/movie/"
        f"{movie_id}"
    )

    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except Exception:

        return {}

# Fetch movie poster URL from TMDB API
def fetch_poster(movie_id):

    data = get_movie_details(movie_id)

    poster_path = data.get("poster_path")

    if poster_path:

        return (
            "https://image.tmdb.org/t/p/w500"
            + poster_path
        )

    return (
        "https://via.placeholder.com/"
        "500x750?text=No+Poster"
    )

# Recommend movies based on similarity
def recommend(movie):

    index = movies[
        movies["title"] == movie
    ].index[0]

    distances = sorted(
        list(
            enumerate(
                similarity[index]
            )
        ),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_scores = []

    # Top 5 recommendations
    for i in distances[1:6]:

        movie_index = i[0]

        movie_id = movies.iloc[
            movie_index
        ].movie_id

        movie_name = movies.iloc[
            movie_index
        ].title

        score = i[1]

        poster = fetch_poster(
            movie_id
        )

        recommended_movie_names.append(
            movie_name
        )

        recommended_movie_posters.append(
            poster
        )

        recommended_scores.append(
            score
        )

    return (
        recommended_movie_names,
        recommended_movie_posters,
        recommended_scores
    )

# Main Streamlit application
st.markdown(
    """
    <div class="main-title">
        🎬 Movie Recommendation System
    </div>

    <div class="subtitle">
        NLP-powered content-based movie recommendation
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar settings
with st.sidebar:

    st.header("⚙️ Settings")

    st.markdown("---")

    st.subheader("🎯 Recommendation")

    number_of_movies = st.slider(
        "Number of recommendations",
        min_value=1,
        max_value=5,
        value=5
    )

    st.markdown("---")

    st.subheader("🧠 Algorithm")

    st.info(
        """
        **Content-Based Filtering**

        Recommendations are generated using
        similarity between movie feature vectors.
        """
    )

    st.markdown("---")

    st.subheader("📊 Dataset")

    st.metric(
        "Total Movies",
        f"{len(movies):,}"
    )

# Search and select a movie
st.markdown(
    '<div class="section-title">🔎 Find a Movie</div>',
    unsafe_allow_html=True
)

search_query = st.text_input(
    "Search",
    placeholder="Search for a movie...",
    label_visibility="collapsed"
)

# Filter movies based on search query
if search_query:

    filtered_movies = movies[
        movies["title"]
        .str.contains(
            search_query,
            case=False,
            na=False
        )
    ]

else:

    filtered_movies = movies

# Display warning if no movies found
if len(filtered_movies) == 0:

    st.warning(
        "No movies found. Try another search."
    )

    st.stop()


selected_movie_name = st.selectbox(
    "Select a movie",
    filtered_movies["title"].values
)

# Fetch and display details of the selected movie
selected_movie_row = movies[
    movies["title"] == selected_movie_name
].iloc[0]

selected_movie_id = selected_movie_row.movie_id

movie_details = get_movie_details(
    selected_movie_id
)

poster = fetch_poster(
    selected_movie_id
)


st.markdown(
    '<div class="section-title">🎥 Movie Details</div>',
    unsafe_allow_html=True
)

info_col1, info_col2 = st.columns(
    [1, 3]
)


with info_col1:

    st.image(
        poster,
        use_container_width=True
    )


with info_col2:

    movie_title = movie_details.get(
        "title",
        selected_movie_name
    )

    rating = movie_details.get(
        "vote_average",
        "N/A"
    )

    release_date = movie_details.get(
        "release_date",
        "N/A"
    )

    overview = movie_details.get(
        "overview",
        "No overview available."
    )

    genres = movie_details.get(
        "genres",
        []
    )

    genre_names = [
        genre["name"]
        for genre in genres
    ]

    genre_text = (
        " • ".join(genre_names)
        if genre_names
        else "Unknown"
    )

    st.markdown(
        f"""
        <div class="movie-details">

        <h1>{movie_title}</h1>

        <p>
        ⭐ <b>{rating:.1f}</b>
        &nbsp;&nbsp;&nbsp;
        📅 <b>{release_date}</b>
        </p>

        <p>
        🎭 <b>{genre_text}</b>
        </p>

        <br>

        <h3>Overview</h3>

        <p class="overview">
        {overview}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("")

recommend_button = st.button(
    "✨ Show Recommendations",
    type="primary",
    use_container_width=True
)


if recommend_button:

    (
        recommended_movie_names,
        recommended_movie_posters,
        recommended_scores
    ) = recommend(
        selected_movie_name
    )

    st.markdown(
        '<div class="section-title">'
        '✨ Recommended Movies'
        '</div>',
        unsafe_allow_html=True
    )


    cols = st.columns(
           number_of_movies
       )
   
    for i in range(
           min(
               number_of_movies,
               len(recommended_movie_names)
           )
       ):
   
           with cols[i]:
   
               movie_name = (
                   recommended_movie_names[i]
               )
   
               movie_poster = (
                   recommended_movie_posters[i]
               )
   
               similarity_score = (
                   recommended_scores[i]
               )
   
               movie_row = movies[
                   movies["title"] == movie_name
               ].iloc[0]
   
               movie_id = movie_row.movie_id
   
               details = get_movie_details(
                   movie_id
               )
   
               rating = details.get(
                   "vote_average",
                   0
               )
   
               release_date = details.get(
                   "release_date",
                   ""
               )
   
               year = (
                   release_date[:4]
                   if release_date
                   else "N/A"
               )
   
               with st.container(border=True):
                   st.image(
                       movie_poster,
                       use_container_width=True
                   )
   
                   st.markdown(f"**{movie_name}**")
                   st.caption(
                       f"📅 {year}  •  ⭐ {float(rating):.1f}"
                       if isinstance(rating, (int, float))
                       else f"📅 {year}  •  ⭐ {rating}"
                   )
                   st.markdown(
                       f"🧠 **Similarity: {similarity_score * 100:.1f}%**"
                   )

    st.markdown(
        '<div class="section-title">'
        '🧠 How Were These Movies Recommended?'
        '</div>',
        unsafe_allow_html=True
    )

    st.info(
        """
        The system uses **content-based filtering**.

        The selected movie is compared with other movies
        using the similarity matrix generated during the
        NLP processing stage.

        Higher similarity means the movie has a more similar
        feature representation to the selected movie.

        **Similarity method:** Cosine Similarity
        """
    )


    st.markdown(
        '<div class="section-title">'
        '📊 Recommendation Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    analysis_data = []

    for i in range(
        min(
            number_of_movies,
            len(recommended_movie_names)
        )
    ):

        analysis_data.append({
            "Movie":
                recommended_movie_names[i],

            "Similarity":
                f"{recommended_scores[i] * 100:.2f}%"
        })


    analysis_df = pd.DataFrame(
        analysis_data
    )

    st.dataframe(
        analysis_df,
        use_container_width=True,
        hide_index=True
    )


st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#6b7280;
        padding:20px;
    ">

        🎬 Movie Recommendation System


        Built with Python • NLP • Cosine Similarity • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)