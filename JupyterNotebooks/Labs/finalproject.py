#imports and initiate pygame
import pygame
import time
import random
pygame.init()

#colors
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (225, 0, 0)
green = (0, 155, 0)
purple = (210, 165, 255)

#window display and caption
disiplay_width = 600
display_height = 400
dis = pygame.display.set_mode((disiplay_width, display_height))
pygame.display.set_caption('snake')

clock = pygame.time.Clock()

#snake variables
snake_square = 10
snake_speed = 15

#text fonts
font_style = pygame.font.SysFont("arial", 20)
score_font = pygame.font.SysFont("times new roman", 20)

#scoreboard
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

#drawing the snake
def our_snake(snake_square, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_square, snake_square])

#game end messgae and position
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [disiplay_width / 6, display_height / 3])

#defining the loop
def gameLoop():
    game_over = False
    game_close = False
    x1 = disiplay_width / 2
    y1 = display_height / 2
    x1_change = 0
    y1_change = 0

#snake length
    snake_List = []
    Length_of_snake = 1

#apple randomization
    applex = round(random.randrange(0, disiplay_width - snake_square) / 10.0) * 10.0
    appley = round(random.randrange(0, display_height - snake_square) / 10.0) * 10.0

    while not game_over:

        #game over message
        while game_close == True:
            dis.fill(purple)
            message("Game over! Press Space to play again or Q to quit", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            #game end options to quit or keep playing
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        #snake movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_square
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_square
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_square
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_square
                    x1_change = 0

        #game over due to snake breaking boundary
        if x1 >= disiplay_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(purple)

        #drawing the apple
        pygame.draw.rect(dis, green, [applex, appley, snake_square, snake_square])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        #not letting snake make a 180 degree turn without turning left or right
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_square, snake_List)
        your_score(Length_of_snake - 1)
        pygame.display.update()

        #when snake position = apple position, increase length and move the apple
        if x1 == applex and y1 == appley:
            applex = round(random.randrange(0, disiplay_width - snake_square) / 10.0) * 10.0
            appley = round(random.randrange(0, display_height - snake_square) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()