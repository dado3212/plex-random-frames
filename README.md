# Plex Random Frames
Script for pulling a random frame from a movie off of Plex.

https://framed.wtf/

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