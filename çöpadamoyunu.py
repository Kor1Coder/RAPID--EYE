import sys
import pygame
pygame.font.init()
FPS = 60
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('ADAM ASMACA')
MAIN_FONT=pygame.font.SysFont("comicsans", 24)
# basic font for user typed
base_font = pygame.font.Font(None, 22)
base_font2=pygame.font.Font(None, 152)


def textblit(win,font,text):
    render=font.render(text, 1, (0, 255,0 ))
    win.blit(render, (400,700))
def textblit2(win,font,text,ceri):
    render=font.render(text, 1, (125, 100,125 ))
    win.blit(render, ceri )

def drawline(start, end):
    pygame.draw.line(WIN, (255, 255, 255), start, end, 2)


def drawcircle(center, radius):
    pygame.draw.circle(WIN, (255, 255, 255), center, radius)



input_rect = pygame.Rect(100, 100, 50, 50)
sina=True

class takeinput:
    def __init__(self):
        self.description = input('SORMAK İSTEDİĞİNİZİN KELİMENİN AÇIKLAMASI:')
        self.inp = input('SORULAN KELİME:')
        self.k=0
    def showtext(self,win,letter,designbox):
        sina=True
        for i in self.inp:
            if i==letter:
                k=[]
                for rang in range(len(self.inp)):
                    if self.inp[rang] ==i:
                        k.append(rang)

                for say in k:

                    say=int(say)
                    ind=self.inp.index(i)

                    textblit2(win,base_font2,i,designbox.depo[ say])#

        if letter not in self.inp:
            print(letter)
            if self.k == 8:
                drawline((500, 350), (450, 390))
                self.k += 1
            if self.k == 7:
                drawline((500, 350), (550, 390))
                self.k += 1
            if self.k == 6:
                drawline((500, 210), (450, 250))
                self.k += 1
            if self.k == 5:
                drawline((500, 210), (550, 250))
                self.k += 1
            if self.k == 4:
                drawline((500, 210), (500, 350))
                self.k += 1
            if self.k == 3:
                    drawcircle((500, 180), 30)
                    self.k += 1
            if self.k == 2:
                drawline((500, 100), (500, 150))
                self.k += 1
            if self.k==1.5:
                drawline((300, 100), (500, 100))
                self.k += 0.5
            if self.k == 1:
                drawline((300, 500), (300, 100))
                self.k += 0.5
            if self.k == 0:
                drawline((200, 500), (400, 500))
                self.k += 1


class designbox():
    def __init__(self, question):

        self.yaxix=550
        self.letter=0
        self.question = question

    def writedescription(self,win):
        textblit(win,MAIN_FONT,'TIP='+self.question.description)
    def drawbox(self,win):
        if ' ' not in self.question.inp:
            length=len(self.question.inp)
            x=10
            self.depo=[]
            self.depo2=[]
            for box in range(length):
                Rec=pygame.Rect(x,self.yaxix,40,40)
                pygame.draw.rect(win,(100,200,200),Rec)
                self.depo.append((x,self.yaxix))
                self.depo2.append(Rec)
                x+=50

question=takeinput()
designer=designbox(question)


active=False
while True:

    user_text = ''
    clock.tick(FPS)
    designer.writedescription(WIN)
    designer.drawbox(WIN)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos) and len(user_text)<=1:

                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                question.__init__()
                designer.__init__(question)
                WIN.fill((0,0,0))
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]


            if event.type == pygame.K_KP_ENTER:

                print(2)


            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
    if active  and len(user_text)<=1:
        color = pygame.Color('lightskyblue3')
    else:
        color = pygame.Color('chartreuse4')
    pygame.draw.rect(WIN, color, input_rect)

    if len(user_text)==1 and user_text!='\n':

        text_surface = base_font.render(user_text, True, (255, 255, 255))

        question.showtext(WIN,user_text,designer)
        user_text=''
        # render at position stated in arguments
        WIN.blit(text_surface, (input_rect.x+input_rect.width/2-5, input_rect.y+input_rect.height/2-10))
    sumbit=False
    pygame.display.update()