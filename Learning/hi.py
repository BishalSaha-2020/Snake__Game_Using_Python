import pygame
import random
x=pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
col=(55,155,100)
black=(0,0,0)

#Creating window

gameWindow=pygame.display.set_mode((900,500))
pygame.display.set_caption("The Bishal Game")
pygame.display.update()

#variable

exit_game=False
game_over=False
score=0
snake_x=45
snake_y=45
snake_size=20
snake_sizey=20
velocity_x=0
velocity_y=0
init_velocity=5
fps=60

food_x=random.randint(25,900/2)
food_y=random.randint(25,500/2)


clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])



snk_list=[]
snk_length=1


def plot_snake(gameWindow,color,snk_list,snake_size):
    print(snk_list)
    for x,y in snk_list:

        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_sizey])


while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:

            if (event.key==pygame.K_RIGHT) :
               velocity_x=init_velocity
               velocity_y=0

            if (event.key==pygame.K_LEFT) :
                velocity_x=-init_velocity
                velocity_y=0

            if (event.key==pygame.K_UP) :
                velocity_y=-init_velocity
                velocity_x=0

            if (event.key==pygame.K_DOWN) :
                velocity_y=init_velocity
                velocity_x=0

    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y
    
    if abs(snake_x-food_x)<12 and (snake_y-food_y)<12 and (food_x-snake_x)<12 and (food_y-snake_y)<12:
        score=(score+1)
        
        text_screen("score : "+str(score*5),col,5,5)
        food_x=random.randint(25,900/2)
        food_y=random.randint(25,500/2)
        snk_length=snk_length+5
        
        

        

    gameWindow.fill(white)
    text_screen("score : "+str(score*10),col,700,400)
   # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_sizey])
    pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_sizey])
    

    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    

    if len(snk_list) > snk_length:
        del snk_list[0]
     
    plot_snake(gameWindow,black,snk_list,snake_size)

    pygame.display.update()
    clock.tick(fps)
   
pygame.quit()
quit()