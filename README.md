# 🎬 Movie Recommendation System

This is a **Content-Based Movie Recommender System** that suggests movies similar to the one you select. It uses **Natural Language Processing (NLP)** techniques to analyze movie metadata and return recommendations based on cosine similarity.

![System Screenshot](assets/scond_screen.png)

## **[App Link](https://movi-recommender.streamlit.app/) --> https://movi-recommender.streamlit.app/**

## 📌 Project Overview

The goal of this project is to build a practical movie recommendation\
engine that can answer:

> **"If I like this movie, which other movies are similar to it?"**

The system uses a **Content-Based Filtering** approach. Instead of\
depending on ratings from other users, it analyzes the characteristics\
of each movie and compares them with the selected movie.

The recommendation process is based on:

- Movie metadata
- Natural Language Processing
- Text vectorization
- Cosine similarity
- Precomputed similarity matrices
- Streamlit interactive UI
- TMDB API for movie posters

---

## ✨ Key Features

- 🎬 Search and select a movie from the available dataset
- 🤖 Generate movie recommendations based on content similarity
- 🧠 NLP-based metadata processing
- 📊 Convert movie metadata into numerical vectors
- 📐 Calculate similarity using **Cosine Similarity**
- 🖼️ Fetch movie posters using the **TMDB API**
- 🌐 Interactive web interface built with **Streamlit**
- 💾 Save trained/precomputed data using **Pickle**
- 📓 Reproducible data preprocessing and model-building notebook
- 📁 Organized project structure for application, models, datasets,\
  and routes

---

## 🧠 Recommendation Approach

This project uses **Content-Based Filtering**.

Each movie is represented using a combined text description created from\
relevant metadata, such as:

- Genres
- Keywords
- Cast
- Crew
- Movie information

The text is then converted into numerical features using\
`CountVectorizer`.

### Recommendation Pipeline

```text
Movie Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Feature Selection
     │
     ▼
Metadata Combination
     │
     ▼
Text Vectorization
     │
     ▼
CountVectorizer
     │
     ▼
Movie Feature Vectors
     │
     ▼
Cosine Similarity
     │
     ▼
Similarity Matrix
     │
     ▼
Top Similar Movies
     │
     ▼
Streamlit Application
     │
     ▼
TMDB Poster API
```

---

## 🔍 Types of Recommender Systems

There are three common recommendation approaches:

### 1. Content-Based Filtering

Recommends items that are similar to items based on their features or\
characteristics.

**Used in this project.**

Example:

> If you select an action movie with specific genres, actors, keywords,\
> and crew members, the system searches for other movies with similar\
> metadata.

### 2. Collaborative Filtering

Recommends items based on the behavior and preferences of similar users.

Example:

> Users who liked Movie A also liked Movie B.

### 3. Hybrid Recommendation

Combines both:

- Content-Based Filtering
- Collaborative Filtering

This project currently focuses on **Content-Based Filtering**.

---

## 📊 Dataset

The project uses movie data from **TMDB (The Movie Database)**.

The main datasets are:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

The data contains information that can be used to describe and compare\
movies.

### Main Metadata Used

The preprocessing workflow combines relevant movie information into a\
single metadata representation, including:

- Genres
- Keywords
- Cast
- Crew
- Movie-related descriptive information

### Data Source

[TMDB - The Movie Database](https://www.themoviedb.org/)

> The dataset is used for educational and machine-learning purposes.

---

## ⚙️ Machine Learning Methodology

### 1. Data Preprocessing

The raw movie datasets are cleaned and prepared for machine learning.

The workflow includes:

- Loading the movie and credits datasets
- Selecting useful columns
- Handling missing values
- Converting structured metadata into usable text
- Extracting information from nested fields
- Combining important movie features

The final result is a **combined metadata string** for each movie.

---

### 2. Feature Engineering

The selected movie features are combined into a single textual\
representation.

Conceptually:

```text
genres + keywords + cast + crew + other metadata
                    ↓
          combined movie tags
```

This allows the recommendation system to compare movies based on their\
content.

---

### 3. Text Vectorization

The project uses:

```python
CountVectorizer
```

from `scikit-learn`.

The vectorizer converts movie metadata into numerical feature vectors.

The project uses a maximum vocabulary size of approximately **5,000**\
**features**.

Example:

```text
Movie Metadata
      ↓
CountVectorizer
      ↓
Numerical Feature Vector
```

---

### 4. Cosine Similarity

After converting movies into vectors, the system calculates the\
similarity between movies using:

```python
cosine_similarity()
```

Cosine similarity measures how similar two vectors are based on their\
orientation.

The resulting similarity matrix is used to identify the movies closest\
to the selected movie.

Conceptually:

```text
Selected Movie
      ↓
Find corresponding vector
      ↓
Compare with all movie vectors
      ↓
Calculate cosine similarity
      ↓
Sort similarity scores
      ↓
Select top recommendations
```

---

## 🎯 Recommendation Process

When a user selects a movie:

1. The application finds the selected movie in the movie dataset.
2. Its index is retrieved.
3. The corresponding similarity scores are obtained.
4. Movies are sorted by similarity.
5. The most similar movies are selected.
6. Movie information is displayed.
7. Posters are retrieved through the TMDB API.

This produces a simple and interactive recommendation experience.

---

## 🖥️ Application Interface

The user interface is implemented using **Streamlit**.

The application provides:

- Movie selection/search
- Recommendation controls
- Movie details
- Recommended movie results
- Movie posters
- Similarity-based recommendations

### Application Preview

```{=html}
<p align="center">
```

`<img src="assets/scond_screen.png" alt="Movie Recommendation System" width="900">`{=html}

```{=html}
</p>
```

---

## 🧰 Technologies Used

Category               Technology

---

Programming Language   Python\
Web Framework          Streamlit\
Data Processing        Pandas\
Machine Learning       Scikit-learn\
NLP                    CountVectorizer\
Similarity Metric      Cosine Similarity\
Serialization          Pickle\
API                    TMDB API\
Development            Jupyter Notebook / VS Code / PyCharm\
Dataset                TMDB 5000 Movies Dataset\
Version Control        Git / GitHub

---

## 📦 Python Libraries

Main libraries used in the project:

```text
pandas
scikit-learn
streamlit
requests
pickle
```

The complete dependency list is available in:

```text
requirements.txt
```

---

## 📁 Project Structure

```text
movie-recommendation-system/
│
├── assets/
│   ├── first_screen
│   ├── scond_screen
│   └── third_screen
│
├── datasets/
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
│
├── models/
│   ├── movie_dict.pkl
│   ├── movies.pkl
│   └── similarity.pkl
│
├── notebooks/
│   └── movie_recommender_system.ipynb
│
├── routes/
│   ├── __init__.py
│   ├── convert.py
│   ├── recommend.py
│   └── stem.py
│
├── src/
│   ├── __init__.py
│   ├── app.py
│  
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 📄 Important Files

### `src/app.py`

The main Streamlit application responsible for running the\
recommendation interface.

### `notebooks/movie_recommender_system.ipynb`

Contains the main data science workflow:

- Data loading
- Data exploration
- Preprocessing
- Feature engineering
- Vectorization
- Similarity calculation
- Model preparation

### `models/movie_dict.pkl`

Serialized movie data used by the application.

### `models/movies.pkl`

Serialized/prepared movie dataset used by the recommendation system.

### `models/similarity.pkl`

Precomputed cosine similarity information used to generate\
recommendations.

### `routes/recommend.py`

Contains recommendation-related functionality.

### `routes/convert.py`

Contains data conversion/processing functionality used by the project.

### `requirements.txt`

Contains the Python dependencies required to run the project.

### `LICENSE`

Project license information.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd movie-recommendation-system
```

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 TMDB API Configuration

The application uses the **TMDB API** to retrieve movie poster\
information.

Create a TMDB account and obtain an API key from TMDB.

Then configure the API key in the application according to the\
implementation in `src/app.py`.

### Important

Do **not** upload a private API key directly to GitHub.

Instead, use an environment variable or another secure configuration\
method.

Example:

```text
TMDB_API_KEY=your_api_key_here
```

If the project uses a `.env` file, make sure it is included in\
`.gitignore`.

---

## ▶️ Run the Application

From the project root:

```bash
streamlit run src/app.py
```

After Streamlit starts, open the local URL shown in the terminal,\
usually:

```text
http://localhost:8501
```

---

## 🧪 How to Use

1. Start the Streamlit application.
2. Open the application in your browser.
3. Search for or select a movie.
4. Choose the number of recommendations if supported by the interface.
5. Submit the recommendation request.
6. The system calculates similarity.
7. The most similar movies are displayed.
8. Posters are retrieved through TMDB.

---

## 📈 Model Output

The recommendation engine produces a ranked list of movies according to\
their similarity with the selected movie.

Example workflow:

```text
Input:
The Dark Knight

        ↓

Movie Metadata

        ↓

Feature Vector

        ↓

Cosine Similarity

        ↓

Similarity Ranking

        ↓

Recommended Movies
```

The recommendations are based on **movie content similarity**, not on\
user ratings or user-to-user behavior.

---

## 🧪 Testing

The repository contains testing scripts under:

```text
src/test.py
src/test2.py
```

These can be used to test parts of the recommendation logic and\
application behavior during development.

---

## 🧩 Project Architecture

The project can be viewed as four main layers:

### Data Layer

Responsible for:

- TMDB datasets
- Movie metadata
- Credits
- Keywords
- Genres
- Cast
- Crew

### Machine Learning Layer

Responsible for:

- Feature engineering
- Text preprocessing
- CountVectorizer
- Feature vectors
- Cosine similarity
- Recommendation ranking

### Application Layer

Responsible for:

- Streamlit interface
- User interaction
- Movie selection
- Recommendation display

### External API Layer

Responsible for:

- Retrieving movie posters
- Connecting the application with TMDB services

---

## 💡 Why Content-Based Filtering?

Content-based filtering is suitable for this project because movie\
metadata provides useful information for measuring similarity.

For example, two movies may be considered similar when they share:

- Similar genres
- Similar keywords
- Similar actors
- Similar crew members
- Similar descriptive metadata

This approach also does not require a large user-rating history.

---

## ⚠️ Limitations

The current implementation has several limitations:

- Recommendations depend on the quality of movie metadata.
- Content-based recommendations may become repetitive.
- The system does not currently learn individual user preferences.
- It does not use collaborative user-rating information.
- Similarity does not necessarily mean that a user will personally\
  enjoy the movie.
- TMDB poster retrieval requires API connectivity and valid API\
  configuration.
- The recommendation quality depends on the selected features and\
  preprocessing strategy.

---

## 🔮 Future Improvements

Possible future improvements include:

### Recommendation Improvements

- Add Collaborative Filtering
- Build a Hybrid Recommendation System
- Add user profiles and personalized recommendations
- Add movie ratings
- Improve feature weighting
- Experiment with TF-IDF
- Experiment with word embeddings
- Use transformer-based text representations

### Application Improvements

- Add authentication
- Add user watchlists
- Add favorites
- Add rating functionality
- Add movie filtering by genre/year/rating
- Improve search
- Add detailed movie pages
- Improve responsive UI

### Machine Learning Improvements

- Evaluate recommendation quality using ranking metrics
- Compare CountVectorizer with TF-IDF
- Experiment with semantic similarity
- Tune feature extraction
- Reduce redundant metadata
- Improve handling of missing values

### Deployment

The application can be deployed using platforms such as:

- Streamlit Community Cloud
- Docker
- Cloud hosting platforms
- A personal server

---

## 📚 Learning Outcomes

Through this project, the following concepts were practiced:

- Python programming
- Pandas data processing
- Data cleaning
- Feature engineering
- Natural Language Processing
- Text vectorization
- CountVectorizer
- Cosine similarity
- Machine learning pipelines
- Model/data serialization
- REST API usage
- Streamlit application development
- Git and GitHub project organization

---

## 🏆 Project Highlights

This project demonstrates an end-to-end machine learning workflow:

```text
Raw Data
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
NLP / Text Processing
   ↓
CountVectorizer
   ↓
Cosine Similarity
   ↓
Recommendation Engine
   ↓
Serialized Models
   ↓
Streamlit Web Application
   ↓
TMDB Poster API
```

It combines **Data Science + NLP + Machine Learning + API Integration +**\
**Web Application Development** in one practical project.

---

## 👨‍💻 Author

**Abdullah Khamis**

Computer Science / Computers & Information Student

Interested in:

- Machine Learning
- Artificial Intelligence
- Data Science
- Natural Language Processing
- Cybersecurity

---

## 📜 License

This project is provided for educational and portfolio purposes.

See the [`LICENSE`](LICENSE) file for the applicable license.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on\
GitHub.
