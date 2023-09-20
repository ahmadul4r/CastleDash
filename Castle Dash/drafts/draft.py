#Modules
import pygame
import time
import random
import os
import webbrowser


pygame.init()
clock = pygame.time.Clock()



#Window config
display_width = 800
display_height = 500
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Castle Dash") #This sets the title of the window
pygame.display.set_icon(pygame.image.load(os.path.join('Sprites', 'systemicon.png')))


#These are the images that will be imported in the game:

#Left/Right movement sprites for player
walkRight = [pygame.image.load(os.path.join('Sprites', 'R1.png')), pygame.image.load(os.path.join('Sprites', 'R2.png')), pygame.image.load(os.path.join('Sprites', 'R3.png')), pygame.image.load(os.path.join('Sprites', 'R4.png')), pygame.image.load(os.path.join('Sprites', 'R5.png')), pygame.image.load(os.path.join('Sprites', 'R6.png')), pygame.image.load(os.path.join('Sprites', 'R7.png')), pygame.image.load(os.path.join('Sprites', 'R8.png'))]
walkLeft = [pygame.image.load(os.path.join('Sprites', 'L1.png')), pygame.image.load(os.path.join('Sprites', 'L2.png')), pygame.image.load(os.path.join('Sprites', 'L3.png')), pygame.image.load(os.path.join('Sprites', 'L4.png')), pygame.image.load(os.path.join('Sprites', 'L5.png')), pygame.image.load(os.path.join('Sprites', 'L6.png')), pygame.image.load(os.path.join('Sprites', 'L7.png')), pygame.image.load(os.path.join('Sprites', 'L8.png'))]
char = pygame.image.load(os.path.join('Sprites', 'R1.png'))


#Sword sprite and powerups
swords1 = pygame.image.load(os.path.join('Sprites', 'sword.png'))
dspeed = pygame.image.load(os.path.join('Sprites', 'dspeed.png'))

#powerup_images 
speed = pygame.image.load(os.path.join('Sprites', 'dspeed.png'))
jump = pygame.image.load(os.path.join('Sprites', 'djump.png'))
test = pygame.image.load(os.path.join('Sprites', 'test.png'))

#Background images
bg = pygame.image.load(os.path.join('Backgrounds', 'bg.png'))
background = pygame.image.load(os.path.join('Backgrounds', 'background.jpg'))
aboutmenu = pygame.image.load(os.path.join('Backgrounds', 'aboutmenu.png'))
castleDash = pygame.image.load(os.path.join('Backgrounds', 'title.png'))
pausebg = pygame.image.load(os.path.join('Backgrounds', 'pause5.png'))
endBackground = pygame.image.load(os.path.join('Backgrounds', 'endbg.png')) 

#Button images
playButton = pygame.image.load(os.path.join('Buttons', 'play.png'))
aboutButton = pygame.image.load(os.path.join('Buttons', 'about.png'))
quitButton = pygame.image.load(os.path.join('Buttons', 'quit.png'))
playButton2 = pygame.image.load(os.path.join('Buttons', 'play2.png'))
aboutButton2 = pygame.image.load(os.path.join('Buttons', 'about2.png'))
quitButton2 = pygame.image.load(os.path.join('Buttons', 'quit2.png'))
continueButton = pygame.image.load(os.path.join('Buttons', 'continue.png'))
continueButton2 = pygame.image.load(os.path.join('Buttons', 'continue2.png'))
menuButton = pygame.image.load(os.path.join('Buttons', 'mainmenu.png'))
menuButton2 = pygame.image.load(os.path.join('Buttons', 'mainmenu2.png'))
pQuit = pygame.image.load(os.path.join('Buttons', 'quitpause.png'))
pQuit2 = pygame.image.load(os.path.join('Buttons', 'quitpause2.png'))
feedback = pygame.image.load(os.path.join('Buttons', 'feedback1.png'))
feedback2 = pygame.image.load(os.path.join('Buttons', 'feedback2.png'))
mute = pygame.image.load(os.path.join('Sprites', 'sound1.png'))
mute2 = pygame.image.load(os.path.join('Sprites', 'sound2.png'))
previous = pygame.image.load(os.path.join('Buttons', 'previousV.png'))
previous2 = pygame.image.load(os.path.join('Buttons', 'previousV2.png'))

powerups = pygame.sprite.Group()



#Defining colours
white = (255,255,255) 



#Variables for Motion/Animation/Size/colours
class player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.isJump = False
        self.jumpcount = 7
        self.left = False
        self.right =- False
        self.walkcount = 0
        
    def draw(self,win):
        if self.walkcount + 1 >= 18:
          self.walkcount = 0

        if self.left:
            win.blit(walkLeft[self.walkcount//3], (self.x,self.y))
            self.walkcount += 1
        elif self.right:
            win.blit(walkRight[self.walkcount//3], (self.x,self.y))
            self.walkcount += 1
        else:
            win.blit(char, (self.x,self.y))







#class sword(object):    
    #def __init__(self, x, y, width, height):
        #self.x = x
        #self.y = y
        #self.width = width
        #self.height = height
        #self.hitbox = (x,y,width,height)
        #self.count = 0

    #def draw(self, win):
        #self.hitbox = (self.x + 5, self.y +5, self.width - 10, self.height)

        #if self.count >= 8:
            #self.count = 0
        
        #win.blit(swords1[self.count//2], (self.x,self.y))
       # self.count += 1
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)






            




#Start Screen
def game_intro():
    win.blit(background, (0,0))

    intro = True
    
    while intro:

        for event in pygame.event.get():  #This allows the user to exit the window via the 'x' from the top right corner 
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()            



        win.blit(background, (0,0))
        win.blit(castleDash, (465,5))


        mouse = pygame.mouse.get_pos()     #This is used to get the postioning of the cursor
        click = pygame.mouse.get_pressed() #This is used to indentify when the left mouse button has been clicked


        
        #Play Button
        if 700+103 > mouse[0] > 700 and 67+55 > mouse[1] > 67: #This is the area of the button 
            win.blit(playButton2, (700,67,103,55))             #Button is highlighted when in this area
            if click[0] == 1:                                  #When clicked the game_intro function stops and the actual game loop starts  
                intro = False
                
        else:
            win.blit(playButton, (700,67,103,55)) #This is the default image of the button




        #About Button
        if 700+103 > mouse[0] > 700 and 117+55 > mouse[1] > 117:
            win.blit(aboutButton2, (700,117,103,55)) 
            while click[0] == 1:                
                win.blit(aboutmenu, (0,0))               
                pygame.display.update()               
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            return game_intro()    #This should display the aboutmenu procedure when clicked


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                
        else:
            win.blit(aboutButton, (700,117,103,55)) 




        #Quit Button
        if 700+103 > mouse[0] > 700 and 167+55 > mouse[1] > 167:
            win.blit(quitButton2, (700,167,103,55)) 
            if click[0] == 1:
                pygame.quit() #This should quit the game when clicked
                quit() 
        else:
            win.blit(quitButton, (700,167,103,55))
            
        
        #Feedback Button
        if 695+100 > mouse[0] > 695 and 454+55 > mouse[1] > 454:
            win.blit(feedback2, (695,454,100,55)) 
            if click[0] == 1:
                url = "https://forms.gle/JmGZC8kPUVRqKM1a7"; #This button will open a page from google with a feedback response sheet
                webbrowser.open(url, True);
        else:
            win.blit(feedback, (695,454,100,55))               
        


        #Previous version button

        if 500+180 > mouse[0] > 500 and 450+55 > mouse[1] > 450:
            win.blit(previous2, (500,450,180,55)) 
            if click[0] == 1:
                url = "https://drive.google.com/file/d/1x43TORUTg9qqDRm0sPgzgCSQXnenrMCe/view?usp=sharing"; #This button will open a page from google with a feedback response sheet
                webbrowser.open(url, True);
        else:
            win.blit(previous, (500,454,180,55))        



        pygame.display.update() #This is needed to update any graphical changes
        clock.tick(15)          #This controls the fps at the moment it has been set to 15



    





#Calls the start screen 
game_intro()




#Pause
def pause():
    paused = True

    while paused:

        win.blit(pausebg, (0,0)) #Displays pause background



        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

        


        mouse = pygame.mouse.get_pos()     #Variable used to locate mouse positions for the button
        click = pygame.mouse.get_pressed() #Variable used to indicate when the mouse button 


        #Quit Button
        if 295+205 > mouse[0] > 295 and 280+71 > mouse[1] > 280: #This is the area of the button 
            win.blit(pQuit2, (295,280,205,71))                   #Highlighted button image            
            if click[0] == 1:                                    #Does the following action when button is pressed
                pygame.quit()
                quit()                 
        else:
            win.blit(pQuit, (295,280,205,71)) #Displays defualt image of button




        #Continue Button
        if 290+205 > mouse[0] > 290 and 210+71 > mouse[1] > 210: #Same for all the buttons in the game
            win.blit(continueButton2, (290,210,205,71))
            if click[0] == 1:
                paused = False
                
        else:
            win.blit(continueButton, (290,210,205,71))

        

        #Main menu button
        #if 280+230 > mouse[0] > 280 and 237+71 > mouse[1] > 237:
            #win.blit(menuButton2, (280,237,230,71))
            #if click[0] == 1:
                #return game_intro()  
                #paused = False
        #else:
            #win.blit(menuButton, (280,235,230,71))


    
        if 10+30 > mouse[0] > 10 and 10+30 > mouse[1] > 10: #Same for all the buttons in the game
            win.blit(mute2, (10,10,30,30))
            if click[0] == 1:
                pygame.mixer.music.stop()
            if click[0] == 2:
                pygame.mixer.music.play()
        else:
            win.blit(mute, (10,10,30,30))


        pygame.display.update()














font = pygame.font.SysFont("Calibri", 65)


   
def endscreen():
    gameover= True

 
    while gameover:
        win.blit(endBackground, (0,0))

        score = str(int((duration*20))) # The score is equivalent to the duration of the gameplay
                                        # The score was multiplied by 20 to make it a larger integer
        
        
        #message_to_screen(score, white)        
        text = font.render(score, True, white)
        win.blit(text, (400,223)) 



        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()



        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()



        #Quit Button
        if 295+205 > mouse[0] > 295 and 290+71 > mouse[1] > 290:
            win.blit(pQuit2, (295,290,205,71))
            if click[0] == 1: 
                pygame.quit()
                quit()                 
        else:
            win.blit(pQuit, (295,290,205,71))


                
        pygame.display.update()


        #Main menu
        #if 280+230 > mouse[0] > 280 and 277+71 > mouse[1] > 277:
            #win.blit(menuButton2, (280,277,230,71))
            #if click[0] == 1:               
                #gameover = False
                #game_intro()  
        #else:
            #win.blit(menuButton, (280,275,230,71))        


         












#Functions which will generate random objects

#class Pow(object):
    #def __init__(self, x, y, width, height):
        #pygame.sprite.Sprite.__init__(self)
        #self.x = x
        #self.y = y
        #self.width = width
        #self.height = height
        #self.vel = 5

    #def draw(self,win):
        #win.blit(speed, (random.randrange(0, display_width), -400))
        #self.y += self.vel

        #if self.y > display_height:
            #self.kill

        #pygame.display.update()
        


#Functions for randomly generated objects
def doubleSpeed(speedx, speedy, speeds, speedw, speedh):
    win.blit(dspeed, [speedx, speedy, speedw, speedh])

def swords(swordsx, swordsy, swordsw, swordsh):
    win.blit(swords1, [swordsx, swordsy, swordsw, swordsh])

def sword(swordx, swordy, swordw, swordh):
    win.blit(swords1, [swordx, swordy, swordw, swordh])

def sword1(sword1x, sword1y, sword1w, sword1h):
    win.blit(swords1, [sword1x, sword1y, sword1w, sword1h])





#Character animation with sprites
def redwrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)    
    #power.draw(win)
    pygame.display.update()
    



#Variables for the parameters of the randomly generated objects
swords_startx = random.randrange(0, display_width)
swords_starty = -1000 #I can change the delay by which the swords start to fall by changing the number 
swords_speed = 18
swords_width = 80
swords_height = 80

sword_startx = random.randrange(0, display_width)
sword_starty = -850   #I can change the delay by which the swords start to fall by changing the number 
sword_speed = 18
sword_width = 80
sword_height = 80

sword1_startx = random.randrange(0, display_width)
sword1_starty = -700  #I can change the delay by which the swords start to fall by changing the number 
sword1_speed = 18
sword1_width = 80
sword1_height = 80

ds_startx = random.randrange(0, display_width)
ds_starty = -400
ds_speed = 18
ds_width = 60
ds_height = 60



#Main loop for game
man = player(300, 357, 64, 64)
run = True
#swordd = sword(300, 357, 64, 64)
start_time = time.time()
#power = Pow(random.randrange(0, display_width), -400, 70, 70)



#Sounds import 
deathSound = pygame.mixer.Sound(os.path.join('Music', 'dead.wav'))
jumpSound = pygame.mixer.Sound(os.path.join('Music', 'jumps.wav'))
noise = pygame.mixer.Sound(os.path.join('Music', 'noise.wav'))


#Background Music
music = pygame.mixer.music.load(os.path.join('Music', 'music1.mp3'))
pygame.mixer.music.play(-1)



clock.tick(25)



while run:
        
        
    #Double speed
    #doubleSpeed(ds_startx, ds_starty, ds_speed, ds_width, ds_height)
    #ds_starty += ds_speed


    #if ds_starty > display_height:
        #ds_starty = 0 - ds_height
        #ds_startx = random.randrange(0, display_width)


    #if man.y < ds_startx + ds_height: # Use to check if the hitboxes are crossing over in the y axis        

        #if man.x > ds_startx and man.x < ds_startx + ds_width or man.width > ds_startx and man.x + man.width < ds_startx + ds_width:            
            #man.vel = man.vel + 2
            #if ds_starty > display_height:
                #ds_starty = 1000
                #ds_startx = 1000
                





    #Sword 1
    swords(swords_startx, swords_starty, swords_width, swords_height)
    swords_starty += swords_speed
    
   
    if swords_starty > display_height: #When the sword goes of the screen the sword will start from the beginning
        swords_starty = 0 - swords_height
        swords_startx = random.randrange(0, display_width)
            

    #Hitbox checking
    if man.y < swords_starty + swords_height - 75: # Use to check if the hitboxes are crossing over in the y axis        

        if man.x > swords_startx and man.x < swords_startx + swords_width or man.width > swords_startx and man.x + man.width < swords_startx + swords_width:            
            pygame.mixer.music.stop() #Stops music
            end_time = time.time() #Ends score timer
            duration = end_time - start_time  #Calculates duration the player is alive for
            pygame.mixer.music.stop() #Stops music
            deathSound.play() #Plays sound effect for death
            run = False
            endscreen()
            



    
    #sword 2
    sword(sword_startx, sword_starty, sword_width, sword_height)
    sword_starty += sword_speed    

    if sword_starty > display_height:
        sword_starty = 0 - sword_height
        sword_startx = random.randrange(0, display_width)

    #Hitbox checking
    if man.y < sword_starty + sword_height - 75: # Use to check if the hitboxes are crossing over in the y axis

        if man.x > sword_startx and man.x < sword_startx + sword_width or man.width > sword_startx and man.x + man.width < sword_startx + sword_width:            
            end_time = time.time()
            duration = end_time - start_time
            pygame.mixer.music.stop()
            deathSound.play()
            run = False
            endscreen()






    #sword 3
    sword1(sword1_startx, sword1_starty, sword1_width, sword1_height)
    sword1_starty += sword1_speed
          
    if sword1_starty > display_height:
        sword1_starty = 0 - sword1_height
        sword1_startx = random.randrange(0, display_width)    

    #Hitbox checking
    if man.y < sword1_starty + sword1_height - 75:   

        if man.x > sword1_startx and man.x < sword1_startx + sword1_width or man.width > sword1_startx and man.x + man.width < sword1_startx + sword1_width:                     
            end_time = time.time()            
            duration = end_time - start_time
            pygame.mixer.music.stop()
            deathSound.play()
            run = False
            endscreen()
    

    


    pygame.display.update()
    clock.tick(30)
    


    


    #Allows user to close the window from top right corner
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    
    

    #Keybinds
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and man.x > man.vel:
      man.x -= man.vel
      man.left = True
      man.right = False
    elif keys[pygame.K_RIGHT] and man.x < display_width - man.width - man.vel:
      man.x += man.vel
      man.right = True
      man.left = False
    elif keys[pygame.K_p]:
        pause()
   
    else:
      man.right = False
      man.left = False
      man.walkcount = 0
    


    if not(man.isJump):  
      if keys[pygame.K_SPACE]:
        jumpSound.play()
        man.isJump = True
        man.right = True
        man.left = False
        man.walkcount = 0


    #Jump mechanics
    else:
      if man.jumpcount >= -7:
        neg = 1
        if man.jumpcount < 0:          
          neg = -1
        man.y -= (man.jumpcount ** 1) * 0.5 * neg
        man.jumpcount -= 1
        

      else:
        man.isJump = False
        man.jumpcount = 7
        
    

    redwrawGameWindow()
    

pygame.quit()
    
    
