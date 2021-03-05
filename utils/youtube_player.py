import vlc
import pafy
import time
import threading


class YoutubePlayer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(YoutubePlayer, self).__init__(*args, **kwargs)
        self._stopper = threading.Event()
        self.link = ''
        self.first_play = True
        self.ins = vlc.Instance(['--video-on-top'])
        self.player = self.ins.media_player_new()
        self.player.toggle_fullscreen()
        self.stop_it()

    def youtube_play(self):
        url = self.link
        video = pafy.new(url)
        best = video.getbest()
        play_url = best.url
        media = self.ins.media_new(play_url)
        media.get_mrl()
        self.player.set_media(media)
        self.player.play()
        good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
        while str(self.player.get_state()) in good_states:
            if self.stopped():
                return
            time.sleep(1)
        self.player.stop()

    def set_link(self, address):
        self.link = address

    def set_first_play(self):
        self.first_play = False

    def get_first_play(self):
        return self.first_play

    def stop_it(self):
        self.player.stop()
        self._stopper.set()

    def run(self):
        self.youtube_play()

    def stopped(self):
        return self._stopper.is_set()
