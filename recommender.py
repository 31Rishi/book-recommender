# recommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class BookRecommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path, encoding='latin-1')
        self.df = self.df[['Book-Title', 'Book-Author', 'Publisher']]
        self.df.dropna(inplace=True)
        self.df.drop_duplicates(subset='Book-Title', inplace=True)

        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['Book-Title'])
        self.similarity = cosine_similarity(self.tfidf_matrix)

    def recommend(self, book_title, top_n=5):
        if book_title not in self.df['Book-Title'].values:
            return ["Book not found in dataset."]
        
        idx = self.df[self.df['Book-Title'] == book_title].index[0]
        sim_scores = list(enumerate(self.similarity[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]

        recommended_books = [self.df.iloc[i[0]]['Book-Title'] for i in sim_scores]
        return recommended_books
