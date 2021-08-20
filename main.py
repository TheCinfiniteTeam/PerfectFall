# -*-coding:UTF-8 -*-
import os, time, pygame, requests, sys, easygui, locale, sqlite3
from pygame.locals import *
from Util import *

pygame.init()
pygame.mixer.init()

#定义常用语法
NULL = None
null = None

none = None
NONE = None

true = True
TRUE = True

false = False
FALSE = False

zero = 0
Zero = 0
ZERO = 0
#


logger = Logger()
logger.info('LANG -> %s'%locale.getdefaultlocale()[0])
#Handler Argv
logger.info('Argv is %s'%sys.argv[1:])
if '--debug' in sys.argv or '-d' in sys.argv:
    logger.DebugMode()
####

playerUUID = getUUID('admin')
logger.info('GET UUID > %s' % playerUUID)

saveData = sqlite3.connect('save.db')
logger.info('Connect to archive database > %s'%saveData)
saveCursor = saveData.cursor()
logger.info('Create save database cursor > %s'%saveCursor)

try:
    URL = 'http://perfectfall.cinfinitestudio.xyz'
    rp = requests.get(URL)
    logger.info('Online Mode > %s' % rp.text)
    title = 'Perfect Fall [Online]'
except Exception as exc:
    logger.warn('Offline Mode > %s' % exc)
    title = 'Perfect Fall [Offline]'


class Game():
    STATES = ['NO_ENTER', 'ENTERING', 'MENU', 'PLAY', 'IEND', 'END']
    GAMESTATES = ['LEAVE', 'IN', 'END']
    STATE = STATES[0]
    MENUSTATES = ['NONE', 'SOLO_SELECT', 'MULTI_SELECT', 'CONFIG']
    MENUSTATE = MENUSTATES[0]
    width = 1280
    height = 720
    size = width, height
    runDir = os.getcwd()


resource = Resource(Game.runDir, logger)
conf = Config(Game.runDir).getConfig()
lang = Lang(Game.runDir)
if locale.getdefaultlocale()[0] == 'zh_CN':
    font = resource.getPath('font', 'ZKWYT')
else:
    font = resource.getPath('font', 'Torus')
os.environ['SDL_VIDEO_WINDOW_POS'] = '{x},{y}'.format(x=80, y=50)
window = pygame.display.set_mode((Game.width, Game.height), vsync=conf['display']['vsync'])
pygame.display.set_icon(resource.getSurface('image', 'icon'))
pygame.display.set_caption(title)

class Surfaces():
    testImg = resource.getSurface('image', 'test')
    filterImg = resource.getSurface('image', 'filter')
    startImg = resource.getSurface('image', 'start')
    menuBGImg = resource.getSurface('image', 'menuBG')

    buttonImg = resource.getSurface('image', 'button')
    buttonDownImg = resource.getSurface('image', 'button_down')
    redButtonImg = resource.getSurface('image', 'redBtn')
    greenButtonImg = resource.getSurface('image', 'greenBtn')

    logoImg = resource.getSurface('image', 'logo')

    eBackgroundImg = resource.getSurface('image', 'eBackground')

    musicCoverList = [

    ]

def renderText(fontPath, textSize, textColor, text, alpha=255):# position,
    global window
    TextFont = pygame.font.Font(fontPath, textSize)
    newText = TextFont.render(text, True, textColor)
    newText.set_alpha(alpha)
    #window.blit(newText, position)
    return newText

class ModLoader():pass
class Mod():
    def __init__(self):
        self.MOD_NAME = None
        self.MOD_ID = None
        self.MOD_OTHER_INFO = None

def handlerEvent():
    global aesci
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            logger.info('Player Keybord KEYDOWN > %d'%event.key)
            if event.key == pygame.K_ESCAPE:
                if Game.MENUSTATE == Game.MENUSTATES[0]:
                    if not aesci:
                        aesci = True
                        Game.STATE = Game.STATES[4]
                        #logger.info('Player Will Exit')
                    elif aesci:
                        aesci = False
                        #logger.info('Player No Will Exit')
                        Game.STATE = Game.STATES[2]
        if event.type == pygame.QUIT:
            if os.path.isdir('%s/logs' % Game.runDir):
                with open(file='logs/%d.log' % time.time(), mode='a+', encoding='utf-8') as log:
                    for logLine in logger.logs:
                        log.write(logLine + '\n')
            else:
                os.mkdir('%s/logs' % Game.runDir)
                with open(file='logs/%d.log' % time.time(), mode='a+', encoding='utf-8') as log:
                    for logLine in logger.logs:
                        log.write(logLine + '\n')
            Game.STATE = Game.STATES[5]
            saveCursor.close()
            saveData.close()
            pygame.quit()
            sys.exit()
        if Game.STATE == Game.STATES[0]:
            if event.type == pygame.KEYDOWN:
                #logger.info('Player DOWNKEY %d' % event.key)
                ame.STATE = Game.STATES[1]
        if Game.STATE == Game.STATES[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Game.MENUSTATE == Game.MENUSTATES[0]:
                        if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 248 and mousePos[1] <= 312:
                            Game.MENUSTATE = Game.MENUSTATES[1]
                        if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 328 and mousePos[1] <= 392:
                            Game.MENUSTATE = Game.MENUSTATES[2]
                        if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 408 and mousePos[1] <= 472:
                            Game.MENUSTATE = Game.MENUSTATES[3]


gameClock = pygame.time.Clock()


startImgAlpha = 255

logoAlpha = 0
while logoAlpha <= 255:
    Surfaces.logoImg.set_alpha(logoAlpha)
    window.blit(pygame.transform.scale(Surfaces.logoImg, Game.size),(0, 0))
    logoAlpha+=5
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            saveCursor.close()
            saveData.close()
            pygame.quit()
            sys.exit()
    gameClock.tick(60)
    pygame.display.update()

aesci = False

while not Game.STATE == Game.STATES[5]:
    mousePos = pygame.mouse.get_pos()
    if Game.STATE == Game.STATES[0]:
        window.blit(pygame.transform.scale(Surfaces.startImg, Game.size), (0, 0))
        pakfSurface = renderText(font, 40, (135, 206, 250), str(lang.key('menu.text.press_any_key')))
        window.blit(pakfSurface, (Game.size[0] / 2 - pakfSurface.get_size()[0] / 2, 590))

    if Game.STATE == Game.STATES[1]:
        if startImgAlpha >= 0:
            startImgAlpha -= 17
            Surfaces.startImg.set_alpha(startImgAlpha)
            window.blit(pygame.transform.scale(Surfaces.startImg, Game.size), (0, 0))
            pakfSurface = renderText(font, 40, (135, 206, 250), str(lang.key('menu.text.press_any_key')), startImgAlpha)
            window.blit(pakfSurface, (Game.size[0] / 2 - pakfSurface.get_size()[0] / 2, 590))

        if startImgAlpha <= 0:
            pygame.mixer.music.stop()
            Surfaces.startImg.set_alpha(255)
            Surfaces.buttonImg.set_alpha(255)
            Game.STATE = Game.STATES[2]

    if Game.STATE == Game.STATES[2]:
        if Game.MENUSTATE == Game.MENUSTATES[0]:
            window.blit(pygame.transform.scale(Surfaces.menuBGImg, Game.size), (0, 0))
            window.blit(Surfaces.filterImg, (0, 0))

            window.blit(Surfaces.buttonImg, (500, 248))
            soloSurface = renderText(font, 40, (135, 206, 250), str(lang.key('menu.text.solo')))
            window.blit(soloSurface, (Game.size[0] / 2 - soloSurface.get_size()[0] / 2, 258))

            window.blit(Surfaces.buttonImg, (500, 328))
            multiSurface = renderText(font, 40, (135, 206, 250), str(lang.key('menu.text.multi')))
            window.blit(multiSurface, (Game.size[0] / 2 - multiSurface.get_size()[0] / 2, 338))

            window.blit(Surfaces.buttonImg, (500, 408))
            configureSurface = renderText(font, 40, (135, 206, 250), str(lang.key('menu.text.configure')))
            window.blit(configureSurface, (Game.size[0]/2-configureSurface.get_size()[0]/2, 418))

            if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 248 and mousePos[1] <= 312:
                window.blit(Surfaces.buttonDownImg, (500, 248))
                soloSurface = renderText(font, 40, (175, 239, 255), str(lang.key('menu.text.solo')))
                window.blit(soloSurface, (Game.size[0] / 2 - soloSurface.get_size()[0] / 2, 258))

            if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 328 and mousePos[1] <= 392:
                window.blit(Surfaces.buttonDownImg, (500, 328))
                multiSurface = renderText(font, 40, (175, 239, 255), str(lang.key('menu.text.multi')))
                window.blit(multiSurface, (Game.size[0] / 2 - multiSurface.get_size()[0] / 2, 338))

            if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 408 and mousePos[1] <= 472:
                window.blit(Surfaces.buttonDownImg, (500, 408))
                configureSurface = renderText(font, 40, (175, 239, 255), str(lang.key('menu.text.configure')))
                window.blit(configureSurface, (Game.size[0] / 2 - configureSurface.get_size()[0] / 2, 418))
    if Game.STATE == Game.STATES[4]:
        window.blit(Surfaces.eBackgroundImg, (Game.size[0] / 2 - Surfaces.eBackgroundImg.get_size()[0] / 2, 0))

        window.blit(Surfaces.redButtonImg, (Game.size[0] / 2 - Surfaces.eBackgroundImg.get_size()[0] / 2 + Surfaces.redButtonImg.get_size()[0] / 2 - Surfaces.redButtonImg.get_size()[0] / 2 / 2 / 2 / 2, 35))

        window.blit(Surfaces.greenButtonImg, (Game.size[0] / 2 - Surfaces.eBackgroundImg.get_size()[0] / 2 + Surfaces.greenButtonImg.get_size()[0] / 2 - Surfaces.greenButtonImg.get_size()[0] / 2 / 2 / 2 / 2, 134))

    handlerEvent()
    """
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if Game.MENUSTATE == Game.MENUSTATES[0]:
                    if not aesci:
                        aesci = True
                        Game.STATE = Game.STATES[4]
                        logger.info('Player Will Exit')
                    elif aesci:
                        aesci = False
                        logger.info('Player No Will Exit')
                        Game.STATE = Game.STATES[2]
        if event.type == pygame.QUIT:
            if os.path.isdir('%s/logs' % Game.runDir):
                with open(file='logs/%d.log' % time.time(), mode='a+', encoding='utf-8') as log:
                    for logLine in logger.logs:
                        log.write(logLine + '\n')
            else:
                os.mkdir('%s/logs' % Game.runDir)
                with open(file='logs/%d.log' % time.time(), mode='a+', encoding='utf-8') as log:
                    for logLine in logger.logs:
                        log.write(logLine + '\n')
            Game.STATE = Game.STATES[5]
            saveCursor.close()
            saveData.close()
            pygame.quit()
            sys.exit()
        if Game.STATE == Game.STATES[0]:
            if event.type == pygame.KEYDOWN:
                logger.info('Player DOWNKEY %d' % event.key)
                Game.STATE = Game.STATES[1]
        if Game.STATE == Game.STATES[2]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Game.MENUSTATE == Game.MENUSTATES[0]:
                        if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 248 and mousePos[1] <= 312:
                            Game.MENUSTATE = Game.MENUSTATES[1]
                        if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 328 and mousePos[1] <= 392:
                            Game.MENUSTATE = Game.MENUSTATES[2]
                        if mousePos[0] >= 500 and mousePos[0] <= 780 and mousePos[1] >= 408 and mousePos[1] <= 472:
                            Game.MENUSTATE = Game.MENUSTATES[3]
    """


    if conf['display']['fps'] == None:
        gameClock.tick(sys.maxsize)
    else:
        gameClock.tick(conf['display']['fps'])
    pygame.display.update()
