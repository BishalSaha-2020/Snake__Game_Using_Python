import pygame
import random
import time
x=pygame.init()

pygame.mixer.init()



#colors
white=(255,255,255)
red=(255,0,0)

col=(0,0,0)
lol=(139,69,19)
black=	(255,255,0)

#Creating window

gameWindow=pygame.display.set_mode((900,500))
pygame.display.set_caption("The Bishal Game")
pygame.display.update()

bgimg=pygame.image.load("forest.jpg")
bgimg=pygame.transform.scale(bgimg,(900,500)).convert_alpha()
bgimg2=pygame.image.load("wl.jpg")
bgimg2=pygame.transform.scale(bgimg2,(900,500)).convert_alpha()
bgimg3=pygame.image.load("go.jpg")
bgimg3=pygame.transform.scale(bgimg3,(900,500)).convert_alpha()




clock=pygame.time.Clock()

font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def welcome():
    exit_game=False
    while not exit_game:
        
        gameWindow.blit(bgimg2,(0,0)) 
        
        
        text_screen("Welcome To Snakes",white,900/4,500/2.5)
        text_screen("Press SpaceBar To Play",white,900/4.5,500/2)
        
        for event in pygame.event.get():
           
           if event.type==pygame.QUIT:
               exit_game=True
           if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()
           
            
                
        pygame.display.update()
        clock.tick(60)



def plot_snake(gameWindow,color,snk_list,snake_size,snake_sizey):
   
    for x,y in snk_list:

        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_sizey])

def gameloop():
   

    #variable
    exit_game=False
    game_over=False
    score=0
    snake_x=45
    snake_y=45
    snake_size=30
    snake_sizey=30
    velocity_x=0
    velocity_y=0
    init_velocity=4
    fps=60
    snk_list=[]
    snk_length=1
  
    with open("highscore.txt","r") as f:
        highscore=f.read()

    food_x=random.randint(25,900/2)
    food_y=random.randint(25,500/2)


    while not exit_game:
        s=time.time()

        local_time=time.ctime(s)


        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(bgimg3,(0,0))  
            text_screen("Game Over ! "+"score : "+str(score)+" Press Enter To Continue",white,900/19,500/2.5)
               
         

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.load('back.mp3')
                        pygame.mixer.music.play()
                        gameloop()

        else:
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
                    #Cheat Code
                    if (event.key==pygame.K_q):
                       score=score+50  

                    if (event.key==pygame.K_F12):
                        score=score-20 

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            
            if abs(snake_x-food_x)<12 and (snake_y-food_y)<12 and (food_x-snake_x)<12 and (food_y-snake_y)<12:
                score=(score+10)
               
               
                food_x=random.randint(0,750)
                food_y=random.randint(0,350)
                snk_length=snk_length+5
                

                if score>int(highscore):
                    highscore=score
                
                
                

                

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("score : "+str(score)+" Highscore :"+str(highscore),col,400,20)
            text_screen(local_time,col,10,450)
        # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_sizey])
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_sizey])
            

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            

            if len(snk_list) > snk_length:
                del snk_list[0]
            

            if head in snk_list[:-1]:
                game_over=True
                gameWindow.blit(bgimg3,(0,0)) 
                pygame.mixer.music.load('exp.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x >900 or snake_y<0 or snake_y >500:
                game_over=True
                print("Game Over")
                
                
                pygame.mixer.music.load('exp.mp3')
                pygame.mixer.music.play()
                

            plot_snake(gameWindow,black,snk_list,snake_size,snake_sizey)

        pygame.display.update()
        clock.tick(fps)
    
    pygame.quit()
    quit()

welcome()