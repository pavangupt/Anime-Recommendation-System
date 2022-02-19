# Anime-Recommendation-System
Now-a-days, almost all the ecommerce or OTT platforms uses recommendation system to recommend to the user.In this project, I am going to built a recommendaton system for recommending anime's to the users with the help of Collaborative Filtering System. Before building such system ,we have to understand "What is Collaborative Based Filtering System"?

## What is Collaborative Filtering Recommendation System?
- In Collaborative Filtering, we tend to find similar users and recommend what similar users like. In this type of recommendation system, we don’t use the features of the item to recommend it, rather we classify the users into the clusters of similar types, and recommend each user according to the preference of its cluster.
- In order to built a recommendation system, we will be using KNN ie. Nearest Neighbors- Cosine Similarity.
 
### Cosine Similarity:-
 - We can apply the cosine distance between two users in the utility matrix, and we can also give the zero value to all the unfilled columns to make calculation easy, if we get smaller cosine then there will be a larger distance between the users and if the cosine is larger then we have a small angle between the users, and we can recommend them similar things.
 - ![cosine similarity](https://user-images.githubusercontent.com/91775600/154799508-4a9ba459-d1e3-471a-9258-bb2a03cb284b.png)

## Table of Content:-
 - 1. INTRODUCTION
 - 2. Importing necessary libraries
 - 3. Reading the dataset
 - 4. Merging rating and anime list data 
   - a. Feature Selection
   - b. Handling Missing Values
   - c. Checking For Datatypes
 - 5. Feature Engineering
   - a. Converting Categorical Variable
 - 6. Model Creation- KNN(Cosine Similiarity)
