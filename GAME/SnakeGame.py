import sys
try:
    import pygame
except ImportError:
    print(' Please install requirements.')
    sys.exit(1)
import time, random
from pygame.locals import *

pygame.init()
clock= pygame.time.Clock()
screen=pygame.display.set_mode((650,650),0,32)
snake=[pygame.Rect(288,300,12,12)]
left=True
right=False
up=False
down=False
i=0
part=[]
check=0
x=[]
c=0
m=0
i=0
food=True
black=(0,0,0)
death=[]*4
l=[]
refood=[24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168, 180, 192, 204, 216, 228, 240, 252, 264, 276, 288, 300, 312, 324, 336, 348, 360, 372, 384, 396, 408, 420, 432, 444, 456, 468, 480, 492, 504, 516, 528, 540, 552, 564, 576, 588]
it=False
def pause():
    while True:
        f=''
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==ord('p'):
                    f='stop'
                    break
        if f=='stop':
            break
while True:
    death.append(pygame.Rect(0,0,12,12))
    death.append(pygame.Rect(640,0,12,12))
    death.append(pygame.Rect(3,0,12,12))
    death.append(pygame.Rect(3,640,12,12))

    if food==True:
        x=random.randint(0,47)
        y=random.randint(0,47)
        en=pygame.Rect(refood[x],refood[y],12,12)

        food=False

    screen.fill(black)
    for d in death[:]:
        pygame.draw.rect(screen,(255,255,255),d)
    for d in death[:]:
        if d.colliderect(snake[len(snake)-1]):
            pygame.quit()
            sys.exit()
    for p in part[:]:
        if p.colliderect(snake[len(snake)-1]):
            pygame.quit()
            sys.exit()
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==ord('q'):
                pygame.quit()
                sys.exit()
            if event.key==ord('p'):
                pause()
            if event.key==K_UP:
                if left==True:
                    for s in snake[:len(snake)-1]:
                        part.append(s)
                        snake.remove(s)

                    up=True
                    down=False
                    left=False
                    right=False

                if right==True:
                    for s in snake[:len(snake)-1]:
                        part.append(s)
                        snake.remove(s)
                    up=True
                    down=False
                    left=False
                    right=False

                break
            if event.key==K_DOWN:

                if left==True:
                    for s in snake[:len(snake)-1]:
                        part.append(s)
                        snake.remove(s)
                    up=False
                    down=True
                    left=False
                    right=False

                if right==True:
                    for s in snake[:len(snake)-1]:
                        part.append(s)
                        snake.remove(s)
                    up=False
                    down=True
                    left=False
                    right=False

                break
            if event.key==K_LEFT:
                if up==True:
                    for s in snake[:len(snake)-1]:
                        part.append(s)
                        snake.remove(s)

                    up=False
                    down=False
                    left=True
                    right=False




                if down==True:
                    for s in snake[:len(snake)-1]:
                        part.append(s)
                        snake.remove(s)

                    up=False
                    down=False
                    left=True
                    right=False

                break
            if event.key==K_RIGHT:
                if up==True:
                    for s in snake[:len(snake)-1]:
                        part.append(s)
                        snake.remove(s)
                    up=False
                    down=False
                    left=False
                    right=True

                if down==True:
                    for s in snake[:len(snake)-1]:
                        part.append(s)
                        snake.remove(s)
                    up=False
                    down=False
                    left=False
                    right=True

                break

    if len(part)==0:
        if en.colliderect(snake[len(snake)-1]):
            if left==True:
                snake.append(pygame.Rect(snake[len(snake)-1].left-12,snake[len(snake)-1].top,12,12))
                if snake[len(snake)-1].left<0:
                    del snake[len(snake)-1]
                    snake.append(636,snake[len(snake)-1].top,12,12)

            if right==True:

                snake.append(pygame.Rect(snake[len(snake)-1].right,snake[len(snake)-1].top,12,12))
                if snake[len(snake)-1].right>648:
                    del snake[len(snake)-1]
                    snake.append(pygame.Rect(12,snake[len(snake)-1].top,12,12))
            if up==True:
                snake.append(pygame.Rect(snake[len(snake)-1].left,snake[len(snake)-1].top-12,12,12))
                if snake[len(snake)-1].top<0:
                    del snake[len(snake)-1]
                    snake.append(snake[len(snake)-1].left,636,12,12)
            if down==True:
                snake.append(pygame.Rect(snake[len(snake)-1].left,snake[len(snake)-1].bottom,12,12))
                if snake[len(snake)-1].bottom>648:
                    del snake[len(snake)-1]
                    snake.append(snake[len(snake)-1].left,12,12,12)

            en=0
            food=True
        else:
            for s in snake[:]:
                if left==True:
                    s.left-=12
                    if s.left<0:
                        s.left=636
                if right==True:
                    s.left+=12
                    if s.right>648:
                        s.left=0
                if up==True:
                    s.top-=12
                    if s.top<0:
                        s.top=636
                if down==True:
                    s.top+=12
                    if s.bottom>648:
                        s.top=0

    if len(part)>0:
        if en.colliderect(snake[len(snake)-1]):
            if left==True:
                snake.append(pygame.Rect(snake[len(snake)-1].left-12,snake[len(snake)-1].top,12,12))

            if right==True:
                snake.append(pygame.Rect(snake[len(snake)-1].right,snake[len(snake)-1].top,12,12))
            if up==True:
                snake.append(pygame.Rect(snake[len(snake)-1].left,snake[len(snake)-1].top-12,12,12))
            if down==True:
                snake.append(pygame.Rect(snake[len(snake)-1].left,snake[len(snake)-1].bottom,12,12))
            en=0
            food=True
        else:
            if left==True:
                snake.append(pygame.Rect(snake[len(snake)-1].left-12,snake[len(snake)-1].top,12,12))
                del part[0]
                if snake[len(snake)-1].left<0:
                    del snake[len(snake)-1]
                    snake.append(pygame.Rect(636,snake[len(snake)-1].top,12,12))
            if right==True:
                snake.append(pygame.Rect(snake[len(snake)-1].right,snake[len(snake)-1].top,12,12))
                del part[0]
                if snake[len(snake)-1].right>648:
                    del snake[len(snake)-1]
                    snake.append(pygame.Rect(0,snake[len(snake)-1].top,12,12))
            if up==True:
                snake.append(pygame.Rect(snake[len(snake)-1].left,snake[len(snake)-1].top-12,12,12))
                del part[0]
                if snake[len(snake)-1].top<0:
                    del snake[len(snake)-1]
                    snake.append(pygame.Rect(snake[len(snake)-1].left,636,12,12))
            if down==True:
                snake.append(pygame.Rect(snake[len(snake)-1].left,snake[len(snake)-1].bottom,12,12))
                del part[0]
                if snake[len(snake)-1].bottom>648:
                    del snake[len(snake)-1]
                    snake.append(pygame.Rect(snake[len(snake)-1].left,0,12,12))
    for s in snake[:]:

        pygame.draw.rect(screen,(25,25,25),s)
    for p in part[:]:
        pygame.draw.rect(screen,(25,25,25),p)
    if en!=0:
        pygame.draw.rect(screen,(45,54,45),en)
    for p in part[:]:
        if p.colliderect(snake[len(snake)-1]):
            pygame.quit()
            sys.exit()
    for d in death[:]:
        death.remove(d)
    time.sleep(0.1)

    pygame.display.update()
    c=0
    check=0
