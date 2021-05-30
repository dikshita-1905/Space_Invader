import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
#background
bg = pygame.image.load("bg.png")


pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("rocket.png")
playerX = 370
playerY = 480
playerX_change = 0


# enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("coronavirus.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(5)
    enemyY_change.append(40)

# bullet
#Ready=You cant see the bullet on the screen
#Fire=The bullet is moving

bulletImg = pygame.image.load("vaccine.png")
bulletX = 0                                  #we will change the value in our while loop
bulletY = 480
bulletX_change = 0
bulletY_change=10 #we want the bullet to move with the speed of 10
bullet_state="ready"

score=0
def player(x, y):
    screen.blit(playerImg, (x, y))  # blit means to draw


def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))  # blit means to draw

def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    # playerX-=0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # IF KEYSTOKE IS PRESSED  CHECK WHETHER ITS RIGHT OR LEFT
        if event.type == pygame.KEYDOWN:  # this means that a keystroke has been pressed on the computer
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                   bulletX=playerX
                   fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    screen.fill((0, 0, 0))  # tuple
    #background image
    screen.blit(bg,(0,0))
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy Movement
    for i in range(num_of_enemies):
         enemyX[i] += enemyX_change[i]
    if enemyX[i] <= 0:
        enemyX_change[i] = 4
        enemyY[i] +=enemyY_change[i]
    elif enemyX[i] >= 736:
        enemyX_change[i] = -4
        enemyY[i] += enemyY_change[i]

        # collision
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX[i] = random.randint(0, 735)
        enemyY[i] = random.randint(50, 150)
    enemy(enemyX[i], enemyY[i],i)


    #Bullet movement
    if bulletY<=0 :
        bulletY=480
        bullet_state='ready'
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change


    player(playerX, playerY)

    pygame.display.update()
