import pickle
from flask import Flask, request, render_template
from check_genre import check_genre
app = Flask(__name__)

with open('clf_rfc.p', 'rb') as f:
    model = pickle.load(f, encoding='latin1')

with open('features.p', 'rb') as f:
    features = pickle.load(f, encoding='latin1') 

@app.route('/')
def entry_page():
    return render_template('index.html')


@app.route('/predict_genre/', methods=['GET', 'POST'])
def render_message():
    acousticness = request.form['acousticness']
    try:
        acousticness_float = float(acousticness)/100
    except:
        message = "Please enter a number for acousticness"
        return render_template('index.html',
                               message=message)

    danceability = request.form['danceability']
    try:
        danceability_float = float(danceability)/100
    except:
        message = "Please enter a number for danceability"
        return render_template('index.html',
                               message=message)

    energy = request.form['energy']
    try:
        energy_float = float(energy)/100
    except:
        message = "Please enter a number for energy"
        return render_template('index.html',
                               message=message)

    instrumentalness = request.form['instrumentalness']
    try:
        instrumentalness_float = float(instrumentalness)/100
    except:
        message = "Please enter a number for instrumentalness"
        return render_template('index.html',
                               message=message)

    liveness = request.form['liveness']
    try:
        liveness_float = float(liveness)/100
    except:
        message = "Please enter a number for liveness"
        return render_template('index.html',
                               message=message)

    speechiness = request.form['speechiness']
    try:
        speechiness_float = float(speechiness)/100
    except:
        message = "Please enter a number for speechiness"
        return render_template('index.html',
                               message=message)

    tempo = request.form['tempo']
    try:
        tempo_float = float(tempo)
    except:
        message = "Please enter a number for tempo"
        return render_template('index.html',
                               message=message)

    valence = request.form['valence']
    try:
        valence_float = float(valence)/100
    except:
        message = "Please enter a number for valence"
        return render_template('index.html',
                               message=message)
    
    artist_discovery = request.form['artist_discovery']
    try:
        artist_discovery_float = float(artist_discovery)/100
    except:
        message = "Please enter a number for artist discovery"
        return render_template('index.html',
                               message=message)
    
    artist_familiarity = request.form['artist_familiarity']
    try:
        artist_familiarity_float = float(artist_familiarity)/100
    except:
        message = "Please enter a number for artist familiarity"
        return render_template('index.html',
                               message=message)
    
    artist_hotttnesss = request.form['artist_hotttnesss']
    try:
        artist_hotttnesss_float = float(artist_hotttnesss)/100
    except:
        message = "Please enter a number for artist hotness"
        return render_template('index.html',
                               message=message)
    
    message, image = check_genre(acousticness_float,
                            danceability_float,
                            energy_float,
                            instrumentalness_float,
                            liveness_float,
                            speechiness_float,
                            tempo_float,
                            valence_float,
                            artist_discovery_float,
                            artist_familiarity_float,
                            artist_hotttnesss_float,
                            model)


    return render_template('index.html',
                           message=message,
                           )

if __name__ == '__main__':
    app.run(debug=True)