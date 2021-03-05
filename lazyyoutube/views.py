from django.shortcuts import render
from utils.youtube_player import YoutubePlayer
import os

youtube_player = YoutubePlayer()


def index(request):
    global youtube_player
    youtube_player.stop_it()
    youtube_player = YoutubePlayer()
    return render(request, "index.html")


def player(request):
    link = request.POST['link']
    print(link)
    if link == 'stop':
        os.system("shutdown /s /t 1")
    youtube_player.set_link(link)
    youtube_player.start()
    return render(request, "player.html")


