import sys

import pygame
import random
pygame.font.init()

MAIN_FONT=pygame.font.SysFont('comicsans',25)
MAIN_FONT2=pygame.font.SysFont('comicsans',55)
Sumbit_Font= pygame.font.SysFont('comicsans',25)
user_text=''
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive

clock=pygame.time.Clock()
HEIGHT,WIDTH=860,640
WIN=pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('Göz Geliştiricisi')
FPS=60
devamet=pygame.image.load('devamet.jpg')
devamet=pygame.transform.scale(devamet,(WIN.get_width()-200,400))

class Scor:
    def __init__(self):
        self.score=0
        self.stage=1
        self.onemore=False
        self.random_integer1 = random.randint(1, 10)
        self.random_integer2 = random.randint(10, 100)
        self.random_integer3 = random.randint(100, 1000)
        self.random_integer4 = random.randint(1000, 10000)
        self.kes=False
    def stagefon(self):
        if self.score<5:
            textquest=MAIN_FONT.render(str(self.random_integer1) , True, (232, 121, 1))
            WIN.blit(textquest, (random.randint(10,800), random.randint(190,400)))
        if 10>self.score>=5:
            textquest = MAIN_FONT.render(str(self.random_integer2), True, (232, 121, 1))
            WIN.blit(textquest, (random.randint(10,800), random.randint(190,400)))

        if 15>self.score>=10:
            textquest = MAIN_FONT.render(str(self.random_integer3) , True, (232, 121, 1))
            WIN.blit(textquest, (random.randint(10,800), random.randint(190,400)))
        if self.score >= 15:
            textquest = MAIN_FONT.render(str(self.random_integer4), True, (232, 121, 1))
            WIN.blit(textquest, (random.randint(10, 800), random.randint(190, 400)))

        self.onemore=False
    def dogrula(self,text):
        if self.score >=15:
            if str(self.random_integer4) ==text.strip(' '):
                self.score+=1
                self.onemore = False
            elif str(self.random_integer4) != text.strip(' '):
                self.kes = True
        if 15>self.score>=10:
            if str(self.random_integer3) ==text.strip(' '):
                self.score+=1
                self.onemore = False
            elif str(self.random_integer3) != text.strip(' '):
                self.kes = True
        if 10>self.score>=5:
            if str(self.random_integer2) ==text.strip(' '):
                self.score+=1
                self.onemore = False
            elif str(self.random_integer2) !=text.strip(' '):
                self.kes = True
        if self.score < 5:
            if str(self.random_integer1) ==text.strip(' '):
                self.score+=1
                self.onemore = False
            elif str(self.random_integer1) != text.strip(' '):
                self.kes = True









    def scoresayac(self):
        if self.score <= 5:
            textquest = MAIN_FONT2.render(str(self.score)+"-----stage1", True, (1, 1, 1))
            WIN.blit(textquest, (WIN.get_width() / 2 - textquest.get_width() / 2, 0))
        if self.score > 5:
            textquest = MAIN_FONT2.render(str(self.score)+"-----stage2", True, (1, 1, 1))
            WIN.blit(textquest, (WIN.get_width() / 2 - textquest.get_width() / 2, 0))
        if self.score  >=10:
            textquest = MAIN_FONT2.render(str(self.score)+"-----stage3", True, (1, 1, 1))
            WIN.blit(textquest, (WIN.get_width() / 2 - textquest.get_width() / 2, 0))
        if self.score >=15:
            textquest = MAIN_FONT2.render(str(self.score)+"-----stage4", True, (1, 1, 1))
            WIN.blit(textquest, (WIN.get_width() / 2 - textquest.get_width() / 2, 0))
    def fail(self):
        self.score = 0
        self.stage = 1

        self.onemore = False
    def startagain(self):
        WIN.fill((0, 0, 0))
        textquest = MAIN_FONT.render("YANLIŞ YAPTINIZ.", True, (255, 255, 255))
        WIN.blit(textquest, (WIN.get_width() / 2 - textquest.get_width() / 2, 0))
        textquest = MAIN_FONT.render("TEKRAR BAŞLATMAK İÇİN YUKARI TUŞUNA BAS", True, (255, 255, 255))
        WIN.blit(textquest, (WIN.get_width() / 2 - textquest.get_width() / 2, 60))
        WIN.blit(devamet,(100,200,100,600))
        pygame.display.update()



pygamerect=pygame.Rect(WIN.get_width()/2-100,WIN.get_height()/2+125,200,50)
pygamesumbitrect=pygame.Rect(WIN.get_width()/2-80,WIN.get_height()/2+200,200,50)
active=False
etkin=False
play=Scor()

while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygamerect.collidepoint(event.pos):
                active = True
            elif pygamesumbitrect.collidepoint(event.pos):
                 gettext=user_text
                 play.dogrula(gettext)

                 b=False
                 if play.kes==True:
                     b=True
                 a=play.score
                 play.__init__()
                 play.kes=b
                 play.score=a
                 user_text=''
            elif event.button==3:
                play.onemore = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                play.kes=False
                play.__init__()

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]

            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode



            # it will set background color of screen
        WIN.fill((255, 255, 255))

        if active:
            color = color_active
        else:
            color = color_passive
    mousepos = pygame.mouse.get_pos()
    if mousepos:

        xek, yek = mousepos
        if (
        pygamesumbitrect.x) < xek < pygamesumbitrect.x + pygamesumbitrect.w and pygamesumbitrect.y < yek < pygamesumbitrect.y + pygamesumbitrect.h:
            Sumbit_Font = pygame.font.SysFont('comicsans', 30,italic=True,bold=True)
    if play.onemore:
       play.stagefon()
    play.scoresayac()

    if play.kes==True:
        play.startagain()

    else:

        pygame.draw.rect(WIN,(255,0,0),pygamesumbitrect,1)
        textsumbit=Sumbit_Font.render('ONAYLA', True, (232, 121, 1))
        WIN.blit(textsumbit,(pygamesumbitrect.x+45,pygamesumbitrect.y+12))
        pygame.draw.rect(WIN, (1, 100, 1), pygamerect, 2)
        oyun_bilgi = MAIN_FONT.render('''OYUN NASIL OYNANIR? ÖNCELİKLE OYUNU OYNAMAK İÇİN YUKARI YÖNÜ VE VE FARENİN SAĞ TIKINI KULLANMANIZ GERKELİDİR.OYUN 4 AŞAMADAN OLUŞUR VE BU AŞAMALAR STAGE ADI VERİLEN BÖLÜMLERE AYRILMIŞTIR AMAÇ STAGELERİ BİTİRMEK.''', True,(1, 1, 1))
        WIN.blit(oyun_bilgi, (0, 100)    )
        oyun_bilgi = MAIN_FONT.render(''' YÖNÜ VE VE FARENİN SAĞ TIKINI KULLANMANIZ GERKELİDİR.OYUN 4 AŞAMADAN OLUŞUR VE BU AŞAMALAR STAGE ADI VERİLEN BÖLÜMLERE AYRILMIŞTIR AMAÇ STAGELERİ BİTİRMEK.''', True,
                                      (1, 1, 1))
        WIN.blit(oyun_bilgi, (0, 130))
        oyun_bilgi = MAIN_FONT.render(
            ''' 4 AŞAMADAN OLUŞUR OLUŞUR VE BU AŞAMALAR STAGE ADI VERİLEN BÖLÜMLERE AYRILMIŞTIR AMAÇ STAGELERİ BİTİRMEK.''',
            True,
            (1, 1, 1))
        WIN.blit(oyun_bilgi, (0, 160))
        oyun_bilgi = MAIN_FONT.render(
            '''BÖLÜMLERE AYRILMIŞTIR AMAÇ STAGELERİ BİTİRMEK.''',
            True,
            (1, 1, 1))
        WIN.blit(oyun_bilgi, (0, 190))
        text_surface = MAIN_FONT.render(user_text, True, (232, 121, 1))
        WIN.blit(text_surface, (pygamerect.x + 20 , pygamerect.y + 5))
        pygamerect.w=max(240,text_surface.get_width())
        pygame.display.update()
        if etkin != True:
            Sumbit_Font = pygame.font.SysFont('comicsans', 25)
        etkin=False
        play.kes=False


    clock.tick(FPS)