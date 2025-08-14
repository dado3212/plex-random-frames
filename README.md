# Plex Random Frames

This is two projects in one: a Python script to automatically download random frames from your Plex movies based on the IMDb ID, and a local web app that mirrors https://framed.wtf/ to have you guess a movie from your Plex library based on up to 6 random frames.

Sample images of the web app:
<img width="1259" height="981" alt="Screenshot 2025-08-13 at 8 42 00 PM" src="https://github.com/user-attachments/assets/2ab0b96c-e122-4fb7-80bc-aa44643b4e0a" />

<img width="1259" height="981" alt="Screenshot 2025-08-13 at 8 42 24 PM" src="https://github.com/user-attachments/assets/ac81fef7-e15e-44ec-92f6-ca1b12d73eec" />


## Installation

### Python Script
For the Python script run these commands
```
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```
Create `secret.py` and fill it with
```
PLEX_URL = 'http://<ip>:<port>'
PLEX_TOKEN = '<token>'
```

You can get the token by following https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/.

### Web App
Create `config.local.js` and fill it with
```
window.BASE = 'http://<ip>:<port>';
window.TOKEN = '<token>';
```

## Running

### Python Script
Load the environment with `source venv/bin/activate`. 

Then there are two options:
* `python main.py random` which selects a random frame from a random movie and shows it to you.
* `python main.py tt0049406 5` which takes in an IMDB ID and the # of frames you want, and downloads them into the current directory.

### Web App
Just drag and drop the `index.html` file into your browser and you're good to go!
