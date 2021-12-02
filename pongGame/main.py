import pygame
import math

pygame.init()

sc = pygame.display.set_mode((700, 400))

pygame.display.set_caption("PongGame by Anvin")
icon = pygame.image.load("pong.png")
pygame.display.set_icon(icon)

background = pygame.image.load("bg1.png")

playerAy = 160
playerBy = 160
playerAy_change = 0
playerBy_change = 0
playerA = pygame.Rect(10, playerAy, 10, 80)
playerB = pygame.Rect(680, playerBy, 10, 80)

# ball
ball = pygame.image.load("ball.png")
ballX = 338
ballY = 188
ballX_change = 0.041
ballY_change = 0.072

over_font = pygame.font.Font("game_over.ttf", 150)
font = pygame.font.Font("Typewriter.ttf", 25)
win = pygame.font.Font("Typewriter.ttf", 15)
playagain_font = pygame.font.Font("Typewriter.ttf", 15)


def playagain_text():
    over_text = playagain_font.render(" Press 'Q' to Play Again ", True, (255, 255, 255))
    sc.blit(over_text, (253, 227))


def to_win_text():
    win_text = win.render("First to score '5' WINS", True, (0, 0, 0))
    sc.blit(win_text, (259, 1))

def show_scoreA(x, y):
    score = font.render("Score : " + str(scoreA), True, (0, 0, 0))
    sc.blit(score, (x, y))


def show_scoreB(x, y):
    score = font.render("Score : " + str(scoreB), True, (0, 0, 0))
    sc.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    sc.blit(over_text, (178, 150))


def player(x, y):
    pygame.draw.rect(sc, (0, 0, 0), pygame.Rect(10, x, 10, 80))
    pygame.draw.rect(sc, (0, 0, 0), pygame.Rect(680, y, 10, 80))


def pong_ball(x, y):
    sc.blit(ball, (x, y))


scoreA = 0
scoreB = 0
count = 1
count1 = 0
running = True
while running:
    sc.fill((0, 0, 0))
    sc.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # player A
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerAy_change = -0.2
            if event.key == pygame.K_s:
                playerAy_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerAy_change = 0

        # player B
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerBy_change = -0.2
            if event.key == pygame.K_DOWN:
                playerBy_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerBy_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                ballX = 338
                ballY = 188
                ballX_change = 0.041
                ballY_change = 0.072
                scoreA = 0
                scoreB = 0


    playerAy += playerAy_change
    if playerAy <= 5:
        playerAy_change = 0
    elif playerAy >= 315:
        playerAy_change = 0

    playerBy += playerBy_change
    if playerBy <= 5:
        playerBy_change = 0
    elif playerBy >= 315:
        playerBy_change = 0

    ballX += ballX_change

    ballY += ballY_change
    if (ballY <= 0) or (ballY >= 371):
        ballY_change = -ballY_change

    ballX += ballX_change

    if ballX + 24 >= 680 and ((ballY + 12) >= playerBy and ballY + 12 <= playerBy + 80):
        ballX_change = -ballX_change
    if ballX <= 20 and ((ballY + 12) >= playerAy and ballY + 12 <= playerAy + 80):
        ballX_change = -ballX_change
        count += 1
        if count % 2 == 0:
            ballX_change = ballX_change * 1.2
            ballY_change = ballY_change * 1.2

    if ballX + 24 >= 681:
        scoreA += 1
        count1 += 1
        ballX = 338
        ballY = 188
        ballX_change = -0.041 * pow(1.3, count1)
        ballY_change = 0.072 * pow(1.3, count1)

    if ballX <= 19:
        scoreB += 1
        ballX = 338
        ballY = 188
        ballX_change = 0.041 * pow(1.3, count1)
        ballY_change = 0.072 * pow(1.3, count1)

    if scoreA >= 5 or scoreB >= 5:
        ballX = 338
        ballY = 250
        ballX_change = 0
        ballY_change = 0
        game_over_text()
        playagain_text()

    pong_ball(ballX, ballY)
    player(playerAy, playerBy)
    show_scoreA(5, 2)
    show_scoreB(585, 2)
    to_win_text()
    pygame.display.update()
