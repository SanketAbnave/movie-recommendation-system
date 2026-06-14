# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using **Python, NLP, Machine Learning, and Streamlit**. The application recommends similar movies based on movie metadata such as genres, keywords, cast, crew, and plot overview using **Cosine Similarity**.

---

## 📌 Project Overview

Recommendation systems are widely used by platforms such as Netflix, Amazon Prime, YouTube, and Spotify to improve user experience through personalized suggestions.

This project implements a **Content-Based Filtering** approach that analyzes movie features and recommends movies with similar content.

---

## 🚀 Features

* 🔍 Search movies by title
* 🎯 Get Top-N similar movie recommendations
* 📊 Interactive Streamlit dashboard
* ⚡ Fast recommendation generation using similarity matrices
* 🧠 NLP-based feature engineering
* 📈 Similarity score visualization
* 🎨 Professional and responsive user interface

---

## 🏗️ Project Workflow

### 1. Data Collection

Dataset Source:

* TMDB 5000 Movies Dataset

Files Used:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

---

### 2. Data Preprocessing

Performed the following preprocessing steps:

* Removed missing values
* Merged movie and credit datasets
* Extracted:

  * Genres
  * Keywords
  * Cast
  * Director
  * Overview
* Removed spaces from names
* Converted text to lowercase
* Applied stemming using NLTK

---

### 3. Feature Engineering

Created a unified feature called **tags** by combining:

* Overview
* Genres
* Keywords
* Cast
* Director

Example:

```text
Action Adventure ScienceFiction SamWorthington JamesCameron Pandora Alien Future
```

---

### 4. Text Vectorization

Converted movie tags into numerical vectors using:

```python
CountVectorizer(max_features=5000, stop_words='english')
```

---

### 5. Similarity Calculation

Calculated pairwise movie similarity using:

```python
cosine_similarity()
```

This generates a similarity matrix used for recommendation generation.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* NLTK
* Pickle

### Visualization & Deployment

* Streamlit

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── Movie Recommendation System.ipynb
├── requirements.txt
├── README.md
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
└── .streamlit/
    └── config.toml
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## 📈 Example Recommendation

### Input

```text
Avatar
```

### Output

```text
Aliens
Battle: Los Angeles
Aliens vs Predator: Requiem
Apollo 18
Titan A.E.
```

---

## 🎯 Machine Learning Concepts Used

* Natural Language Processing (NLP)
* Feature Engineering
* Text Vectorization
* Cosine Similarity
* Recommendation Systems
* Content-Based Filtering

---

## 🔮 Future Improvements

* Integrate TMDB API for movie posters
* Display ratings and release dates
* Add movie trailers
* Implement fuzzy search
* Use TF-IDF Vectorizer
* Use Sentence Transformers for semantic recommendations
* Hybrid Recommendation System (Content + Collaborative Filtering)
* Deploy on Streamlit Cloud

---

## 📊 Skills Demonstrated

This project showcases proficiency in:

* Data Cleaning
* Data Preprocessing
* Feature Engineering
* Machine Learning
* Recommendation Systems
* NLP
* Python Development
* Streamlit Deployment
* Git & GitHub

---

## 👨‍💻 Author

**Sanket Abnave**

Data Analyst | Aspiring Data Scientist | Python Developer

GitHub: https://github.com/SanketAbnave

LinkedIn: Add Your LinkedIn Profile Here

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
