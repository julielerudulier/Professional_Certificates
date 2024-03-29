## Music Recommendation System

This project was my final project for the Data Analyst Certificate I obtained from L'école des **Mines Paris PSL** in August 2023. It was **my FIRST coding project ever!**

The aim of this project was to build a music recommendation system based on data retrieved from Spotify and Twitter. I used two different ML approaches to solve this problem: clustering and a similarity matrix.

---

#### Language used in this project:
- Python
  
#### Framework:
- Streamlit

#### Librairies:
- Scikit-learn
- Yellowbrick
- Pandas
- Numpy
- Requests
- Json
- Seaborn
- Matplotlib
- SciPy
- Graphviz
- Plotly Express

#### Data:
The database used in this project is a mix of multiple Spotify databases available on [Kaggle.com](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset). The final dataset contains more than 528,000 unique songs, 22,366 unique artists and 63 different genres.

---

#### About the project:
The aim of this project was to build a music recommendation system based on data retrieved from Spotify and Twitter.
I chose to group similar tracks automatically by running a k-means algorithm on the dataset, but I was not very successful in creating self-sufficient clusters. I was still able to use the clusters by adding manual steps and fine-tuning my algorithm to create the first part of the recommendation system.

The second part was based on a similarity matrix. Using the Mahalanobis metric allowed my algorithm to return the best recommendations possible, given the limited number of songs avaible in my dataset.

I achieved my goal as I was able to build a music recommendation system allowing users to choose between two songs similar to a seed song of their liking. Although the relevancy of the recommendations can always be discussed, my system was designed and adjusted so that the songs suggested to users could be considered the most interesting suggestions possible.


With more time, I could have:
  - Searched for additional resources and add songs to the dataset to have a broader selection of tracks to recommend;
  - Run alternative unsupervised algorithms to try and get better results than the clusters created in this project;
  - Designed a review system that would allow me to store ratings of recommendations in a database.


#### Project Timeline
I started working on this project in January 2023. A paper on data cleansing and exploration was first handed in to Faculty members in March. This paper also included data visualizations and a primary analysis of trends in data. A second paper on data modeling was handed in in May. The final essay was handed in to Faculty members in June, while the outcomes of this project as well as the recommendation system were presented to a jury on June 26th, 2023.


#### Streamlit App
If you want to take a closer look at the project and see exactly how I built the recommendation system step by step, I created a Streamlit App that is accessible [here](https://julielerudulier.streamlit.app/).

---

#### Bibliography

Here are the articles and ressources used for the project:
  - Zhang, Z. “Text Mining for Social and Behavioral Research Using R - Chapter 8 Sentiment Analysis”, 2018 [Online], https://books.psychstat.org/textmining/sentiment-analysis.html, (Consulted on January 18th, 2023);
  - Calderon, P. “VADER Sentiment Analysis Explained”, 2017 [Online], https://medium.com/@piocalderon/vader-sentiment-analysis-explained-f1c 4f9101cd9, (Consulted on January 19th, 2023);
  - Beri, A. “Sentimental Analysis Using Vader”, 2020 [Online], https://towardsdatascience.com/sentimental-analysis-using-vader-a3415fef7 664, (Consulted on January 18th, 2023);
  - Al-Shabi, M.A. “Evaluating the performance of the most important Lexicons used to Sentiment analysis and opinions Mining”, 2020 [Online], https://osf.io/exqr9/download, Consulted on January 20th, 2023);
  - Sree, S. “Spotify - Song Prediction and Recommendation System”, 2021 [Online], https://medium.com/swlh/spotify-song-prediction-and-recommendation-sy stem-b3bbc71398ad, (Consulted on March 22nd, 2023);
  - Jones, M. “Making a pairwise distance matrix in pan”, 2021 [Online], https://drawingfromdata.com/pandas/clustering/making-a-pairwise-distanc e-matrix-in-pandas.html, (Consulted on May 9th, 2023);
  - Shukla, S., Khanna P., Kant Agrawal K. “Review on sentiment analysis on music”, 2017 [Online], https://ieeexplore.ieee.org/document/8286111 (Consulted on January 20th, 2023);
  - Gunawan, A. A. S., Suhartono, D. “Music Recommender System Based on Genre using Convolutional Recurrent Neural Networks”, 2019 [Online], https://doi.org/10.1016/j.procs.2019.08.146, (Consulted on January 20th, 2023).
