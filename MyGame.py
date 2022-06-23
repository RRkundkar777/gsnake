import pygame
import random

pygame.init() # Initializes the dependencies of pygame

pygame.mixer.init()



# Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
rb = (255,0,128)

# Screen Size Variables
width = 1200
height = 660

gameWindow = pygame.display.set_mode((width,height))   # A game window of pygame

back = pygame.image.load("Py.jpg")
back = pygame.transform.scale(back,(width,height)).convert_alpha()

pygame.display.set_caption("Feed the Snake") # The title of any game
pygame.display.update() # Updates the window


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,60)
font2 = pygame.font.SysFont(None,30)



def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def txt_screen(text,color,x,y):
    screen_text = font2.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
    
def Toggle(value):
    if value == True:
        value = False
    else:
        value = True
 

music = True
# A gameloop
def gameloop():
        # Game Variables
    exit_game = False
    game_over = False
    pause = False
    tazer = False
    speed = False
    snake_x = 340
    snake_y = 55
    snake_size = 20
    fps = 35
    vel_x = 0
    vel_y = 0
    thrust = 0
    food_x = random.randint(20,width-20)
    food_y = random.randint(20,height-20)
    score = 0
    snake_list = []
    snake_length = 1

    global music
    with open('hiscore.txt','r') as f:
         hiscore = f.read()

    if music:
        pygame.mixer.music.load('Back.mp3')
        pygame.mixer.music.play()


    while not exit_game:
        if game_over:
            with open('hiscore.txt','w') as f:
                f.write(str(hiscore))
            gameWindow.fill(black)
            text_screen('Game Over Press Enter to Continue',red,width-1000,height-360)
            music = False
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('Back.mp3')
                        pygame.mixer.music.play()
                        gameloop()

            
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
            

                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                    if event.key == pygame.K_RIGHT:
                        vel_x = 10 + thrust; vel_y = 0;pause = False
                    if event.key == pygame.K_LEFT:
                        vel_x = -10 - thrust; vel_y = 0;pause = False
                    if event.key == pygame.K_UP:
                        vel_y = -10 - thrust; vel_x = 0;pause = False
                    if event.key == pygame.K_DOWN:
                        vel_y = 10 + thrust; vel_x = 0;pause = False
                    if event.key == pygame.K_p:
                        vel_x,vel_y = 0,0; pause = True
                    if event.key == pygame.K_s:
                        thrust += 4 ; speed = True ; tazer = False
                    if event.key == pygame.K_t:
                        speed = False; tazer = True
                        thrust += -3
                       

                    

            if abs(snake_x-food_x)<7 and abs(snake_y-food_y)<7:
                score += 10
                food_x = random.randint(20,width-20)
                food_y = random.randint(20,height-20)
                snake_length += 1
                if score>int(hiscore):
                    hiscore = score
            


            if snake_x>(width - 10):
                snake_x = 10
            elif snake_x<5:
                snake_x = width - 10
            elif snake_y>(height - 10):
                snake_y = 10
            elif snake_y<10:
                snake_y = height - 10
                
            gameWindow.fill(white)
            gameWindow.blit(back,(0,0))

            if pause:
                text_screen('Paused...',green,600-70,300)
            
            if speed:
                text_screen('HyperSpeed...',black,10,130)
            
            if tazer:
                text_screen('Tazered...',black,10,130)
                
                
            text_screen('Score: ' + str(score) ,red,10,10)
            text_screen('Hi Score: ' + str(hiscore) ,green,10,70) 
            txt_screen("Appleton",white,width-100,height-25) 
            pygame.draw.rect(gameWindow,blue,[0,0,5,height])
            pygame.draw.rect(gameWindow,blue,[0,0,width,5])
            pygame.draw.rect(gameWindow,blue,[0,height-5,width,5])
            pygame.draw.rect(gameWindow,blue,[width-5,0,5,height])

            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            
            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
            plot_snake(gameWindow,black,snake_list,snake_size)
            snake_x += vel_x
            snake_y += vel_y
            
        pygame.display.update()
        clock.tick(fps)
            
           



    pygame.quit()
    quit()

if __name__ == "__main__":
    gameloop()
    # Ai.takeCommand()