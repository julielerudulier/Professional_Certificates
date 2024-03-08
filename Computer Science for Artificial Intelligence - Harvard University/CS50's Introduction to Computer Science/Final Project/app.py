import os
import pandas as pd
import numpy as np
import random

from flask import Flask, flash, render_template, request, session, jsonify
from flask_session import Session

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Import dataframe
df = pd.read_csv("df.csv")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/mode", methods=["GET", "POST"])
def mode():
    return render_template("mode.html")


@app.route("/artist", methods=["GET", "POST"])
def artist():
    if request.method == "GET":
        artists = df["track_artist"].unique().tolist()
        return render_template("artist.html", artists=artists)

    if request.method == "POST":
        data = request.get_json()
        artist = data["artist"]
        dfa = df[df["track_artist"] == artist]
        genre = dfa["subgenre"].mode().item()
        year = int(np.round(dfa["year"].mean(), decimals=0))
        pop = dfa["popularity"].mean()
        dance = dfa["danceability"].mean()
        energy = dfa["energy"].mean()
        loud = dfa["loudness"].mean()
        tempo = dfa["tempo"].mean()
        dfo = df[(df["track_artist"] != artist) & (df["subgenre"] == genre) &
        ((df["year"] <= (year + 5)) | (df["year"] >= (year - 5))) &
        ((df["danceability"] <= (dance + 3)) & (df["danceability"] >= (dance - 3))) &
        ((df["energy"] <= (energy + 10)) & (df["energy"] >= (energy - 10))) &
        ((df["loudness"] <= (loud + 2)) & (df["loudness"] >= (loud - 2))) &
        ((df["tempo"] <= (tempo + 10)) & (df["tempo"] >= (loud - 10))) &
        ((df["popularity"] <= (pop + 20)) | (df["popularity"] >= (pop - 10)))]
        artists = dfo["track_artist"].unique()
        opponent = random.choice(artists)
        return jsonify(opponent=opponent)


@app.route("/fight", methods=["GET", "POST"])
def fight():
    if request.method == "GET":
        return render_template("fight.html")

    if request.method == "POST":
        data = request.get_json()
        artist = data["artist"]
        opponent = data["opponent"]
        def tracks(artist):
            dfa = df[df["track_artist"] == artist]
            lista = dfa["track_name"].unique()
            track1 = random.choice(lista)
            id1 = df[(df["track_name"] == track1) & (df["track_artist"] == artist)]["track_id"].item()
            lista = lista.tolist()
            while(track1 in lista):
                lista.remove(track1)
            track2 = random.choice(lista)
            id2 = df[(df["track_name"] == track2) & (df["track_artist"] == artist)]["track_id"].item()
            while(track2 in lista):
                lista.remove(track2)
            track3 = random.choice(lista)
            id3 = df[(df["track_name"] == track3) & (df["track_artist"] == artist)]["track_id"].item()
            while(track3 in lista):
                lista.remove(track3)
            track4 = random.choice(lista)
            id4 = df[(df["track_name"] == track4) & (df["track_artist"] == artist)]["track_id"].item()
            while(track4 in lista):
                lista.remove(track4)
            track5 = random.choice(lista)
            id5 = df[(df["track_name"] == track5) & (df["track_artist"] == artist)]["track_id"].item()
            return track1, id1, track2, id2, track3, id3, track4, id4, track5, id5
        Atrack1, Aid1, Atrack2, Aid2, Atrack3, Aid3, Atrack4, Aid4, Atrack5, Aid5 = tracks(artist)
        Otrack1, Oid1, Otrack2, Oid2, Otrack3, Oid3, Otrack4, Oid4, Otrack5, Oid5 = tracks(opponent)
        linkA1 = "https://open.spotify.com/embed/track/" + Aid1
        linkA2 = "https://open.spotify.com/embed/track/" + Aid2
        linkA3 = "https://open.spotify.com/embed/track/" + Aid3
        linkA4 = "https://open.spotify.com/embed/track/" + Aid4
        linkA5 = "https://open.spotify.com/embed/track/" + Aid5
        linkO1 = "https://open.spotify.com/embed/track/" + Oid1
        linkO2 = "https://open.spotify.com/embed/track/" + Oid2
        linkO3 = "https://open.spotify.com/embed/track/" + Oid3
        linkO4 = "https://open.spotify.com/embed/track/" + Oid4
        linkO5 = "https://open.spotify.com/embed/track/" + Oid5
        urlA1 = "https://open.spotify.com/track/" + Aid1
        urlA2 = "https://open.spotify.com/track/" + Aid2
        urlA3 = "https://open.spotify.com/track/" + Aid3
        urlA4 = "https://open.spotify.com/track/" + Aid4
        urlA5 = "https://open.spotify.com/track/" + Aid5
        urlO1 = "https://open.spotify.com/track/" + Oid1
        urlO2 = "https://open.spotify.com/track/" + Oid2
        urlO3 = "https://open.spotify.com/track/" + Oid3
        urlO4 = "https://open.spotify.com/track/" + Oid4
        urlO5 = "https://open.spotify.com/track/" + Oid5
        return jsonify(Atrack1=Atrack1, Atrack2=Atrack2, Atrack3=Atrack3, Atrack4=Atrack4, Atrack5=Atrack5,
                    Otrack1=Otrack1, Otrack2=Otrack2, Otrack3=Otrack3, Otrack4=Otrack4, Otrack5=Otrack5,
                    Aid1=Aid1, Aid2=Aid2, Aid3=Aid3, Aid4=Aid4, Aid5=Aid5,
                    Oid1=Oid1, Oid2=Oid2, Oid3=Oid3, Oid4=Oid4, Oid5=Oid5,
                    linkA1=linkA1, linkA2=linkA2, linkA3=linkA3, linkA4=linkA4, linkA5=linkA5,
                    linkO1=linkO1, linkO2=linkO2, linkO3=linkO3, linkO4=linkO4, linkO5=linkO5,
                    urlA1=urlA1, urlA2=urlA2, urlA3=urlA3, urlA4=urlA4, urlA5=urlA5,
                    urlO1=urlO1, urlO2=urlO2, urlO3=urlO3, urlO4=urlO4, urlO5=urlO5)

@app.route("/fights", methods=["GET", "POST"])
def fights():
    if request.method == "GET":
        return render_template("fights.html")

    if request.method == "POST":
        data = request.get_json()
        artist = data["artist"]
        opponent = data["opponent"]
        def tracks(artist):
            dfa = df[df["track_artist"] == artist]
            lista = dfa["track_name"].unique()
            track1 = random.choice(lista)
            id1 = df[(df["track_name"] == track1) & (df["track_artist"] == artist)]["track_id"].item()
            lista = lista.tolist()
            while(track1 in lista):
                lista.remove(track1)
            track2 = random.choice(lista)
            id2 = df[(df["track_name"] == track2) & (df["track_artist"] == artist)]["track_id"].item()
            while(track2 in lista):
                lista.remove(track2)
            track3 = random.choice(lista)
            id3 = df[(df["track_name"] == track3) & (df["track_artist"] == artist)]["track_id"].item()
            while(track3 in lista):
                lista.remove(track3)
            track4 = random.choice(lista)
            id4 = df[(df["track_name"] == track4) & (df["track_artist"] == artist)]["track_id"].item()
            while(track4 in lista):
                lista.remove(track4)
            track5 = random.choice(lista)
            id5 = df[(df["track_name"] == track5) & (df["track_artist"] == artist)]["track_id"].item()
            return track1, id1, track2, id2, track3, id3, track4, id4, track5, id5
        Atrack1, Aid1, Atrack2, Aid2, Atrack3, Aid3, Atrack4, Aid4, Atrack5, Aid5 = tracks(artist)
        Otrack1, Oid1, Otrack2, Oid2, Otrack3, Oid3, Otrack4, Oid4, Otrack5, Oid5 = tracks(opponent)
        linkA1 = "https://open.spotify.com/embed/track/" + Aid1
        linkA2 = "https://open.spotify.com/embed/track/" + Aid2
        linkA3 = "https://open.spotify.com/embed/track/" + Aid3
        linkA4 = "https://open.spotify.com/embed/track/" + Aid4
        linkA5 = "https://open.spotify.com/embed/track/" + Aid5
        linkO1 = "https://open.spotify.com/embed/track/" + Oid1
        linkO2 = "https://open.spotify.com/embed/track/" + Oid2
        linkO3 = "https://open.spotify.com/embed/track/" + Oid3
        linkO4 = "https://open.spotify.com/embed/track/" + Oid4
        linkO5 = "https://open.spotify.com/embed/track/" + Oid5
        urlA1 = "https://open.spotify.com/track/" + Aid1
        urlA2 = "https://open.spotify.com/track/" + Aid2
        urlA3 = "https://open.spotify.com/track/" + Aid3
        urlA4 = "https://open.spotify.com/track/" + Aid4
        urlA5 = "https://open.spotify.com/track/" + Aid5
        urlO1 = "https://open.spotify.com/track/" + Oid1
        urlO2 = "https://open.spotify.com/track/" + Oid2
        urlO3 = "https://open.spotify.com/track/" + Oid3
        urlO4 = "https://open.spotify.com/track/" + Oid4
        urlO5 = "https://open.spotify.com/track/" + Oid5
        return jsonify(Atrack1=Atrack1, Atrack2=Atrack2, Atrack3=Atrack3, Atrack4=Atrack4, Atrack5=Atrack5,
                    Otrack1=Otrack1, Otrack2=Otrack2, Otrack3=Otrack3, Otrack4=Otrack4, Otrack5=Otrack5,
                    Aid1=Aid1, Aid2=Aid2, Aid3=Aid3, Aid4=Aid4, Aid5=Aid5,
                    Oid1=Oid1, Oid2=Oid2, Oid3=Oid3, Oid4=Oid4, Oid5=Oid5,
                    linkA1=linkA1, linkA2=linkA2, linkA3=linkA3, linkA4=linkA4, linkA5=linkA5,
                    linkO1=linkO1, linkO2=linkO2, linkO3=linkO3, linkO4=linkO4, linkO5=linkO5,
                    urlA1=urlA1, urlA2=urlA2, urlA3=urlA3, urlA4=urlA4, urlA5=urlA5,
                    urlO1=urlO1, urlO2=urlO2, urlO3=urlO3, urlO4=urlO4, urlO5=urlO5)


@app.route("/random", methods=["GET", "POST"])
def random_page():
    if request.method == "GET":
        genres = df["track_genre"].unique().tolist()
        return render_template("random.html", genres=genres)

    elif request.method == "POST":
        data = request.get_json()
        main_genre = data["genre"]
        def genres(main_genre):
            dfg = df[df["track_genre"] == main_genre]
            artists = dfg["track_artist"].unique()
            artist = random.choice(artists)
            dfa = df[df["track_artist"] == artist]
            genre = dfa["subgenre"].mode().item()
            year = int(np.round(dfa["year"].mean(), decimals=0))
            pop = dfa["popularity"].mean()
            dance = dfa["danceability"].mean()
            energy = dfa["energy"].mean()
            loud = dfa["loudness"].mean()
            tempo = dfa["tempo"].mean()
            dfo = df[(df["track_artist"] != artist) & (df["subgenre"] == genre) &
                    ((df["year"] <= (year + 5)) | (df["year"] >= (year - 5))) &
                    ((df["danceability"] <= (dance + 3)) & (df["danceability"] >= (dance - 3))) &
                    ((df["energy"] <= (energy + 10)) & (df["energy"] >= (energy - 10))) &
                    ((df["loudness"] <= (loud + 2)) & (df["loudness"] >= (loud - 2))) &
                    ((df["tempo"] <= (tempo + 10)) & (df["tempo"] >= (loud - 10))) &
                    ((df["popularity"] <= (pop + 20)) | (df["popularity"] >= (pop - 10)))]
            opponents = dfo["track_artist"].unique()
            opponent = random.choice(opponents)
            return artist, opponent
        artist, opponent = genres(main_genre)
        return jsonify(artist=artist, opponent=opponent)


if __name__ == "__main__":
    app.run(debug=True)
