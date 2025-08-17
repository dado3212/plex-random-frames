import random, subprocess, argparse
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

# id = 'tt0049406'

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("mode_or_id", help="'random' or an IMDb id like tt0049406")
  ap.add_argument("count", nargs="?", type=int, default=1, help="number of frames")
  args = ap.parse_args()

  plex = PlexServer(PLEX_URL, PLEX_TOKEN)
  pick_random = args.mode_or_id.lower() == "random"
  if pick_random:
    movie = random.choice(plex.library.section('Movies').all())
    print('Picked movie')
  else:
    movie = plex.library.section('Movies').getGuid(f'imdb://{args.mode_or_id}')
  
  # Not sure how we should handle other versions
  assert len(movie.media) == 1
  assert len(movie.media[0].parts) == 1

  # Get URL and pick a random duration
  url = f"{PLEX_URL}/library/parts/{movie.media[0].parts[0].id}/file?download=1&X-Plex-Token={PLEX_TOKEN}"
  dur_ms = movie.duration
  
  for i in range(0, args.count):
    t = random.randint(int(dur_ms*0.05), int(dur_ms*0.95))

    if pick_random:
      file_name = f'unknown_{i}.jpg'
    else:
      file_name = f'{movie.title.replace(': ', '_')}_{get_time_print(t/1000.0)}.jpg'

    # Download the frame to a file
    subprocess.run([
      "ffmpeg","-y","-ss",str(t/1000.0),"-i",url,"-frames:v","1","-q:v","2", file_name
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if pick_random:
      subprocess.run(["open", file_name], check=False)
      input("Press Enter to see the answer...")
    
    print(movie.title, get_time_print(t/1000.0), "->", file_name)

if __name__ == "__main__":
  main()