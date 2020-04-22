import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

pygame.mixer.music.load('05 Fast Lane (Dirty).mp3')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NEON = (57, 255, 20)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(BLUE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(RED, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

ball2 = Ball(WHITE, 10, 10)
ball2.rect.x = 345
ball2.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
all_sprites_list.add(ball2)
carryOn = True

clock = pygame.time.Clock()

scoreA = 19
scoreB = 0
intro = True
LEVAL = 0


def textobj(text, font, color=WHITE):
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


def gameOver(scoreA, scoreB):
    quit = False
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    startScreen(True)

        screen.fill(WHITE)
        if scoreA > scoreB:
            largetxt = pygame.font.Font('digital-7.ttf', 80)
            textsurf, textrect = textobj("PLAYER -A- WIN'S", largetxt, BLUE)
            textrect.center = ((700 / 2), (200))
            screen.blit(textsurf, textrect)

            largetxt = pygame.font.Font(None, 30)
            textsurf, textrect = textobj("PRESS ENTER TO PLAY AGAIN", largetxt, RED)
            textrect.center = ((700 / 2), (300))
            screen.blit(textsurf, textrect)

        if scoreB > scoreA:
            largetxt = pygame.font.Font('digital-7.ttf', 100)
            textsurf, textrect = textobj("PLAYER -B- WIN'S", largetxt, RED)
            textrect.center = ((700 / 2), (200))
            screen.blit(textsurf, textrect)

            largetxt = pygame.font.Font(None, 30)
            textsurf, textrect = textobj("PRESS ENTER TO PLAY AGAIN", largetxt, BLUE)
            textrect.center = ((700 / 2), (300))
            screen.blit(textsurf, textrect)

        pygame.display.update()
        clock.tick(15)


def game_Easy(carryOn, LEVAL, scoreA, scoreB):
    all_sprites_list.remove(ball2)
    pygame.mixer.music.play(-1)
    print("EASY")
    while carryOn and LEVAL == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carryOn = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)

        all_sprites_list.update()

        if ball.rect.x >= 690:
            scoreA += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            scoreB += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        # --------------END GAME----------------
        if int(scoreA) == 20 or int(scoreB) == 20:
            carryOn = False
            gameOver(scoreA, scoreB)

        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()

        screen.fill(BLACK)

        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

        all_sprites_list.draw(screen)

        font = pygame.font.Font('digital-7.ttf', 74)
        text = font.render(str(scoreA), 1, NEON)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), 1, NEON)
        screen.blit(text, (420, 10))

        pygame.display.flip()

        clock.tick(60)


def game_Diffcult(carryOn, LEVAL, scoreA, scoreB):
    pygame.mixer.music.play(-1)
    print("DIFFICULT")
    while carryOn and LEVAL == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carryOn = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)

        all_sprites_list.update()

        if ball.rect.x >= 690:
            scoreA += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            scoreB += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        if ball2.rect.x >= 690:
            scoreA += 1
            ball2.velocity[0] = -ball2.velocity[0]
        if ball2.rect.x <= 0:
            scoreB += 1
            ball2.velocity[0] = -ball2.velocity[0]
        if ball2.rect.y > 490:
            ball2.velocity[1] = -ball2.velocity[1]
        if ball2.rect.y < 0:
            ball2.velocity[1] = -ball2.velocity[1]

        # -----------------END GAME---------------
        if int(scoreA) == 50 or int(scoreB) == 50:
            carryOn = False
            gameOver(scoreA, scoreB)

        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            ball.bounce()
        if pygame.sprite.collide_mask(ball2, paddleA) or pygame.sprite.collide_mask(ball2, paddleB):
            ball2.bounce()

        screen.fill(BLACK)

        pygame.draw.line(screen, NEON, [349, 0], [349, 500], 5)

        all_sprites_list.draw(screen)

        font = pygame.font.Font('digital-7.ttf', 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (420, 10))

        pygame.display.flip()

        clock.tick(60)


def startScreen(intro, scoreA=0, scoreB=0):
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    LEVAL = 1
                    intro = False
                    game_Easy(carryOn, LEVAL, scoreA, scoreB)
                    break
                if event.key == pygame.K_2:
                    LEVAL = 2
                    intro = False
                    game_Diffcult(carryOn, LEVAL, scoreA, scoreB)
                    break

        screen.fill(BLACK)
        largetxt = pygame.font.Font('digital-7.ttf', 100)
        textsurf, textrect = textobj("PONG", largetxt, NEON)
        textrect.center = ((700 / 2), (200 / 2))
        screen.blit(textsurf, textrect)

        smalltxt = pygame.font.Font('freesansbold.ttf', 30)
        textsurf, textrect = textobj("Press 1 - EASY ", smalltxt)
        textrect.center = ((700 / 2), (400 / 2))
        screen.blit(textsurf, textrect)

        smalltxt = pygame.font.Font('freesansbold.ttf', 30)
        textsurf, textrect = textobj("Press 2 - DIFFICULT ", smalltxt)
        textrect.center = ((700 / 2), (250))
        screen.blit(textsurf, textrect)

        pygame.display.update()
        clock.tick(15)


startScreen(True)
pygame.quit()
