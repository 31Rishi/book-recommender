import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load data safely (skip corrupted rows)
books = pd.read_csv("Books.csv", on_bad_lines='skip', encoding="latin-1")
ratings = pd.read_csv("Ratings.csv", on_bad_lines='skip', encoding="latin-1")

# Clean and select relevant columns
books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication']]
books.columns = ['isbn', 'title', 'author', 'year']
ratings = ratings[['User-ID', 'ISBN', 'Book-Rating']]
ratings.columns = ['user_id', 'isbn', 'rating']

# Merge ratings with books
merged = ratings.merge(books, on='isbn')

# Filter: keep only books with ≥50 ratings
book_counts = merged['title'].value_counts()
common_books = book_counts[book_counts >= 50].index
filtered = merged[merged['title'].isin(common_books)]

# Create pivot table: books x users
book_pivot = filtered.pivot_table(index='title', columns='user_id', values='rating').fillna(0)

# Compute similarity
similarity = cosine_similarity(book_pivot)

# Save to .pkl files
pickle.dump(book_pivot.reset_index(), open('books.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ books.pkl and similarity.pkl created succes.")
