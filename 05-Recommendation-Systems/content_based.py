import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 50)
pd.set_option('display.expand_frame_repr', False)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("hafta_5/datasets/the_movies_dataset/movies_metadata.csv", low_memory=False)
df = df.head(10000)
df.shape

df["overview"].head()

tfidf = TfidfVectorizer(stop_words='english')

df["overview"] = df["overview"].fillna('')

tfidf_matrix = tfidf.fit_transform(df["overview"])

 # tfidf_matrix.toarray()

tfidf_matrix.shape

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

cosine_sim.shape
cosine_sim[1]

##################################################################

indices = pd.Series(df.index, index=df["title"])

indices.index.value_counts()

indices = indices[~indices.index.duplicated(keep='last')]

indices["The Hunchback of Notre Dame"]

movie_index = indices["The Hunchback of Notre Dame"]

cosine_sim[movie_index]

similarities_scores = pd.DataFrame(cosine_sim[movie_index], columns=["score"])

movie_indices = similarities_scores.sort_values("score", ascending=False)[1:11].index

df["title"].iloc[movie_indices]

###################################################################

def content_based_recommender(title, cosine_sim, dataframe):
    # index'leri olusturma
    indices = pd.Series(dataframe.index, index=dataframe['title'])
    indices = indices[~indices.index.duplicated(keep='last')]
    # title'ın index'ini yakalama
    movie_index = indices[title]
    # title'a gore benzerlik skorlarını hesapalama
    similarity_scores = pd.DataFrame(cosine_sim[movie_index], columns=["score"])
    # kendisi haric ilk 10 filmi getirme
    movie_indices = similarity_scores.sort_values("score", ascending=False)[1:11].index
    return dataframe['title'].iloc[movie_indices]

content_based_recommender("The Matrix", cosine_sim, df)

def calculate_cosine_sim(dataframe):
    tfidf = TfidfVectorizer(stop_words='english')
    dataframe['overview'] = dataframe['overview'].fillna('')
    tfidf_matrix = tfidf.fit_transform(dataframe['overview'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

cosine_sim = calculate_cosine_sim(df)
content_based_recommender('The Matrix', cosine_sim, df)

