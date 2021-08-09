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
        self.game = Game
        self.resource = Resource

    def init(self):
        pygame.init()
        os.environ['SDL_VIDEO_WINDOW_POS'] = '{x},{y}'.format(x=80, y=50)
        self.window = pygame.display.set_mode((Game.width, Game.height))
        pygame.display.set_caption("Perfect Fall")
        pygame.display.set_icon(self.resource.icon)
        self.game.showVideo(self.resource.startVideo)


    def loop(self):
        while self.game.isExit == False:
            self.handlerEvent()
            pygame.display.update()

    def renderText(self, fontName, textSize, textColor, text, position):
        TextFont = pygame.font.Font('%s/resource/fonts/%s'%(self.game.runDir, fontName), textSize)
        newText = TextFont.render(text, True, textColor)
        self.window.blit(newText, position)

    def handlerEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.isExit = True
                pygame.quit()

if __name__ == '__main__':
    window = Window()
    window.init()
    window.loop()