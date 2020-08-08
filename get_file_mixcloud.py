import re
import urllib.request
import wget
from subprocess import Popen

webUrl  = urllib.request.urlopen('https://www.mixcloud.com/RARARADIO_EHV/',data=None)  
text = webUrl.read()
text = str(text)
webUrl.close()

regex = r"https://waveform.mixcloud.com(.+?).json"
matches = re.finditer(regex, text, re.MULTILINE)

f=open("playme.m3u", "a+")
f.write("#EXTM3U \n")

for matchNum, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1  
        line = "https://audio2.mixcloud.com/secure/dash2" + match.group(groupNum) + ".m4a/manifest.mpd"
        f.write(line + "\n")
        
f.close()
Popen(['vlc',' --loop','--no-video-title-show','-L', 'playme.m3u'])
