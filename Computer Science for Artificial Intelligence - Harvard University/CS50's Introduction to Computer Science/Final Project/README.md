## Harvard's CS50 Final Project: Music Battles

This was my final project to complete Harvard's CS50 program. It’s a web application where music artists compete with each other on a musical level. It’s meant to be fun and it’s a great way to discover new artists and new music.


#### Demo Video:  
https://www.youtube.com/watch?v=etunUsVZNxM

---

#### Languages used in this project:
- Python
- JavaScript
- HTML
- CSS
  
#### Framework and engine:
- Flask
- Jinja

#### Librairies:
- Pandas
- Numpy

#### Data:
The database used in this project is a mix of multiple Spotify databases available on [Kaggle.com](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset). The cleansing and feature engineering phase was done separately. The dataset contains more than 528,000 unique songs, 22,366 unique artists and 63 different genres.

---

#### Description:
'CS50 Music Battles' is a playful web application of which the design was inspired by the infamous fighting video game series Tekken. As I was taking CS50's Introduction to Artifical Intelligence with Python course at the time, I designed all of the background videos, images and characters using online AI tools.

The very first page (index.html file) has users standing outside of the fighting arena. Once they click 'Enter', they land to the 'mode' page (mode.html file) where they are asked to choose between two gaming modes: the Artist Mode and the Random Mode.

When selecting the Artist Mode (artist.html file), users are prompted to choose an artist of their liking. They can start typing a name thanks to an autocomplete search bar, and then click the name of the artist they want to select. They can either change artists or save their selection. Once the first artist is chosen, a function written in Python will automatically select a similar artist based on the average year, popularity, danceability, energy and tempo (to name a few attributes) of the first artist's repertoire. Once an opponent has been automatically chosen, users have the possibility to change this opponent and have another artist automatically proposed, or save the computer's selection and go on with the fight. To be noted: on this page, users have the possibility to go back to the main menu if they'd like, or even turn off the background music.

When two artists have been selected, a fight can take place (fight.html file). The app will propose a random selection of songs by the two artists competing, and users will have to vote for the tracks they like the most. They can listen to a preview of the songs on the page, as the app uses the Spotify online streaming iframe. Each vote will give the artist one point. The first artist who gets 3 points wins the fight.

When the fight is over, users can view the playlist of the fight and listen to the songs on Spotify.com. They can also start a new fight with new artists, or they can go back to the main menu and select another gaming mode.

The second gaming mode is the Random mode (random.html file). Here users don’t pick an artist, they choose a music genre from all the genres listed in the database. As per previously, they can either change their selection and pick another genre, or save it. Once the genre has been saved, the app will automatically and randomly pick two artists belonging to the chosen genre. Once the selection is saved, the fight can begin and users will be directed to the fights.html page. It is similar to the fight.html page, except this page will take users back to the Random mode at the end of the fight if desired, instead of the Artist mode page.

#### Timeline and ways of improvement:

Designing and coding this web application took me two whole weeks. I had prior experience coding in Python but no experience at all with JavaScript, Flask, HTML or CSS, which was a challenge to say the least. The app is responsive (landscape orientation only), although it was designed to be experienced on a laptop or a computer.

Some of the initial features I wanted to implement include a user account, to save and retrieve playlists of previous fights. I decided to go for this 'MVP' version of the app, and I'm quite proud of it. I hope you'll enjoy it too!
