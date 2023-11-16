import pygame
import random


def rotated(rotated_bird,bird_drop):
    bird_flappy = pygame.transform.rotozoom(rotated_bird, -bird_drop*6,1)
    return bird_flappy

def hit_tube(time):
    hit_sound = pygame.mixer.Sound('sfx_hit.wav')
    if time > 10:    
        hit_sound.stop()
        time = 0
        return False
    else:
        hit_sound.set_volume(0.4)
        hit_sound.play()

def hit_ground(time):
    die_sound = pygame.mixer.Sound('sfx_die.wav')
    if time > 10:    
        die_sound.stop()
        time = 0
        return False
    else:
        die_sound.set_volume(0.4)
        die_sound.play()

def flappybird(tubeSpeed,betweenX,betweenY,birdDropSpeed,upSpeed,gravity,baseSpeed,hard_lv,aiSmart,aiDodgeUp,aiDodgeDownn,dodge1,dodge2):
    
    #screen
    screen_max_x = 400
    screen_max_y = 600
    pygame.mixer.pre_init()
    pygame.init()
    screen = pygame.display.set_mode((screen_max_x,screen_max_y))
    clock = pygame.time.Clock()
    running = True


        



    #color
    color=(0,255,128)
    green=(0,200,0)
    red=(255,51,51)
    blue=(0,0,204)
    pink=(204,0,204)
    yellow=(255,255,0)
    black=(0,0,0)



    #tube
    TUBE_SPEED = tubeSpeed
    TUBE_WIDTH = 50
    BETWEEN_X = betweenX
    BETWEEN_Y = betweenY
    MIN_X = 100
    MAX_X = 300
    PIPE_HEIGHT = 400
    pass1 = 0
    pass2 = 0
    pass3 = 0
    pass4 = 0

    tube1_x = 400
    tube1_height = random.uniform(MIN_X,MAX_X)
    tubetren_y1 = -(PIPE_HEIGHT - tube1_height)


    tube2_x = tube1_x + BETWEEN_X + TUBE_WIDTH
    tube2_height = random.uniform (MIN_X,MAX_X)
    tubetren_y2 = -(PIPE_HEIGHT - tube2_height)


    tube3_x = tube2_x + BETWEEN_X + TUBE_WIDTH
    tube3_height = random.uniform (MIN_X,MAX_X)
    tubetren_y3 = -(PIPE_HEIGHT - tube3_height)


    tube4_x = tube3_x + BETWEEN_X + TUBE_WIDTH
    tube4_height = random.uniform (MIN_X,MAX_X)
    tubetren_y4 = -(PIPE_HEIGHT - tube4_height)


    #bird
    a=50
    b=300
    c=20
    d=20
    #brid speed
    bird_drop_speed = birdDropSpeed
    UP_SPEED = bird_drop_speed + upSpeed
    GRAVITY = gravity

    #base
    base1_x = 0
    base2_x = 400
    base_y = 570
    BASE_SPEED = baseSpeed

    #AI
    AI_SMART = aiSmart
    AI_DODGEUP = aiDodgeUp
    AI_DODGEDOWN = aiDodgeDownn
    DODGE1 = dodge1
    DODGE2 = dodge2
    AI_OnOff = 1

    #count point
    point = 0   
    font = pygame.font.SysFont('comicsans',20)
    font1 = pygame.font.SysFont('comicsans',50)

    #picture
    bg_img = pygame.image.load('bg21.jpg')
    birdu_img = pygame.image.load('bird3.png')
    bird_img = pygame.image.load('bird1.png')
    birdd_img = pygame.image.load('bird2.png')
    base_img = pygame.image.load('base1.png')
    pipetren_img = pygame.image.load('pipetren.png')
    pipeduoi_img = pygame.image.load('pipeduoi.png')
    victory_img = pygame.image.load('victory.jpeg')
    # mouse_img = pygame.image.load('mouse1.png')
    
    jump_sound = pygame.mixer.Sound('sfx_wing.wav')
    drop_sound = pygame.mixer.Sound('sfx_swooshing.wav')
    die_sound = pygame.mixer.Sound('sfx_die.wav')
    hit_sound = pygame.mixer.Sound('sfx_hit.wav')
    point_sound = pygame.mixer.Sound('sfx_point.wav')
    
    time_play = 0
    ############## ############## ############## ############## 
    ##############  MODE
    ############## ############## ############## ############## 
    # hard
    hard = 4
    HARD_LV = hard_lv
    tubetren_value = 0.4
    tubeduoi_value = 0.2
    # pause
    pause = 0
    
    # bird animation
    count_bird = 0

##################################################
    while running:
        clock.tick(60)
        screen.fill(color)
        screen.blit(bg_img,(0,0))
        


    #stop
        if pause == 0 :
            TUBE_SPEED = 0
            BASE_SPEED = 0.5
            bird_drop_speed = 0
            welcome_txt = font1.render(" FLAPPY BIRD  ",True,pink)
            screen.blit(welcome_txt,(30,180))    
            author_txt = font.render("By SE173657 ",True,black)
            screen.blit(author_txt,(130,260))   
            bird_rect = screen.blit(bird_img,(a,b))




    #math
        tubeduoi_y1 = tube1_height + BETWEEN_Y
        tubeduoi_y2 = tube2_height + BETWEEN_Y
        tubeduoi_y3 = tube3_height + BETWEEN_Y
        tubeduoi_y4 = tube4_height + BETWEEN_Y
        '''
        tubeduoi_y2 = tube2_height + BETWEEN_Y - tubetren_y2 
        tubeduoi_y3 = tube3_height + BETWEEN_Y - tubetren_y3
        tubeduoi_y4 = tube4_height + BETWEEN_Y - tubetren_y4
        '''
        '''
        tube1d_height = 600 - tubeduoi_y1
        tube2d_height = 600 - tubeduoi_y2
        tube3d_height = 600 - tubeduoi_y3
        tube4d_height = 600 - tubeduoi_y4
        '''
        
    #pipe pic

        tube1tren_rect = screen.blit(pipetren_img,(tube1_x,tubetren_y1))
        pygame.draw.rect(screen,yellow,(tube1_x - 10,10,10,10))
        tube2tren_rect = screen.blit(pipetren_img,(tube2_x,tubetren_y2))
        pygame.draw.rect(screen,red,(tube2_x - 10,10,10,10))
        tube3tren_rect = screen.blit(pipetren_img,(tube3_x,tubetren_y3))
        pygame.draw.rect(screen,green,(tube3_x - 10,10,10,10))
        tube4tren_rect = screen.blit(pipetren_img,(tube4_x,tubetren_y4)) 
        pygame.draw.rect(screen,black,(tube4_x - 10,10,10,10)) 
        #tube1tren_rect = pygame.draw.rect(screen,red,(tube1_x,tubetren_y,TUBE_WIDTH,tube1_height))
        #tube2tren_rect = pygame.draw.rect(screen,blue,(tube2_x,tubetren_y,TUBE_WIDTH,tube2_height))
        #tube3tren_rect = pygame.draw.rect(screen,green,(tube3_x,tubetren_y,TUBE_WIDTH,tube3_height))
        #tube4tren_rect = pygame.draw.rect(screen,yellow,(tube4_x,tubetren_y,TUBE_WIDTH,tube4_height))
        
        
        tube1duoi_rect = screen.blit(pipeduoi_img,(tube1_x,tubeduoi_y1))
        tube2duoi_rect = screen.blit(pipeduoi_img,(tube2_x,tubeduoi_y2))
        tube3duoi_rect = screen.blit(pipeduoi_img,(tube3_x,tubeduoi_y3))
        tube4duoi_rect = screen.blit(pipeduoi_img,(tube4_x,tubeduoi_y4))
        
        #tube1duoi_rect = pygame.draw.rect(screen,red,(tube1_x,tubeduoi_y1,TUBE_WIDTH,tube1d_height))
        #tube2duoi_rect = pygame.draw.rect(screen,blue,(tube2_x,tubeduoi_y2,TUBE_WIDTH,tube2d_height))
        #tube3duoi_rect = pygame.draw.rect(screen,green,(tube3_x,tubeduoi_y3,TUBE_WIDTH,tube3d_height))
        #tube4duoi_rect = pygame.draw.rect(screen,yellow,(tube4_x,tubeduoi_y4,TUBE_WIDTH,tube4d_height))





    ### draw base move
        base1_rect = screen.blit(base_img,(base1_x,base_y))
        base2_rect = screen.blit(base_img,(base2_x,base_y))
        base1_x -= BASE_SPEED
        base2_x -= BASE_SPEED
        if base1_x < -400 :
            base1_x = base2_x + 400
        if base2_x < -400 :
            base2_x = base1_x + 400
    
    
    
    
        
    ### bird animations
        if TUBE_SPEED == 0:
            count_bird = 0
        elif TUBE_SPEED != 0:
            count_bird += 1
            
        if count_bird == 0:
            screen.blit(bird_img,(a,b))
        elif count_bird <= 15:
            rotate_bird = rotated(bird_img,bird_drop_speed)
            bird_rect = screen.blit(rotate_bird,(a,b))
        elif count_bird <= 30:
            rotate_bird = rotated(birdd_img,bird_drop_speed)
            bird_rect = screen.blit(rotate_bird,(a,b))
        elif count_bird <= 45:
            rotate_bird = rotated(birdu_img,bird_drop_speed)
            bird_rect = screen.blit(rotate_bird,(a,b))
        elif count_bird <= 46:
            rotate_bird = rotated(birdd_img,bird_drop_speed)
            bird_rect = screen.blit(rotate_bird,(a,b))
            count_bird = 1


            

        
    #draw bird
        b = b + bird_drop_speed
        bird_drop_speed += GRAVITY
        GRAVITY =+ 0.1


                  
           
            
    # move to left to right
        tube1_x = tube1_x - TUBE_SPEED
        tube2_x = tube2_x - TUBE_SPEED
        tube3_x = tube3_x - TUBE_SPEED
        tube4_x = tube4_x - TUBE_SPEED
        
        
    ## move up down tube  
        if TUBE_SPEED != 0 :   
            if tube1_height == tube2_height == tube3_height == tube4_height:
                tube1_height = tube1_height - tubetren_value
                tubetren_y1 = tubetren_y1 - tubeduoi_value
                tube2_height = tube2_height - tubetren_value
                tubetren_y2 = tubetren_y2 - tubeduoi_value
                tube3_height = tube3_height - tubetren_value
                tubetren_y3 = tubetren_y3 - tubeduoi_value
                tube4_height = tube4_height - tubetren_value 
                tubetren_y4 = tubetren_y4 - tubeduoi_value 
                tubetren_value += 0.0005
                tubeduoi_value += 0.0005


            elif pass1 == 3 and pass3 != 3:
                tube1_height = tube1_height + tubeduoi_value
                tubetren_y1 = tubetren_y1 + tubetren_value
                tube2_height = tube2_height - tubetren_value
                tubetren_y2 = tubetren_y2 - tubeduoi_value
                tube3_height = tube3_height + tubeduoi_value
                tubetren_y3 = tubetren_y3 + tubetren_value
                tube4_height = tube4_height - tubetren_value 
                tubetren_y4 = tubetren_y4 - tubeduoi_value    
                tubetren_value += 0.000025
                tubeduoi_value += 0.000025

                
            elif pass1 == 7 and pass3 != 7:
                tube1_height = tube1_height - tubetren_value
                tubetren_y1 = tubetren_y1 - tubeduoi_value
                tube2_height = tube2_height - tubetren_value
                tubetren_y2 = tubetren_y2 - tubeduoi_value
                tube3_height = tube3_height - tubetren_value
                tubetren_y3 = tubetren_y3 - tubeduoi_value
                tube4_height = tube4_height - tubetren_value 
                tubetren_y4 = tubetren_y4 - tubeduoi_value 
                tubetren_value += 0.000025
                tubeduoi_value += 0.000025


            elif pass1 == 11 and pass3 != 11:
                tube1_height = tube1_height + tubeduoi_value
                tubetren_y1 = tubetren_y1 + tubetren_value
                tube2_height = tube2_height - tubetren_value
                tubetren_y2 = tubetren_y2 - tubeduoi_value
                tube3_height = tube3_height + tubeduoi_value
                tubetren_y3 = tubetren_y3 + tubetren_value
                tube4_height = tube4_height - tubetren_value 
                tubetren_y4 = tubetren_y4 - tubeduoi_value    
                tubetren_value += 0.000025
                tubeduoi_value += 0.000025


            elif pass1 == 15 and pass3 != 15:
                tube1_height = tube1_height - tubetren_value
                tubetren_y1 = tubetren_y1 - tubeduoi_value
                tube2_height = tube2_height - tubetren_value
                tubetren_y2 = tubetren_y2 - tubeduoi_value
                tube3_height = tube3_height - tubetren_value
                tubetren_y3 = tubetren_y3 - tubeduoi_value
                tube4_height = tube4_height - tubetren_value 
                tubetren_y4 = tubetren_y4 - tubeduoi_value 
                tubetren_value += 0.000025
                tubeduoi_value += 0.000025

                            
            elif pass1 == 19 and pass3 != 19:
                tube1_height = tube1_height + tubeduoi_value
                tubetren_y1 = tubetren_y1 + tubetren_value
                tube2_height = tube2_height - tubetren_value
                tubetren_y2 = tubetren_y2 - tubeduoi_value
                tube3_height = tube3_height + tubeduoi_value
                tubetren_y3 = tubetren_y3 + tubetren_value
                tube4_height = tube4_height - tubetren_value 
                tubetren_y4 = tubetren_y4 - tubeduoi_value    
                tubetren_value += 0.000025
                tubeduoi_value += 0.000025

                
            elif pass1 == 23 and pass3 != 23:
                tube1_height = tube1_height - tubetren_value
                tubetren_y1 = tubetren_y1 - tubeduoi_value
                tube2_height = tube2_height - tubetren_value
                tubetren_y2 = tubetren_y2 - tubeduoi_value
                tube3_height = tube3_height - tubetren_value
                tubetren_y3 = tubetren_y3 - tubeduoi_value
                tube4_height = tube4_height - tubetren_value 
                tubetren_y4 = tubetren_y4 - tubeduoi_value 
                tubetren_value += 0.000025
                tubeduoi_value += 0.000025



    #create new tube --- harder
        if tube1_x + TUBE_WIDTH + 40 <a :
            point_sound.play()
            point +=1
            if pass4 % 4 == 0:
                tube1_x = tube4_x + BETWEEN_X + TUBE_WIDTH + 50
                tube1_height = random.uniform(MIN_X,MAX_X)
                tubetren_y1 = -(PIPE_HEIGHT - tube1_height)  
                pass1 += 1
                print("Pass tube 1, Time: ",pass1)            
            elif pass4 % 4 > 0 :
                tube1_x = tube4_x + BETWEEN_X + TUBE_WIDTH
                tube1_height = random.uniform(MIN_X,MAX_X)
                tubetren_y1 = -(PIPE_HEIGHT - tube1_height)
                pass1 += 1
                print("Pass tube 1, Time: ",pass1)            
                
        if tube2_x + TUBE_WIDTH + 40 <a:
            point_sound.play()
            point +=1
            if pass4 % 4 == 0:
                tube2_x = tube1_x + TUBE_WIDTH 
                tube2_height = tube1_height
                tubetren_y2 = -(PIPE_HEIGHT - tube2_height)
                pass2 += 1
                print("Pass tube 2, Time: ",pass2)
            elif pass4 % 4 > 0 :
                tube2_x = tube1_x + BETWEEN_X + TUBE_WIDTH 
                tube2_height = random.uniform(MIN_X,MAX_X)
                tubetren_y2 = -(PIPE_HEIGHT - tube2_height)
                pass2 += 1
                print("Pass tube 2, Time: ",pass2)

        if tube3_x + TUBE_WIDTH + 40 <a:
            point_sound.play()
            point +=1
            if pass4 % 4 == 0:
                tube3_x = tube2_x + TUBE_WIDTH  
                tube3_height = tube1_height
                tubetren_y3 = -(PIPE_HEIGHT - tube3_height)
                pass3 += 1
                print("Pass tube 3, Time: ",pass3)
            elif pass4 % 4 > 0 :
                tube3_x = tube2_x + BETWEEN_X + TUBE_WIDTH  
                tube3_height = random.uniform (MIN_X,MAX_X)
                tubetren_y3 = -(PIPE_HEIGHT - tube3_height)
                pass3 += 1
                print("Pass tube 3, Time: ",pass3)
            
        if tube4_x + TUBE_WIDTH + 40 <a:
            point_sound.play()
            point += 1
            if pass4 % 4 == 0:
                tube4_x = tube3_x + TUBE_WIDTH  
                tube4_height = tube1_height
                tubetren_y4 = -(PIPE_HEIGHT - tube4_height) 
                pass4 += 1
                print("Pass tube 4, Time: ",pass4) 
            elif pass4 % 4 > 0 :
                tube4_x = tube3_x + BETWEEN_X + TUBE_WIDTH  
                tube4_height = random.uniform (MIN_X,MAX_X)
                tubetren_y4 = -(PIPE_HEIGHT - tube4_height) 
                pass4 += 1
                print("Pass tube 4, Time: ",pass4)





    #print point
        if TUBE_SPEED != 0:
            point_txt = font.render("Point: " + str(point),True,black)
            screen.blit(point_txt,(5,5))



################################
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # mouse_rect = pygame.draw.rect(screen,blue,(mouse_x,mouse_y,10,10))

        #mouse_rect = screen.blit(mouse_img,(mouse))  
################################
        # for tube in [tube1tren_rect,tube2tren_rect,tube3tren_rect,tube4tren_rect,
        #             tube1duoi_rect,tube2duoi_rect,tube3duoi_rect,tube4duoi_rect]:           
        #     # if mouse_rect.colliderect(tube):
        #     #     # hit_sound.play()
        #     #     TUBE_SPEED = 0
        #     #     bird_drop_speed = 0
        #     #     BASE_SPEED = 0
        #     #     hard = 2
            #     gameover_txt = font1.render("Game Over",True,black)
            #     screen.blit(gameover_txt,(80,210))    
            #     gameover_txt = font1.render("mouseHit the tube",True,green)
            #     screen.blit(gameover_txt,(70,100)) 
            #     point_txt = font.render("Final Point: " + str(point),True,black)
            #     screen.blit(point_txt,(140,280))  


        
    #check bird and tube
        for tube in [tube1tren_rect,tube2tren_rect,tube3tren_rect,tube4tren_rect,
                    tube1duoi_rect,tube2duoi_rect,tube3duoi_rect,tube4duoi_rect]:
            if bird_rect.colliderect(tube):
                # hit_sound.play()
                TUBE_SPEED = 0
                bird_drop_speed = 0
                BASE_SPEED = 0
                hard = 2
                gameover_txt = font1.render("Game Over",True,black)
                screen.blit(gameover_txt,(80,210))    
                gameover_txt = font1.render("Hit the tube",True,green)
                screen.blit(gameover_txt,(70,100)) 
                point_txt = font.render("Final Point: " + str(point),True,black)
                screen.blit(point_txt,(140,280))  
                time_play += 1       
                hit_tube(time_play)


    #check bird hit the ground 
        if  b >= 560:
            TUBE_SPEED = 0
            bird_drop_speed = 0
            BASE_SPEED = 0
            hard = 2
            gameover_txt = font1.render("Game Over",True,black)
            screen.blit(gameover_txt,(80,210))    
            hit_the_ground_txt = font1.render("Hit the base",True,green)
            screen.blit(hit_the_ground_txt,(70,100)) 
            point_txt = font.render("Final Point: " + str(point),True,black)
            screen.blit(point_txt,(140,280)) 
            time_play += 1
            hit_ground(time_play)
             
        if b <= 0:        
            TUBE_SPEED = 0
            bird_drop_speed = 0
            BASE_SPEED = 0
            hard = 2
            gameover_txt = font1.render("Game Over",True,black)
            screen.blit(gameover_txt,(80,210))    
            hit_the_top_txt = font1.render("Hit the top",True,green)
            screen.blit(hit_the_top_txt,(70,100)) 
            point_txt = font.render("Final Point: " + str(point),True,black)
            screen.blit(point_txt,(140,280)) 
            time_play += 1
            hit_ground(time_play)
                 
                 
                 
                        

    ### AI ###
        if AI_OnOff % 2 == 0 and TUBE_SPEED != 0 :
            
            if tube1_x - a < AI_SMART:
                if tube2_height >= tube1_height :
                    if b - tube1_height < AI_DODGEDOWN + DODGE1:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed + UP_SPEED
                    elif tubeduoi_y1 - b < AI_DODGEUP - DODGE2:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed - UP_SPEED
                elif tube2_height < tube1_height :
                    if b - tube1_height < AI_DODGEDOWN - DODGE2:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed + UP_SPEED
                    elif tubeduoi_y1 - b < AI_DODGEUP + DODGE1:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed - UP_SPEED                  
                               
            elif tube2_x - a < AI_SMART:
                if tube3_height >= tube2_height :
                    if b - tube2_height < AI_DODGEDOWN + DODGE1:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed + UP_SPEED
                    elif tubeduoi_y2 - b < AI_DODGEUP - DODGE2:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed - UP_SPEED
                elif tube3_height < tube2_height :
                    if b - tube2_height < AI_DODGEDOWN - DODGE2:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed + UP_SPEED
                    elif tubeduoi_y2 - b < AI_DODGEUP + DODGE1:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed - UP_SPEED          
            
            elif tube3_x - a < AI_SMART:
                if tube4_height >= tube3_height :
                    if b - tube3_height < AI_DODGEDOWN + DODGE1:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed + UP_SPEED
                    elif tubeduoi_y3 - b < AI_DODGEUP - DODGE2:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed - UP_SPEED
                elif tube4_height < tube3_height :
                    if b - tube3_height < AI_DODGEDOWN - DODGE2:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed + UP_SPEED
                    elif tubeduoi_y3 - b < AI_DODGEUP + DODGE1:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed - UP_SPEED
                                          
            elif tube4_x - a < AI_SMART:
                if tube1_height >= tube4_height :
                    if b - tube4_height < AI_DODGEDOWN + DODGE1:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed + UP_SPEED
                    elif tubeduoi_y4 - b < AI_DODGEUP - DODGE2:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed - UP_SPEED
                elif tube1_height < tube4_height :
                    if b - tube4_height < AI_DODGEDOWN - DODGE2:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed + UP_SPEED
                    elif tubeduoi_y4 - b < AI_DODGEUP + DODGE1:
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed - UP_SPEED                      
            
            
            elif b > 520:
                bird_drop_speed = 0
                bird_drop_speed = bird_drop_speed - UP_SPEED


            elif point == 0 and tube1_x - a < AI_SMART + 100:
                if b > 450:
                    bird_drop_speed = 0
                    bird_drop_speed = bird_drop_speed - UP_SPEED 
                elif b < 250:
                    bird_drop_speed = 0
                    bird_drop_speed = bird_drop_speed + UP_SPEED
                




    ### HARD UP
        if TUBE_SPEED != 0:
            if pass1 >= hard:
            #move left to right
                TUBE_SPEED += (0.1 * HARD_LV)
                BETWEEN_X -= (1 * HARD_LV)
                BETWEEN_Y -= (1 * HARD_LV)
                MIN_X -= (2 * HARD_LV)
                MAX_X += (2 * HARD_LV)
            #draw bird
                bird_drop_speed += (0.15 * HARD_LV)
                UP_SPEED += (0.1 * HARD_LV)
                
            # base
                BASE_SPEED += (0.2 * HARD_LV)
                
            # level up min max hard
                print("tube speed: ",TUBE_SPEED)
                print('up speed: ',UP_SPEED)
                print('base speed: ',BASE_SPEED)
                hard += 4





    ### victory
        VICTORY_POINT = 100
        if point == VICTORY_POINT :
            TUBE_SPEED = 0
            bird_drop_speed = 0
            BASE_SPEED = 0
            hard = 2
            win_txt = font.render(" VICTORY ",True,black)
            point_txt = font.render("You get " + str(point) + ' out of ' + str(VICTORY_POINT),True,black)
            screen.blit(victory_img,(0,0))
            screen.blit(win_txt,(140,250))  
            screen.blit(point_txt,(110,280))  
            
            tube1_x = 500
            tube2_x = 500
            tube3_x = 500
            tube4_x = 500
            
            
            
            
            
    #game play                          
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                
                
                if event.key == pygame.K_a:
                    if AI_OnOff % 2 == 0:
                        AI_OnOff += 1
                        print("AI off") 
                    elif AI_OnOff % 2 != 0:
                        AI_OnOff += 1
                        print("AI on")
                        
                        
                elif event.key == pygame.K_SPACE:     
                                
                    if  TUBE_SPEED == 0 and bird_drop_speed == 0 and BASE_SPEED == 0:
                        
                        #point
                        point = 0
                        
                        #pipe
                        TUBE_SPEED = tubeSpeed
                        TUBE_WIDTH = 50
                        BETWEEN_X = betweenX
                        BETWEEN_Y = betweenY
                        MIN_X = 50
                        MAX_X = 400
                        PIPE_HEIGHT = 400
                        pass1 = 0
                        pass2 = 0
                        pass3 = 0
                        pass4 = 0
                        
                        #bird
                        a = 50
                        b = 300
                        
                        #brid speed
                        bird_drop_speed = birdDropSpeed
                        UP_SPEED = bird_drop_speed + upSpeed
                        GRAVITY = gravity

                        #base
                        base1_x = 0
                        base2_x = 400
                        base_y = 570
                        BASE_SPEED = baseSpeed

                        #AI
                        AI_SMART = aiSmart
                        AI_DODGEUP = aiDodgeUp
                        AI_DODGEDOWN = aiDodgeDownn
                        AI_OnOff = 1
                        
                        # time play
                        time_play = 0
                        
                        # hard
                        hard = 4
                        tubetren_value = 0.4
                        tubeduoi_value = 0.2        
                                        
                        #tube
                        tube1_x = 400
                        tube1_height = random.uniform (MIN_X,MAX_X)
                        tubetren_y1 = -(PIPE_HEIGHT - tube1_height)


                        tube2_x = tube1_x + BETWEEN_X + TUBE_WIDTH
                        tube2_height = random.uniform(MIN_X,MAX_X)
                        tubetren_y2 = -(PIPE_HEIGHT - tube2_height)


                        tube3_x = tube2_x + BETWEEN_X + TUBE_WIDTH
                        tube3_height = random.uniform (MIN_X,MAX_X)
                        tubetren_y3 = -(PIPE_HEIGHT - tube3_height) 


                        tube4_x = tube3_x + BETWEEN_X + TUBE_WIDTH
                        tube4_height = random.uniform (MIN_X,MAX_X)
                        tubetren_y4 = -(PIPE_HEIGHT - tube4_height)
                        
                    # check data
                        print('pause + 1',pause)
                        print(" --- NEW GAME DATA --- ")
                        print("TUBE_SPEED",TUBE_SPEED)
                        print("BETWEENX",BETWEEN_X)
                        print("BETWEENY",BETWEEN_Y)
                        print("BIRD DROP",bird_drop_speed)
                        print("UP SPEED",UP_SPEED)
                        print("GRAVITY",GRAVITY)
                        print("BASE SPEED",BASE_SPEED)
                        print("HARD LV",HARD_LV)
                        print("AI SMART",AI_SMART)
                        print("AI UP",AI_DODGEUP)
                        print("AI DOWN",AI_DODGEDOWN)                       
                    
                    elif pause == 0 : 
                            
                        #tube             
                        TUBE_SPEED = tubeSpeed
                        BETWEEN_X = betweenX
                        BETWEEN_Y = betweenY
                        
                        #brid speed
                        bird_drop_speed = birdDropSpeed
                        UP_SPEED = bird_drop_speed + upSpeed
                        GRAVITY = gravity

                        #base
                        
                        BASE_SPEED = baseSpeed

                        #AI
                        AI_SMART = aiSmart
                        AI_DODGEUP = aiDodgeUp
                        AI_DODGEDOWN = aiDodgeDownn
                        
                        #pause
                        pause += 1
                        
                    #check data
                        print('pause + 1',pause)
                        print(" --- STRAT GAME DATA --- ")
                        print("TUBE_SPEED",TUBE_SPEED)
                        print("BETWEENX",BETWEEN_X)
                        print("BETWEENY",BETWEEN_Y)
                        print("BIRD DROP",bird_drop_speed)
                        print("UP SPEED",UP_SPEED)
                        print("GRAVITY",GRAVITY)
                        print("BASE SPEED",BASE_SPEED)
                        print("HARD LV",HARD_LV)
                        print("AI SMART",AI_SMART)
                        print("AI UP",AI_DODGEUP)
                        print("AI DOWN",AI_DODGEDOWN)                            
                    
                    else:
                        jump_sound.play()
                        print('press space')
                        bird_drop_speed = 0
                        bird_drop_speed = bird_drop_speed - UP_SPEED
                        
    
                
                
                
        pygame.display.flip()
    pygame.quit()





   ################################# PLAYER #################################
   
   
   
while True:
    print("----------------------------------------------------------------------------------------------")
    print("--------------------------------- FLAPPY BIRD - DUYPCSE173657 --------------------------------")
    print("----------------------------------------------------------------------------------------------")
    print("1/ Dễ ẹt\n2/ Bình thường thôi\n3/ Khó khó 1 tẹo\n4/ Thắng hộ - bot tôi còn chưa win được - BẠN THÌ THẮNG HỘ <3\n5/ Thoát trò chơi ")
    
    choice = int(input('Nhận độ khó mà bạn muốn " var " chạm: '))
    
    if choice == 1:
        print("Game Mode 'Dễ' - 1")
        flappybird(2,250,200,3,-0.5,0.1,2,2,200,60,40,40,0)
        
        
    elif choice == 2:
        print("Game Mode 'Trung Bình' - 2")
        flappybird(2.1,245,200,4,-0.8,0.3,3,2.7,200,60,40,40,0)
        
        
    elif choice == 3:
        print("Game Mode 'Bình thường' - 3")
        flappybird(2.2,235,190,5,-1.3,0.4,4,3.5,195,50,50,40,-10)
        
        
    elif choice == 4:
        print("Game Mode 'Khó' - 4")
        flappybird(2.5,220,180,6,-2.5,0.6,5,5,190,40,40,30,-10)
        
    
    elif choice == 5:
        print("GAME EXIT")     
        break 


