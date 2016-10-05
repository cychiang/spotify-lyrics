import subprocess
import musixmatch
import getKey
def getCurrentTrack():
    currentTrack = subprocess.Popen(['osascript', 'getCurrentTrack.scpt'], 
    stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return currentTrack.communicate()[0].decode('utf-8').strip().split('-')
    

def getLyrics():
    return lyrics

currentTrack = getCurrentTrack()
currentInfo = {
    "artist": currentTrack[0],
    "track": currentTrack[1]
}

print(currentInfo)
musixmatch_key = getKey.musixmatch()[:-1]

# try:
#     musixmatch
#     chart = musixmatch.ws.track.chart.get(country='it', apikey=apikey)
# except musixmatch.api.Error, e:
#     pass
