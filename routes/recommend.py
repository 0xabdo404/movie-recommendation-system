import pandas as pd
import numpy as np
import ast


# Convert string representation of list of dictionaries to list of names
def recommend(movie):
	movie_index = new_df[new_df['title'] == movie].index[0]
	distances = similarity[movie_index]
	movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

	for _ in movies_list:
		print(new_df.iloc[_[0]].title)