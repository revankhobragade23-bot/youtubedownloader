from yt_dlp import YoutubeDL 

url = input("Enter the url you want to download:")

options = {
    "format": "bestvideo+bestaudio/best",

}

with YoutubeDL(options) as ydl:
    ydl.download([url])