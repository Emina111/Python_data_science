# Python_data_science
In this file there are two .csv files that contain certain info about movies.
First one (movies.csv) contains columns: movieId, title, and the other one (ratings) contain columns (movieId, rating, userId).
Every movie has been rated by more people (userId).
After merging .csv files, I used pivot_table() function to reorganize table, and then corr() function to explore correlations among movies.
The final result is table that contains title of the movie and it's rating, ranked in descending order.
