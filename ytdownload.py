from pytube import YouTube
from sys import argv

# take the fist argument in the command line and put it into link
link = argv[1]
yt = YouTube(link)

print("Title: " ,yt.title)
print("Views: ", yt.views)

# download quality
yd = yt.streams.get_highest_resolution()
# download destination
yd.download('/Users/manojayyappan/Documents/Personal/Yt_downloads')
 