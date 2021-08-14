# -*-coding:UTF-8 -*-
from moviepy.editor import VideoFileClip
import os, time, random, pygame, json, requests, sys
from pygame.locals import *
from Util import *

pygame.init()
pygame.mixer.init()

logger = Logger()

playerUUID = getUUID('admin')
logger.info('GET UUID > %s' % playerUUID)

try:
    URL = 'http://perfectfall.cinfinitestudio.xyz'
    rp = requests.get(URL)
    logger.info('Online Mode > %s' % rp.text)
    title = 'Perfect Fall [Online]'
except Exception as exc:
    logger.warn('Offline Mode > %s' % exc)
    title = 'Perfect Fall [Offline]'


class Game():
    STATES = ['NO_ENTER', 'ENTERING', 'MENU', 'PLAY', 'END']
    GAMESTATES = ['LEAVE', 'IN', 'END']
    STATE = STATES[0]
    width = 1280
    height = 720
    size = width, height
    runDir = os.getcwd()

    def showVideo(video):
        video.preview()
        video.close()


resource = Resource(Game.runDir)
conf = Config(Game.runDir).getConfig()

startVideo = VideoFileClip(resource.getPath('video', 'start_720p'))
startVideo.size = [1280, 720]

os.environ['SDL_VIDEO_WINDOW_POS'] = '{x},{y}'.format(x=80, y=50)
window = pygame.display.set_mode((Game.width, Game.height), vsync=conf['display']['vsync'])
pygame.display.set_icon(resource.getSurface('image', 'icon'))
pygame.display.set_caption(title)


class Images():
    testImg = resource.getSurface('image', 'test')
    filterImg = resource.getSurface('image', 'filter')
    startImg = resource.getSurface('image', 'start')
    menuBGImg = resource.getSurface('image', 'menuBG')

    buttonImg = resource.getSurface('image', 'button')
    buttonDownImg = resource.getSurface('image', 'button_down')

    musicCoverList = [

    ]



def renderText(fontPath, textSize, textColor, text, position, alpha=255):
    global window
    TextFont = pygame.font.Font(fontPath, textSize)
    newText = TextFont.render(text, True, textColor)
    newText.set_alpha(alpha)
    window.blit(newText, position)

class ModLoader():pass
class Mod():pass

gameClock = pygame.time.Clock()

Game.showVideo(startVideo)

startImgAlpha = 255

while not Game.STATE == Game.STATES[4]:
    mousePos = pygame.mouse.get_pos()
    if Game.STATE == Game.STATES[0]:
        window.blit(pygame.transform.scale(Images.startImg, Game.size), (0, 0))
        renderText(resource.getPath('font', 'ZKWYT'), 40, (135, 206, 250), '按下任意键开始游戏', (465, 590))

    if Game.STATE == Game.STATES[1]:
        if startImgAlpha >= 0:
            startImgAlpha -= 17
            Images.startImg.set_alpha(startImgAlpha)
            window.blit(pygame.transform.scale(Images.startImg, Game.size), (0, 0))
            renderText(resource.getPath('font', 'ZKWYT'), 40, (135, 206, 250), '按下任意键开始游戏', (465, 590), startImgAlpha)

        if startImgAlpha <= 0:
            pygame.mixer.music.stop()
            Images.startImg.set_alpha(255)
            Images.buttonImg.set_alpha(255)
            Images.peopleImg.set_alpha(255)
            Game.STATE = Game.STATES[2]

    if Game.STATE == Game.STATES[2]:
        window.blit(pygame.transform.scale(Images.menuBGImg, Game.size), (0, 0))
        window.blit(Images.filterImg, (0, 0))
        window.blit(Images.buttonImg, (500, 248))
        renderText(resource.getPath('font', 'Torus'), 40, (135, 206, 250), 'Solo', (600, 248))
        window.blit(Images.buttonImg, (500, 328))
        renderText(resource.getPath('font', 'Torus'), 40, (135, 206, 250), 'Multi', (600, 328))
        window.blit(Images.buttonImg, (500, 408))
        renderText(resource.getPath('font', 'Torus'), 40, (135, 206, 250), 'Configure', (552, 408))

        if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 248 and mousePos[1] <= 312:
            window.blit(Images.buttonDownImg, (500, 248))
            renderText(resource.getPath('font', 'Torus'), 40, (175, 239, 255), 'Solo', (600, 248))

        if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 328 and mousePos[1] <= 392:
            window.blit(Images.buttonDownImg, (500, 328))
            renderText(resource.getPath('font', 'Torus'), 40, (175, 239, 255), 'Multi', (600, 328))

        if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 408 and mousePos[1] <= 472:
            window.blit(Images.buttonDownImg, (500, 408))
            renderText(resource.getPath('font', 'Torus'), 40, (175, 239, 255), 'Configure', (552, 408))

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.STATE = Game.STATES[4]
            pygame.quit()
            if os.path.isdir('%s/logs' % Game.runDir):
                with open(file='logs/%d.log' % time.time(), mode='a+', encoding='utf-8') as log:
                    for logLine in logger.logs:
                        log.write(logLine + '\n')
            else:
                os.mkdir('%s/logs' % Game.runDir)
                with open(file='logs/%d.log' % time.time(), mode='a+', encoding='utf-8') as log:
                    for logLine in logger.logs:
                        log.write(logLine + '\n')
            sys.exit()
        if Game.STATE == Game.STATES[0]:
            if event.type == pygame.KEYDOWN:
                logger.info('Player DOWNKEY %d' % event.key)
                Game.STATE = Game.STATES[1]

    if conf['display']['fps'] == None:
        gameClock.tick(sys.maxsize)
    else:
        gameClock.tick(conf['display']['fps'])
    pygame.display.update()
