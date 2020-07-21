import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

channel = input('What is the name of the YouTube channel are we looking at?\nFor example: \"enyay\" or \"UCtqxG9IrHFU_ID1khGvx9sA\".\n')

try:
    url = (str('https://www.youtube.com/user/') + str(channel))
    req = requests.get(url)
    if req.status_code == 404:
        url = (str('https://www.youtube.com/c/') + str(channel))
        req = requests.get(url)
        if req.status_code == 404:
            url = (str('https://www.youtube.com/') + str(channel))
            req = requests.get(url)
    ytsoup = BeautifulSoup(req.text, 'html.parser')
    rssline = ytsoup.find(title="RSS")
    rss = (rssline.get('href'))
except:
    rss = "https://www.youtube.com/feeds/videos.xml?channel_id=" + channel

req = requests.get(rss)
ytsoup = BeautifulSoup(req.text,'html.parser')
videos = []

for item in ytsoup.find_all('entry'):
    videoOG = item.find('id').string
    videoID = videoOG.replace('yt:video:', '')
    videoTitle = item.find('title').string
    videoLink = str("https://www.youtube.com/watch?v=") + str(videoID)
    videoDictionary = {}
    videoDictionary['15 Most Recent Videos uploads by ' + str(channel)] = videoTitle
    videoDictionary['Video URL'] = videoLink
    videos.append(videoDictionary)

print(tabulate(videos, headers="keys"))
if not videos:
    print("No videos found on this channel!")