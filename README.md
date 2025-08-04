📚 Book Recommendation System

A personalized book recommender system built using collaborative filtering and Streamlit for an interactive web interface. It suggests books based on user preferences by analyzing user-book interactions.

🔍 Features

- ✅ User-based collaborative filtering with cosine similarity
- ✅ Interactive UI using Streamlit
- ✅ Real-time recommendations
- ✅ Deployable on Streamlit Cloud or locally

🚀 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Open Library API

📁 Folder Structure

- Data


  -Books.csv


  -Ratings.csv


  -Users.csv

  
-app.py


-recommender.py


-helper.py


-generate.py which generates books.pkl and similarity.pkl

RUN- python generate.py in terminal


-requirements.txt



 Install dependencies

 
pip install -r requirements.txt


 Run the app

 
streamlit run app.py
