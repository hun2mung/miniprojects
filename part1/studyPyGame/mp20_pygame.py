# Python Game - PyGame Game Framework
# pip install pygame
import pygame   # pygame 선언

pygame.init()   # 게임초기화

height = 500
width = 500

win = pygame.display.set_mode((height,width))    # 창 크기 500*500
pygame.display.set_caption('게임 만들기')
icon = pygame.image.load('./studyPyGame/gameicon.png')
pygame.display.set_icon(icon)

# object
x = 250
y = 250
radius = 10
vel_x = 10
vel_y = 10
jump = False

run = True

while run:
    win.fill('Blue')    # 윈도우 전체 배경

    pygame.draw.circle(win, (255,255,255), (x, y), radius)    # 흰 공 그리기

    # 이벤트 = 시그널
    for event in pygame.event.get():    #이벤트 받기
        if event.type == pygame.QUIT:
            run = False
    
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 10:
        x -= vel_x    # 왼쪽으로 10 이동
    if userInput[pygame.K_RIGHT] and x < width - 10:
        x += vel_x    # 오른쪽으로 10 이동    
    # if userInput[pygame.K_UP] and y > 10:
    #     y -= vel_x    # 위쪽으로 10 이동    
    # if userInput[pygame.K_DOWN] and y< height - 10:
    #     y += vel_x    # 아래쪽으로 10 이동    

    # 객체 점프
    if jump == False and userInput[pygame.K_SPACE]:
        jump = True
    if jump == True:
        y -= vel_y * 3
        vel_y -=1
        if vel_y < -10:
            jump = False
            vel_y = 10

    pygame.time.delay(10)
    pygame.display.update()     # 화면 업데이트(전환)

