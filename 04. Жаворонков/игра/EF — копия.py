import time
import random
import pygame
import sys

WIDTH =600
HEIGHT = 800
FPS = 40

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255,215,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED=(255,10,10)
tyh1=0
tyh2=0
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
bg = pygame.image.load("bg.jpg").convert_alpha()
screen.fill(GOLD)
screen.blit(bg,(0,0))
sound1 = 'cool.mp3'
gf=[sound1]
pik=0
tome=3
pygame.mixer.music.load('yaponia.mp3')#музыка,|                     #|
pygame.mixer.music.play()         #___
lk="3.png"
k="2.png"
def right_left(k,lk):
    image1 = pygame.image.load(k).convert_alpha()
    image2= pygame.image.load(lk).convert_alpha()
    screen.fill(GOLD)
    screen.blit(bg,(0,0))
    new_image = pygame.transform.scale(image1, (400, 400))
    new_image2 = pygame.transform.scale(image2, (400, 400))
    screen.blit(new_image2, (10, 145))
    screen.blit(new_image, (180, 145))
    pygame.display.update()
def right_left_stuk(k,lk):
    image1 = pygame.image.load(k).convert_alpha()
    image2= pygame.image.load(lk).convert_alpha()
    screen.fill(GOLD)
    screen.blit(bg,(0,0))
    new_image = pygame.transform.scale(image1, (400, 400))
    new_image2 = pygame.transform.scale(image2, (400, 400))
    screen.blit(new_image2, (10, 120))
    screen.blit(new_image, (180, 120))
    pygame.display.update()
def proigral_right(k,lk):
    image1 = pygame.image.load(k).convert_alpha()
    image2= pygame.image.load(lk).convert_alpha()
    screen.fill(GOLD)
    screen.blit(bg,(0,0))
    new_image = pygame.transform.scale(image1, (400, 400))
    new_image2 = pygame.transform.scale(image2, (400, 400))
    screen.blit(new_image2, (10, 120))
    n=180
    while n!=600:
     n+=1
     screen.blit(new_image, (n, 120))
     pygame.display.update()
     screen.fill(GOLD)
     screen.blit(bg,(0,0))
def proigral_left(k,lk):
    image1 = pygame.image.load(k).convert_alpha()
    image2= pygame.image.load(lk).convert_alpha()
    screen.fill(GOLD)
    screen.blit(bg,(0,0))
    new_image = pygame.transform.scale(image1, (400, 400))
    new_image2 = pygame.transform.scale(image2, (400, 400))
    screen.blit(new_image, (10, 120))
    n=10
    while n!=-600:
     n-=1
     screen.blit(new_image2, (n, 120))
     pygame.display.update()
     screen.fill(GOLD)
     screen.blit(bg,(0,0))
def nikto(k,lk):
    image1 = pygame.image.load(k).convert_alpha()
    image2= pygame.image.load(lk).convert_alpha()
    screen.fill(GOLD)
    screen.blit(bg,(0,0))
    new_image = pygame.transform.scale(image1, (400, 400))
    new_image2 = pygame.transform.scale(image2, (400, 400))
    screen.blit(new_image, (10, 120))
    n=10
    k=180
    while n!=-100:
     k+=1
     n-=1
     screen.blit(new_image2, (n, 120))
     screen.blit(new_image, (k, 120))
     time.sleep(0.01)
     pygame.display.update()
     screen.fill(GOLD)
     screen.blit(bg,(0,0))
    screen.blit(new_image2, (n, 120))
    screen.blit(new_image, (k, 120))
    pygame.display.update()
    screen.fill(GOLD)
    screen.blit(bg,(0,0))
def draw_shield_bar(surf, x, y, pct):
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 10) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.display.update()
def one_two(sur,X,Y,TEXT):
    font = pygame.font.Font(None, 20)
    text = font.render(TEXT, True, WHITE)
    textpos = (X, Y)
    sur.blit(text,textpos)
    pygame.display.update()
def one_two1(sur,X,Y,TEXT):
    font = pygame.font.Font("sher.ttf", 35)
    text = font.render(TEXT, True, RED)
    textpos = (X, Y)
    sur.blit(text,textpos)
    pygame.display.update()
def texa(sur,X,Y,TEXT):
    font = pygame.font.Font("sher.ttf", 35)
    text = font.render(TEXT, True, WHITE)
    textpos = (X, Y)
    sur.blit(text,textpos)
    pygame.display.update()
def texaGreen(sur,X,Y,TEXT):
    font = pygame.font.Font("sher.ttf", 35)
    text = font.render(TEXT, True, GREEN)
    textpos = (X, Y)
    sur.blit(text,textpos)
    pygame.display.update()
def texaRed(sur,X,Y,TEXT):
    font = pygame.font.Font("sher.ttf", 35)
    text = font.render(TEXT, True, RED)
    textpos = (X, Y)
    sur.blit(text,textpos)
    pygame.display.update()
right_left(k,lk)
pygame.display.update()
htth=10
z=1
zhopa=0
songhh=pygame.mixer.Sound('ya1.mp3')
class Human(object):
    def __init__(self,ochko,hp,sila,lovkost,uroven):
        self.uroven=uroven
        self.hp=hp
        self.sila=sila
        self.lovkost=lovkost
        self.ochko=ochko
    def opit(self):
     global z,zhopa
     self.uroven+=zhopa/z
     return(self.uroven)
    def win(self):
      self.ochko+=1
      return(self.ochko)
    def lovkosE(self):
      self.lovkost-=1
      return(self.lovkost)

NEKIT = Human(0,3,1,1000,0)
Oleg = Human(0,3,1,0,0)
def obrabotkaLVL(Oleg,v):
 global htth,z,zhopa
 if (Oleg.uroven/z)>=htth+1: ####затруднение для прокачки
    htth+=10
    z+=1
 if Oleg.ochko==0:
    print("#%s"%(v),Oleg.opit(),"Уровень")
 else:
    dd=0
    dg=0
    dl=0
    while Oleg.ochko>0:
     imghp=pygame.image.load("hp.jpg").convert_alpha()
     new_imghp=pygame.transform.scale(imghp, (60,60))
     screen.blit(new_imghp, (300,60))
     imgsila=pygame.image.load("sila.jpg").convert_alpha()
     new_imgsila=pygame.transform.scale(imgsila, (60,60))
     screen.blit(new_imgsila, (100,60))
     imglovkost=pygame.image.load("lovkost.jpg").convert_alpha()
     new_imglovkost=pygame.transform.scale(imglovkost, (60,60))
     screen.blit(new_imglovkost, (200,60))
     for i in pygame.event.get():
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                positiion = pygame.mouse.get_pos()
                if positiion[0]>=100 and positiion[0]<=160 and positiion[1]>=60 and positiion[1]<=120:
                    dd+=1
                if positiion[0]>=200 and positiion[0]<=260 and positiion[1]>=60 and positiion[1]<=120:
                    dg+=1
                if positiion[0]>=300 and positiion[0]<=360 and positiion[1]>=60 and positiion[1]<=120:
                    dl+=2
     pygame.display.update()
     Oleg.ochko=Oleg.ochko-(dd+dg+dl)
     Oleg.sila+=dd
     Oleg.lovkost+=dg
     Oleg.hp+=dl
     zhopa=dd+dg+dl
 return(htth,z,zhopa)
def gameru(player,player2,y,UKL):
     if player==y[0] and player2==y[0]:
        songhh.play()
        k="2.png"
        lk="3.png"
        nikto(k,lk)
     if UKL!=1:
           if player==y[0] and player2==y[1]:
              songhh.play()
              ulo=[r for r in range(101)]
              lua=[random.choice(ulo)for t in range(Oleg.lovkost)]
              UKL=1
              ulo=random.randint(0,100)
              zzh=0
              for i in range(len(lua)):
                    if lua[i]==ulo:
                     zzh+=1
              if zzh>0:
               print("""
                ░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
                ░░░░░░░░░▄██████████▄░░░░░░░░░
                ░░░░░░░░▀░▄▄▄▄▄▄▄▄▄▄░▀░░░░░░░░
                ░░░░░░▄▄██████████████▄▄░░░░░░
                ░░░░░████████████████████░░░░░
                ░░░░████▀▀░░░░░░░░░░▀▀████░░░░
                ░░░░██████████████████████░░░░
                ░░▄█▀▀████▀▀██████▀▀███▀▀▀█▄░░
                ░░██░░░▀▀███▀▀██▀▀███▀▀░░░██░░
                ░░▀█▄▄▄░░░░░░▀▀▀▀░░░░░░▄▄▄█▀░░
                ░░░░▀▀█░░░▄██▀░░▀██▄░░░█▀▀░░░░
                ░░░░░░▀█▄██▀░████░▀██▄█▀░░░░░░
                ░░░░░░░░████▄░░░░▄████░░░░░░░░
                ░░░░░░░░░████████████░░░░░░░░░
                ░░░░░░▄▄██▀░░▀▀▀▀░░▀██▄▄░░░░░░
                ░░░▄██████▄░░░░░░░░▄██████▄░░░
                ░▄██████████▄░░░░▄██████████▄░""")
               NEKIT.hp-=Oleg.sila*2
               k="fuck.png"
               lk="3.png"
               right_left(k,lk)
               time.sleep(1)
               lk="3killz.png"
               proigral_left;
               print("2 игрок увернулся.И втыкает нож в спину.-%s хп"%(Oleg.sila*2))
               print("хп игрока #1=%s"%(NEKIT.hp))
               Oleg.win()
              else:
               k="noz4.png"
               lk="3.png"
               right_left(k,lk)
               time.sleep(1)
               k="noz4kill.png"
               proigral_right(k,lk)
               Oleg.hp-=NEKIT.sila
               print("2 игрок получает по лицу -%s хп"%(NEKIT.sila))
               print("хп игрока #2=%s"%(Oleg.hp))
               NEKIT.win()

           if player==y[0] and player2==y[2]:
              songhh.play()
              ulo=[r for r in range(101)]
              lua=[random.choice(ulo)for t in range(NEKIT.lovkost)]
              UKL=1
              ulo=random.randint(0,100)
              zzh=0
              for i in range(len(lua)):
                    if lua[i]==ulo:
                     zzh+=1
              if zzh>0:
               print("""
                ░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
                ░░░░░░░░░▄██████████▄░░░░░░░░░
                ░░░░░░░░▀░▄▄▄▄▄▄▄▄▄▄░▀░░░░░░░░
                ░░░░░░▄▄██████████████▄▄░░░░░░
                ░░░░░████████████████████░░░░░
                ░░░░████▀▀░░░░░░░░░░▀▀████░░░░
                ░░░░██████████████████████░░░░
                ░░▄█▀▀████▀▀██████▀▀███▀▀▀█▄░░
                ░░██░░░▀▀███▀▀██▀▀███▀▀░░░██░░
                ░░▀█▄▄▄░░░░░░▀▀▀▀░░░░░░▄▄▄█▀░░
                ░░░░▀▀█░░░▄██▀░░▀██▄░░░█▀▀░░░░
                ░░░░░░▀█▄██▀░████░▀██▄█▀░░░░░░
                ░░░░░░░░████▄░░░░▄████░░░░░░░░
                ░░░░░░░░░████████████░░░░░░░░░
                ░░░░░░▄▄██▀░░▀▀▀▀░░▀██▄▄░░░░░░
                ░░░▄██████▄░░░░░░░░▄██████▄░░░
                ░▄██████████▄░░░░▄██████████▄░""")
               Oleg.hp-=NEKIT.sila*2
               k="bumaga.png"
               lk="fuck.png"
               right_left(k,lk)
               time.sleep(1)
               lk="bumagakill.png"
               proigral_right(k,lk)
               print("1 игрок увернулся.И втыкает нож в спину.-%s хп"%(NEKIT.sila*2))
               print("хп игрока #2=%s"%(Oleg.hp))
               NEKIT.win()
              else:
               k="bumaga.png"
               lk="3.png"
               right_left(k,lk)
               time.sleep(1)
               lk="3killz.png"
               proigral_left(k,lk)
               NEKIT.hp-=Oleg.sila
               print("1 игрок получает по лицу -%s хп"%(Oleg.sila))
               print("хп игрока #1=%s"%(NEKIT.hp))
               Oleg.win()

           if player==y[1] and player2==y[0]:
              songhh.play()
              ulo=[r for r in range(101)]
              lua=[random.choice(ulo)for t in range(NEKIT.lovkost)]
              UKL=1
              ulo=random.randint(0,100)
              zzh=0
              for i in range(len(lua)):
                    if lua[i]==ulo:
                     zzh+=1
              if zzh>0:
               print("""
                ░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
                ░░░░░░░░░▄██████████▄░░░░░░░░░
                ░░░░░░░░▀░▄▄▄▄▄▄▄▄▄▄░▀░░░░░░░░
                ░░░░░░▄▄██████████████▄▄░░░░░░
                ░░░░░████████████████████░░░░░
                ░░░░████▀▀░░░░░░░░░░▀▀████░░░░
                ░░░░██████████████████████░░░░
                ░░▄█▀▀████▀▀██████▀▀███▀▀▀█▄░░
                ░░██░░░▀▀███▀▀██▀▀███▀▀░░░██░░
                ░░▀█▄▄▄░░░░░░▀▀▀▀░░░░░░▄▄▄█▀░░
                ░░░░▀▀█░░░▄██▀░░▀██▄░░░█▀▀░░░░
                ░░░░░░▀█▄██▀░████░▀██▄█▀░░░░░░
                ░░░░░░░░████▄░░░░▄████░░░░░░░░
                ░░░░░░░░░████████████░░░░░░░░░
                ░░░░░░▄▄██▀░░▀▀▀▀░░▀██▄▄░░░░░░
                ░░░▄██████▄░░░░░░░░▄██████▄░░░
                ░▄██████████▄░░░░▄██████████▄░""")
               Oleg.hp-=NEKIT.sila*2
               k="2.png"
               lk="fuck.png"
               right_left(k,lk)
               time.sleep(1)
               k="3kill.png"
               proigral_right(k,lk)
               print("1 игрок увернулся.И втыкает нож в спину.-%s хп"%(NEKIT.sila*2))
               print("хп игрока #2=%s"%(Oleg.hp))
               NEKIT.win()
              else:
               k="2.png"
               lk="nozz.png"
               right_left(k,lk)
               time.sleep(1)
               lk="nozzkill.png"
               proigral_left(k,lk)
               NEKIT.hp-=Oleg.sila
               print("1 игрок получает по лицу -%s хп"%(Oleg.sila))
               print("хп игрока #1=%s"%(NEKIT.hp))
               Oleg.win()

           if player==y[1] and player2==y[1]:
            songhh.play()
            print("в этой ожесточённой битве битве никто не выиграл.-1 хп у всех,никто очки не получает")
            k="noz4.png"
            lk="nozz.png"
            nikto(k,lk)


           if player==y[1] and player2==y[2]:
              songhh.play()
              ulo=[r for r in range(101)]
              lua=[random.choice(ulo)for t in range(Oleg.lovkost)]
              UKL=1
              ulo=random.randint(0,100)
              zzh=0
              for i in range(len(lua)):
                    if lua[i]==ulo:
                     zzh+=1
              if zzh>0:
               print("""
                ░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
                ░░░░░░░░░▄██████████▄░░░░░░░░░
                ░░░░░░░░▀░▄▄▄▄▄▄▄▄▄▄░▀░░░░░░░░
                ░░░░░░▄▄██████████████▄▄░░░░░░
                ░░░░░████████████████████░░░░░
                ░░░░████▀▀░░░░░░░░░░▀▀████░░░░
                ░░░░██████████████████████░░░░
                ░░▄█▀▀████▀▀██████▀▀███▀▀▀█▄░░
                ░░██░░░▀▀███▀▀██▀▀███▀▀░░░██░░
                ░░▀█▄▄▄░░░░░░▀▀▀▀░░░░░░▄▄▄█▀░░
                ░░░░▀▀█░░░▄██▀░░▀██▄░░░█▀▀░░░░
                ░░░░░░▀█▄██▀░████░▀██▄█▀░░░░░░
                ░░░░░░░░████▄░░░░▄████░░░░░░░░
                ░░░░░░░░░████████████░░░░░░░░░
                ░░░░░░▄▄██▀░░▀▀▀▀░░▀██▄▄░░░░░░
                ░░░▄██████▄░░░░░░░░▄██████▄░░░
                ░▄██████████▄░░░░▄██████████▄░""")
               print("2 игрок увернулся.И втыкает нож в спину.-%s хп"%(Oleg.sila*2))
               NEKIT.hp-=Oleg.sila*2
               k="fuck.png"
               lk="nozz.png"
               right_left(k,lk)
               time.sleep(1)
               lk="nozzkill.png"
               proigral_left(k,lk)
               print("хп игрока #1=%s"%(NEKIT.hp))
               Oleg.win()
              else:
               k="bumaga.png"
               lk="nozz.png"
               right_left(k,lk)
               time.sleep(1)
               k="bumagakill.png"
               proigral_right(k,lk)
               Oleg.hp-=NEKIT.sila
               print("2 игрок получает по лицу -%s хп"%(NEKIT.sila))
               print("хп игрока #2=%s"%(Oleg.hp))
               NEKIT.win()

           if player==y[2] and player2==y[0]:
              songhh.play()
              ulo=[r for r in range(101)]
              lua=[random.choice(ulo)for t in range(Oleg.lovkost)]
              UKL=1
              ulo=random.randint(0,100)
              zzh=0
              for i in range(len(lua)):
                    if lua[i]==ulo:
                     zzh+=1
              if zzh>0:
               print("""
                ░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
                ░░░░░░░░░▄██████████▄░░░░░░░░░
                ░░░░░░░░▀░▄▄▄▄▄▄▄▄▄▄░▀░░░░░░░░
                ░░░░░░▄▄██████████████▄▄░░░░░░
                ░░░░░████████████████████░░░░░
                ░░░░████▀▀░░░░░░░░░░▀▀████░░░░
                ░░░░██████████████████████░░░░
                ░░▄█▀▀████▀▀██████▀▀███▀▀▀█▄░░
                ░░██░░░▀▀███▀▀██▀▀███▀▀░░░██░░
                ░░▀█▄▄▄░░░░░░▀▀▀▀░░░░░░▄▄▄█▀░░
                ░░░░▀▀█░░░▄██▀░░▀██▄░░░█▀▀░░░░
                ░░░░░░▀█▄██▀░████░▀██▄█▀░░░░░░
                ░░░░░░░░████▄░░░░▄████░░░░░░░░
                ░░░░░░░░░████████████░░░░░░░░░
                ░░░░░░▄▄██▀░░▀▀▀▀░░▀██▄▄░░░░░░
                ░░░▄██████▄░░░░░░░░▄██████▄░░░
                ░▄██████████▄░░░░▄██████████▄░""")
               NEKIT.hp-=Oleg.sila*2
               print("2 игрок увернулся.И втыкает нож в спину.-%s хп"%(Oleg.sila*2))
               print("хп игрока #1=%s"%(NEKIT.hp))
               k="fuck.png"
               lk="bumaga1.png"
               right_left(k,lk)
               time.sleep(1)
               lk="bumaga1kill.png"
               proigral_left(k,lk)
               Oleg.win()
              else:
               k="2.png"
               lk="bumaga1.png"
               right_left(k,lk)
               time.sleep(1)
               k="3kill.png"
               proigral_right(k,lk)
               Oleg.hp-=NEKIT.sila
               print("2 игрок получает по лицу -%s хп"%(NEKIT.sila))
               print("хп игрока #2=%s"%(Oleg.hp))
               NEKIT.win()

           if player==y[2] and player2==y[1]:
              songhh.play()
              ulo=[r for r in range(101)]
              lua=[random.choice(ulo)for t in range(NEKIT.lovkost)]
              UKL=1
              ulo=random.randint(0,100)
              zzh=0
              for i in range(len(lua)):
                    if lua[i]==ulo:
                     zzh+=1

              if zzh>0:
               print("""
                ░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
                ░░░░░░░░░▄██████████▄░░░░░░░░░
                ░░░░░░░░▀░▄▄▄▄▄▄▄▄▄▄░▀░░░░░░░░
                ░░░░░░▄▄██████████████▄▄░░░░░░
                ░░░░░████████████████████░░░░░
                ░░░░████▀▀░░░░░░░░░░▀▀████░░░░
                ░░░░██████████████████████░░░░
                ░░▄█▀▀████▀▀██████▀▀███▀▀▀█▄░░
                ░░██░░░▀▀███▀▀██▀▀███▀▀░░░██░░
                ░░▀█▄▄▄░░░░░░▀▀▀▀░░░░░░▄▄▄█▀░░
                ░░░░▀▀█░░░▄██▀░░▀██▄░░░█▀▀░░░░
                ░░░░░░▀█▄██▀░████░▀██▄█▀░░░░░░
                ░░░░░░░░████▄░░░░▄████░░░░░░░░
                ░░░░░░░░░████████████░░░░░░░░░
                ░░░░░░▄▄██▀░░▀▀▀▀░░▀██▄▄░░░░░░
                ░░░▄██████▄░░░░░░░░▄██████▄░░░
                ░▄██████████▄░░░░▄██████████▄░""")
               Oleg.hp-=NEKIT.sila*2
               k="noz4.png"
               lk="fuck.png"
               right_left(k,lk)
               time.sleep(1)
               k="noz4kill.png"
               proigral_right(k,lk)
               print("1 игрок увернулся.И втыкает нож в спину.-%s хп"%(NEKIT.sila*2))
               print("хп игрока #2=%s"%(Oleg.hp))
               NEKIT.win()
              else:
               k="noz4.png"
               lk="bumaga1.png"
               right_left(k,lk)
               time.sleep(1)
               lk="bumaga1kill.png"
               proigral_left(k,lk)
               NEKIT.hp-=Oleg.sila
               print("1 игрок получает по лицу -%s хп"%(Oleg.sila))
               print("хп игрока #1=%s"%(NEKIT.hp))
               Oleg.win()

           if player==y[2] and player2==y[2]:
               songhh.play()
               k="bumaga.png"
               lk="bumaga1.png"
               nikto(k,lk)

piki=0
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    nlox=120
    draw_shield_bar(screen, 180, 200, Oleg.hp)
    draw_shield_bar(screen, 180, 180, NEKIT.hp)
    one_two(screen,nlox,180,"Левый")
    one_two(screen,nlox,200,"Правый")
    if pygame.mixer.music.get_busy()==False:
      pygame.mixer.music.load(gf[0])
      pik+=1
      if pik!=len(gf):
       pygame.mixer.music.play()
    draw_shield_bar(screen, 180, 200, Oleg.hp)
    draw_shield_bar(screen, 180, 180, NEKIT.hp)
    one_two(screen,nlox,180,"Левый")
    one_two(screen,nlox,200,"Правый")
    UKL=0
    player=0
    player2=0
    if player==0 and player2==0:
        piki+=1
        right_left(k,lk)
        draw_shield_bar(screen, 180, 200, Oleg.hp)
        draw_shield_bar(screen, 180, 180, NEKIT.hp)
        one_two(screen,nlox,180,"Левый")
        one_two(screen,nlox,200,"Правый")
        if piki==1:
         one_two1(screen,280,60,"3")
        if piki==2:
         one_two1(screen,280,60,"2")
        if piki==3:
         one_two1(screen,200,60,"Нажимайте")
         piki=0
        time.sleep(1)

        right_left_stuk(k,lk)
        draw_shield_bar(screen, 180, 200, Oleg.hp)
        draw_shield_bar(screen, 180, 180, NEKIT.hp)
        one_two(screen,nlox,180,"Левый")
        one_two(screen,nlox,200,"Правый")
        time.sleep(1)



        y=["Камень","Ножницы","Бумага"]
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_1:
                    player=y[0]
                elif i.key == pygame.K_2:
                    player=y[1]
                elif i.key == pygame.K_3:
                    player=y[2]
                elif i.key == pygame.K_8:
                    player2=y[0]
                elif i.key == pygame.K_9:
                    player2=y[1]
                elif i.key == pygame.K_0:
                    player2=y[2]
        gameru(player,player2,y,UKL)
        draw_shield_bar(screen, 180, 200, Oleg.hp)
        draw_shield_bar(screen, 180, 180, NEKIT.hp)
        one_two(screen,nlox,180,"Левый")
        one_two(screen,nlox,200,"Правый")



        if NEKIT.ochko!=0:
            obrabotkaLVL(NEKIT,1)
            NEKIT.opit()

        if Oleg.ochko!=0:
            obrabotkaLVL(Oleg,2)
            Oleg.opit()

        if Oleg.hp<=0:
            tyh1+=1
            texa(screen,110,250,"левый игрок выиграл".upper())
            texaGreen(screen,270,300,str(tyh1))
            texaRed(screen,310,300,str(tyh2))
            time.sleep(3)
            NEKIT.sila=1
            NEKIT.hp=3
            NEKIT.ochko=0
            NEKIT.uroven=0
            NEKIT.lovkost=0
            Oleg.sila=1
            Oleg.hp=3
            Oleg.ochko=0
            Oleg.uroven=0
            Oleg.lovkost=0
        if NEKIT.hp<=0:
            tyh2+=1
            texa(screen,110,250,"правый игрок выиграл".upper())
            texaRed(screen,270,300,str(tyh1))
            texaGreen(screen,310,300,str(tyh2))
            time.sleep(3)
            NEKIT.sila=1
            NEKIT.hp=3
            NEKIT.ochko=0
            NEKIT.uroven=0
            NEKIT.lovkost=0
            Oleg.sila=1
            Oleg.hp=3
            Oleg.ochko=0
            Oleg.uroven=0
            Oleg.lovkost=0
pygame.quit()

















































