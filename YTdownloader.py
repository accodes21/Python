from pytube import YouTube
link = input("Enter youtube url:")
yt = YouTube(link)

SAVE_PATH = "E:/"

#Title of Video
print("Title:",yt.title)

#Number of Views
print("Views:",yt.views)

#Length of Video
print("Length of Video:",yt.length,"seconds")

#Rating of Video
print("Rating:",yt.rating)

print(yt.streams.filter(progressive=True))

ys = yt.streams.get_by_itag('18')

#Downloading
print("***DOWNLOADING***")
ys.download(SAVE_PATH)
print("***DOWNLOADED***")