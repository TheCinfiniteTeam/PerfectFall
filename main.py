#-*-coding:UTF-8 -*-
import moviepy.editor
import os, time, random, pygame, json
from pygame.locals import *
from resource import Resource

pygame.init()
pygame.mixer.init()

class Game():
    STATES = ['NO_ENTER', 'ENTER', 'PLAY', 'END']
    STATE = STATES[0]
    width = 1280
    height = 720
    runDir = os.getcwd()
    def showVideo(video):
        video.preview()
        video.close()

resource = Resource(Game.runDir)

startVideo = moviepy.editor.VideoFileClip(resource.getPath('video', 'start_720p'))
startVideo.size = [1280, 720]

icon = pygame.image.load(resource.getPath('image', 'icon'))

os.environ['SDL_VIDEO_WINDOW_POS'] = '{x},{y}'.format(x=80, y=50)
window = pygame.display.set_mode((Game.width, Game.height))
pygame.display.set_caption('Perfect Fall')
pygame.display.set_icon(icon)
window.fill((255, 255, 255))

def renderText(fontName, textSize, textColor, text, position):
    TextFont = pygame.font.Font('%s/resource/fonts/%s'%(Game.runDir, fontName), textSize)
    newText = TextFont.render(text, True, textColor)
    window.blit(newText, position)

def handlerEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if Game.STATE == Game.STATES[0]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('start')
                    Game.STATE = Game.STATES[1]

def start():
    Game.showVideo(startVideo)
    pygame.mixer.music.load(resource.getPath('music', 'start'))

gameClock = pygame.time.Clock()

start()

while True:
    if Game.STATE == Game.STATES[0]:
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
    if Game.STATE == Game.STATES[1]:
        pygame.mixer.music.stop()
    gameClock.tick(60)
    #with open(file="fpsData.txt", encoding="utf-8", mode="a+") as fpsData:
    #    fpsData.write("%d -|- %d/60fps -|- %d\n"%(time.time(), gameClock.get_fps(), gameClock.get_time()))
    pygame.display.update()
    handlerEvent()