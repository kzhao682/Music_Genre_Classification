# Overview:

Scientific research has proven that music can improve the health and wellbeing of listeners. Humans naturally favor
listening to music that sounds similar to what they are already familiar with. There are many platforms nowadays, such as
Spotify and Soundcloud, that recommend similar-sounding music in order to improve users' music experience. Another general 
approach to enriching a listener's experience is recommending similar genres.

This project uses supervised learning to classify songs based on audio features. The best model used a random forest classifier
to produce an R-squared score of 0.746. This was a significant improvement over the baseline model, which scored 0.451.
Using the probabilities of each classification, I was also able to recommend the second most probable genre as the most 
similar genre.

# Data:

The data comprised of songs from the Free Music Archive, an interactive library of high-quality, legal audio downloads
directed by WFMU, the most renowned freeform radio station in America. The audio features were extracted for each song
using the Echonest API, which is also used in Spotify.

# Tools:

- `Scikit-learn` - K-nearest neighbors, logistic regression, and random forest classification models
- `Bokeh` - condensed bar plots for similar genres
- `Plot.ly` - chord diagram to map out genre similarity
- `Flask` - interactive app to predict genre and second most probable genre
