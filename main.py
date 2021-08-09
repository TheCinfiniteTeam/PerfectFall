from moviepy.editor import *
import os, time, random, pygame

#init
class Game():
    width = 600
    height = 720
    isExit = False
    runDir = os.getcwd()
    def showVideo(video):
        video.preview()
        video.close()

class Resource():
    startVideo = VideoFileClip('%s/resource/start720p.mp4' % Game.runDir)
    startVideo.size = [1280, 720]





os.environ['SDL_VIDEO_WINDOW_POS'] = '{x},{y}'.format(x=0,y=0)

pygame.display.set_caption("Perfect Fall")
Game.showVideo(Resource.startVideo)
canvas = pygame.display.set_mode((Game.width, Game.height))
while Game.isExit == False:
    pygame.display.update()