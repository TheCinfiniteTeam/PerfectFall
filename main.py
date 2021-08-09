from moviepy.editor import VideoFileClip
import os, time, random, pygame

class Game():
    width = 1280
    height = 720
    isExit = False
    runDir = os.getcwd()
    def showVideo(video):
        video.preview()
        video.close()

class Resource():
    startVideo = VideoFileClip('%s/resource/start720p.mp4' % Game.runDir)
    startVideo.size = [1280, 720]

    icon = pygame.image.load("%s/resource/icon.png"%Game.runDir)

class Window():
    def __init__(self):
        pass
    def init(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '{x},{y}'.format(x=80, y=50)
        pygame.display.set_caption("Perfect Fall")
        pygame.display.set_icon(Resource.icon)
        Game.showVideo(Resource.startVideo)
        self.window = pygame.display.set_mode((Game.width, Game.height))

    def loop(self):
        while Game.isExit == False:
            self.handlerEvent()
            pygame.display.update()

    def handlerEvent(self):
        for event in pygame.event.get():
            pass



if __name__ == '__main__':
    window = Window()
    window.init()
    window.loop()