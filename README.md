# dse230_project
## Data Source  
The data can be found on the movies lens website under the `recommended for new research`. This data should be composed of the 25 million movie ratings, 62,000 distinct movies, and 162,000 users. Please download and extract the data into a folder called `data`. See below for the expected file layout.  
https://grouplens.org/datasets/movielens/
## Data layout
Data directory is on same level as repository directory.
## File layout
```
home/work/
    ├──dse230_project
        ├──data_prep
            ├──movies_cleaning.ipynb
            ├──ratings_cleaning.ipynb
        ├──eda
            ├──movies_rating.ipynb
            ├──movies.ipynb
            ├──ratings.ipynb
        ├──models
            ├──cluster_visualization.ipynb
            ├──movie_clusters.ipynb
            ├──movie_recommendation.ipynb
    ├──data
        movies.csv
        ├──ratings.csv
        ├──tags.csv
```
## Running Code
1. For initial EDA, run the `movies.ipynb` and `ratings.ipynb` in the eda directory.
    * this will save graphs of the distribution in the `data` directory
    * Optional: Run `movie_ratings.ipynb` to see a preview of some of the data that would be dropped in cleaning.
    * Optional: Run `tags.ipynb` for an initial view of the tags data. No further work was done with this data past this point
2. Run `movies_cleaning.ipynb` in `data_prep`. This will output 3 directories into `data`.
    * `cleaned_movies`: This will be read in the `ratings_cleaning.ipynb`.
        * Note: If you want to see the new distributions after cleaning. Return back to the `movies.ipynb` notebook in EDA and change the flag for `load_cleaned` to `True`
    * `als_ratings_train`: The train data used to train the recommendation model in `movie_recommendation.ipynb`
    * `als_ratings_test`: The test data used to test the recommendation model in `movie_recommendation.ipynb`
3. Run `ratings_cleaning.ipynb` in `data_prep`. This will output 3 directories into `data`.
    * `cleaned_movies`: Cleaned ratings. This directory can be used in the EDA to see how the distribution changed after cleaning.
        * Note: If you want to see the new distributions after cleaning. Return back to the `ratings.ipynb` notebook in EDA and change the flag for `load_cleaned` to `True`
    * `kmeans_movies_train`: Train data used in `movie_clusters.ipynb` and `cluster_visualization.ipynb`
    * `kmeans_movies_test`: Test data used in `movie_clusters.ipynb` and `cluster_visualization.ipynb`
4. For k-means clustering, run `movie_clusters.ipynb`
    * Note the flag for `fit_model` is set to `False`. Fitting the model takes several hours.
    * Once the model is created, it is automatically saved. Any code after that loads the model saved and works from there.
5. Run `cluster_visualization.ipynb` to see the composition of a few of the clusters.
6. Run `movie_recommendation.ipynb`
    * Note the flag for `fit_model` is set to `False`. Fitting the model takes at least an hour.
    * Note: You will need at least 9.5gb of storage access for fitting to work. The rating_cap set in `ratings_cleaning.ipynb` was optimized to maximize the amount of data to run on a local machine.
    * Once the model is fit, similar to k-means, all future code will load the saved model and work from there to build recommendations and to view the recommendations.
