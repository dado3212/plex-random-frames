import random, subprocess
from plexapi.server import PlexServer
from secret import PLEX_URL, PLEX_TOKEN

def get_time_print(seconds):
  h = int(seconds // 3600)
  m = int((seconds % 3600) // 60)
  s = seconds % 60
  s = seconds % 60
  if h == 0:
    return f"{m:02d}m_{s:06.3f}s"
  return f"{h}h_{m:02d}m_{s:06.3f}s"

id = 'tt0049406'

# Fetch the movie
plex = PlexServer(PLEX_URL, PLEX_TOKEN)
# Or a random movie
# movie = random.choice(plex.library.section('Movies').all())
movie = plex.library.section('Movies').getGuid(f'imdb://{id}')
assert len(movie.media) == 1
assert len(movie.media[0].parts) == 1

# Get URL and pick a random duration
url = f"{PLEX_URL}/library/parts/{movie.media[0].parts[0].id}/file?download=1&X-Plex-Token={PLEX_TOKEN}"
dur_ms = movie.duration
t = random.randint(int(dur_ms*0.05), int(dur_ms*0.95))

t = 4645135

FILE = f'{movie.title}_{get_time_print(t/1000.0)}.jpg'

# Download the frame to a file
subprocess.run([
  "ffmpeg","-y","-ss",str(t/1000.0),"-i",url,"-frames:v","1","-q:v","2",FILE
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(movie.title, get_time_print(t/1000.0), "->", FILE)