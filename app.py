import streamlit as st
import pickle
import pandas as pd

# Load precomputed files
books = pickle.load(open('books.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.set_page_config(page_title="Book Recommendation System", layout="wide")
st.title("📚 Book Recommendation System")

# Get book titles
book_list = books['title'].values

# Dropdown
selected_book = st.selectbox("Select a book to get recommendations:", book_list)

def recommend(book_name):
    index = books[books['title'] == book_name].index[0]
    distances = similarity[index]
    book_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_books = []
    for i in book_indices:
        recommended_books.append(books.iloc[i[0]]['title'])
    return recommended_books

if st.button("Show Recommendations"):
    recommendations = recommend(selected_book)
    st.subheader("Recommended Books:")
    for i, book in enumerate(recommendations):
        st.write(f"{i+1}. {book}")
