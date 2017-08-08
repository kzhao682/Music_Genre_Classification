import pandas as pd
import pickle

def check_genre(acousticness_float,danceability_float,energy_float,instrumentalness_float,liveness_float,speechiness_float,tempo_float,valence_float,artist_discovery_float,artist_familiarity_float,artist_hotttnesss_float,model):

	input_df = pd.DataFrame({'acousticness': acousticness_float,
							'danceability': danceability_float,
							'energy': energy_float,
							'instrumentalness': instrumentalness_float,
							'liveness': liveness_float,
							'speechiness': speechiness_float,
							'tempo': tempo_float,
							'valence': valence_float,
							'artist_discovery': artist_discovery_float,
							'artist_familiarity': artist_familiarity_float,
							'artist_hotttnesss': artist_hotttnesss_float}, index=[0])

	prediction = model.predict(input_df)[0]

	message_array = ['Classical', 'Electronic', 'Experimental', 'Folk', 'Hip-Hop', 'Instrumental', 'International', 'Jazz', 'Pop', 'Rock']

	image_array = ['Classical.jpg', 'Electronic.jpg', 'Experimental.jpg', 'Folk.jpg', 'Hip_Hop.jpg', 'Instrumental.jpg', 'International.jpg', 'Jazz.jpg', 'Pop.jpg', 'Rock.jpg']

	return ('You are listening to ' + message_array[prediction], './Images/' + image_array[prediction])

# with open('clf_rfc.p', 'rb') as f:
#     clf_rfc = pickle.load(f, encoding='latin1') 

# print(check_genre(0.5,0.5,0.5,0.5,0.5,0.5,120,0.5,0.5,0.4,0.6,clf_rfc))