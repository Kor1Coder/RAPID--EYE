import time

import pygame,sys
pygame.init()
import random
pygame.font.init()
MAIN_FONT=pygame.font.SysFont("comicsans", 24)

def textblit(win,font,text):
    render=font.render(text, 1, (0, 255,0 ))
    win.blit(render, (win.get_width()/2-render.get_width()/2,win.get_height()/2-render.get_height()/2))
class boxes:
    def __init__(self):
        self.x=2
        self.y=2
        self.totalofbox = []
        self.arrangementlight=False
        self.depo=[]
        self.canwedraw=False
    def draw(self,win):

        total=self.x*self.y
        if not self.totalofbox:
            self.canwedraw = True
            for x in  range(self.x) :
                for y in range(self.y):
                    boxrect=pygame.Rect(x*(WIN.get_width()/self.x)+10,y*(WIN.get_height()/self.y)+10,(HEIGHT-60)/self.y,(WIDTH-60)/self.x)
                    self.totalofbox.append(boxrect)
                    pygame.draw.rect(win,(103,103,103),boxrect)
    def randomlight(self,win):
        self.canwedraw = False
        random.shuffle(self.totalofbox)
        self.randomkutu=self.totalofbox
        for box in  self.totalofbox:
            pygame.draw.rect(win,(255,255,255),box)
            pygame.display.update()
            pygame.draw.rect(win, (0, 0, 0), box)
            pygame.time.wait(400)
        self.againdraw(win)
        self.canwedraw=True

    def againdraw(self,win):
        self.canwedraw=False
        pygame.time.wait(500)
        for x in range(self.x):
            for y in range(self.y):
                boxrect = pygame.Rect(x * (WIN.get_width() / self.x) + 10, y * (WIN.get_height() / self.y) + 10, (HEIGHT - 60) / self.y, (WIDTH - 60) / self.x)
                pygame.draw.rect(win, (103, 103, 103), boxrect)
    def lightcertainbox(self,win,mousex,mousey):


        depo=[]

        for location in self.totalofbox:
            if location[0]<mousex<location[0]+location[2]  and location[1]<mousey<location[1]+location[3]:
                pygame.draw.rect(win,(255,255,255),location)
                self.depo.append(location)
        try:

            if self.depo==self.randomkutu:
                textblit(win,MAIN_FONT,'DOĞRU YAPTIN')
                pygame.display.update()
                pygame.time.wait(500)
                win.fill(pygame.Color("black"))
                self.nextlevel(WIN)

            elif len(self.depo)==len(self.totalofbox) and self.depo!=self.totalofbox :


                textblit(win,MAIN_FONT,'Yanlış yaptın')
                pygame.display.update()
                pygame.time.wait(500)
                win.fill(pygame.Color("black"))
                self.reset(win)
        except AttributeError:
            self.reset(win)
            textblit(win, MAIN_FONT, 'Öncelikle İzle(izlemek için a ya ba)')
            pygame.display.update()
            pygame.time.wait(500)
            win.fill(pygame.Color("black"))
        finally:self.canwedraw=True
    def nextlevel(self,win):
        self.x+=1
        self.y+=1
        self.depo = []
        self.canwedraw=False
        self.randomkutu=0
        self.totalofbox = []
        self.arrangementlight = False
        win.fill(pygame.Color("black"))


    def reset(self,win):
        self.x=2
        self.y=2
        self.depo=[]
        self.totalofbox = []
        self.arrangementlight = False
        win.fill(pygame.Color("black"))




def mousequestion(mousex,mousey ,boxes):
    for box in boxes.totalofbox:
        if  box[0]< mousex <box[0]+box[2] and box[1]< mousey <box[1]+box[3]:
            return (mousex,mousey)


fpstime=pygame.time.Clock()
FPS=60
HEIGHT=860
WIDTH=640
WIN=pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('simulate')
box=boxes()

while True:

    fpstime.tick(FPS)
    box.draw(WIN)
    keys=pygame.key.get_pressed()

    if keys[pygame.K_a] :
         box.randomlight(WIN)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            mousex,mousey=pygame.mouse.get_pos()
        else:mousex,mousey=(0,0)

        if event.type == pygame.MOUSEBUTTONUP and box.canwedraw:
            mousex, mousey = pygame.mouse.get_pos()
            Clicked=True
            box.lightcertainbox(WIN,mousex,mousey)



    pygame.display.update()