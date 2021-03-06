# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

# for balloon in Balloon:
# if Balloon.rect.collidepoint(pos):
# pygame.sprite.Sprite.remove
import pygame, sys, random, math
from balloon import Balloon
pygame.init()


BackGround1 = pygame.image.load('tobi.jpg')
BackGround2 = pygame.image.load('settings.jpg')
BackGround3 = pygame.image.load('2_menu_screen.jpg')
BackGround4 = pygame.image.load('in_play.png')
BackGround5 = pygame.image.load('game_screen.jpg')
BackGround6 = pygame.image.load('credits.jpg')
BackGround7 = pygame.image.load('stripedlines.jpg')
BackGround8 = pygame.image.load('jariya.jpg')
                                
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Naruto Shippuden OST 1 - Track 02 - Douten ( Heaven Shaking Event ).mp3')
pygame.mixer.music.play(-1)

music_playing = True
pygame.mixer.music.play()

#https://stackoverflow.com/questions/21947389/how-to-continuously-move-an-image-in-pygame
import pygame, sys
pygame.init()




# Define some colours
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)  
BLACK = (0, 0, 0)
RED = (188, 16, 22)
BLUE = (0, 0, 255)
BRED = (188, 16, 22)
BBRED = (216, 15, 21)
TEA = (208, 240, 192)
# Colour Palette
DARK_BLUE = (12, 44, 82)
GREY = (95, 107, 97)
BABY_BLUE = (94, 157, 200)
WHITE_BLUE = (220, 240, 247)

SCREENWIDTH = 800
SCREENHEIGHT = 710

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)


all_sprites_list = pygame.sprite.Group()

class Button():
    """This is a class for a generic button.
    
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """

    def __init__(self, txt, location, action, bg=BRED, fg=BLACK, size=(120, 50), font_name="Segoe Print", font_size=16):
        """This function defines the text, color, font and placement"""
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action
      
        #pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
        #pygame.mixer.load('Sounds/soundtrack.mps3')
        #pygame.mixer.music.play(-1) THIS IS WHERE THE MUSIC FILE IS

    def draw(self):
        """Global draw function that illustrates text, images, buttons, sprites"""
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = BBRED  # mouseover color


    def mouseBalloondown():
        """This function deals with the collision of the sprite"""
        pos = pygame.mouse.get_pos()
        Hit = False
        for balloon in Balloon:
         if balloon.image.collidepoint(pos):
            Hit = True
            balloon.image.y = (900)
            balloon.image.x = (900) 
            myBalloon = balloon(balloonImage1, 70, 70, 5)


    

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()

def my_shell_function():
    """A generic function that prints something in the shell"""
    print('Fire the nukes!')

def my_settings_function():
    """A function that advances to the next level"""
    global level
    level += 1

def my_playgame_function():
    global level
    """A function that takesm you to the game screen when pressed"""
    level += 2
    print('Game Start')


def my_next_function():
    global level
    """A function that takes the user to the next page/level."""
    level +=1


def my_credits_function():
    global level
    """A function that allows you to view the credits"""
    level += 7    

def my_back_function():
    """A function that retreats to the previous level"""
    global level
    level -= 1

def my_sound_function():
    """A function that allows user to change sound settings"""
    print('')

def my_soundon_function():
    """A function that allows you to turn the sound on"""
    pygame.mixer.music.unpause()
    print('Sound On')


def my_soundoff_function():
    """A function that allows you to turn the sound off"""
    pygame.mixer.music.pause()
    print('Sound Off')


def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def my_instructions_function():
    """a function that allows you to read the intructions"""
    global level
    level += 1

def my_easy_function():
    'takes you to easy level'
    global level
    level += 2

def my_hard_function():
    'takes you to hard level'
    global level
    level += 3

def my_mainmenu_function():
    """A funtion that will return you to the main menu"""
    global level
    level = 1

def my_retry_function():
    """This function is used to reset the player life"""
    global level, Health
    level = 4  
    Health = 100
    
    #reset balloons
    for balloon in all_sprites_list:
        myBalloon1.rect.x = random.randint(-2100,0)
        myBalloon1.rect.y = 355
        myBalloon1.speed = 5

        myBalloon2.rect.x = random.randint(-2100,0)
        myBalloon2.rect.y = 355
        myBalloon2.speed = 5

        myBalloon3.rect.x = random.randint(-2100,0)
        myBalloon3.rect.y = 355
        myBalloon3.speed = 5
#def my_on_function():
    #global music_playing
    #if music_playing == True:
     #   pygame.mixer.music.paus()
    #    music_playing = False

#def my_off_function():
   # global music_playing
   # if music_playing == True:
     #   pygame.mixer.music.pause()


def my_display_function(screen,self):
    """A function that allows sprite to be shown"""
    BackGround5 = Pygame.image.load('grass_template_straightpath.jpg')
   

        
def mousebuttondown(level):
    """A function that checks if a button was pressed tranfering one
        to set level"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 3:
        for button in level3_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 4:
        for button in level4_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 5:
        for button in level5_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 6:
        for button in level6_buttons:
            if button.rect.collidepoint(pos):
                    button.call_back()
    elif level == 7:
        for button in level7_buttons:
            if button.rect.collidepoint(pos):
                    button.call_back()
    elif level == 8:
        for button in level8_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
                
    elif level == 10:
        for button in level10_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

#Stores all sprites into a list
ALL_sprites_lists = pygame.sprite.Group()

#Balloon images
BalloonImage1 = pygame.image.load("blue-balloon-hi.png")
BalloonImage2 = pygame.image.load("new-pink-balloon-hi (1).png")
BalloonImage3 = pygame.image.load("orange-balloon.png")

#Creates five of each ballons, sclaes to size, controls speed,randomly places on level
for i in range(5):
    myBalloon1 = Balloon(BalloonImage1, 70, 70, 8)
    myBalloon1.rect.x = random.randint(-2100,0)
    myBalloon1.rect.y = 355

    myBalloon2 = Balloon(BalloonImage2, 70, 70, 7)
    myBalloon2.rect.x = random.randint(-2100,0)
    myBalloon2.rect.y = 355

    myBalloon3 = Balloon(BalloonImage3, 70, 70, 5)
    myBalloon3.rect.x = random.randint(-2100,0)
    myBalloon3.rect.y = 355
    
    ALL_sprites_lists.add(myBalloon1, myBalloon2, myBalloon3)



#create button objects
button_01 = Button("Settings", (SCREENWIDTH*2/3.3, SCREENHEIGHT*3.5/4), my_settings_function)
button_02 = Button("Back", (SCREENWIDTH/2, SCREENHEIGHT/3), my_back_function)
button_03 = Button("Quit", (SCREENWIDTH/2.7, SCREENHEIGHT*3.5/4), my_quit_function, bg=(50, 200, 20))
button_04 = Button("Play", (SCREENWIDTH/2, SCREENHEIGHT/2), my_playgame_function)
button_05 = Button("Sound", (SCREENWIDTH/2, SCREENHEIGHT/2), my_sound_function)
button_06 = Button("Sound On", (SCREENWIDTH/4, SCREENHEIGHT/2), my_soundon_function)
button_07 = Button("Sound Off", (SCREENWIDTH *3/4, SCREENHEIGHT/2), my_soundoff_function)
button_08 = Button("Next", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_next_function)
button_09 = Button("MainMenu", (SCREENWIDTH/2, SCREENHEIGHT*1/5), my_mainmenu_function)
button_10 = Button("Play!", (SCREENWIDTH/2, SCREENHEIGHT/2), my_instructions_function)
button_11 = Button("Credits", (SCREENWIDTH/2, SCREENHEIGHT*3/4), my_credits_function)
button_12 = Button("Play", (SCREENWIDTH/2 , SCREENHEIGHT*2/5), my_playgame_function)
button_13 = Button("MainMenu", (SCREENWIDTH/2.7, SCREENHEIGHT*2.5/5), my_mainmenu_function) # level 4 main menu
button_14 = Button("Gemu Shimasu", (SCREENWIDTH/1.6 , SCREENHEIGHT*2.5/5), my_playgame_function) #level 4 game start
button_15 = Button("Tutorial", (SCREENWIDTH/2.7, SCREENHEIGHT*2.5/5), my_easy_function) # level 4 main menu
button_16 = Button("Survival!", (SCREENWIDTH/1.7 , SCREENHEIGHT*2.5/5), my_hard_function)
button_18 = Button("Retry", (SCREENWIDTH/2.0 , SCREENHEIGHT*2.5/5), my_retry_function)
#Game title
#for Balloon in ALL_sprites_lists:
   # Balloon.moveRight()
    #Balloon.rect.y > SCREENWIDTH


#screen.blit(BackGround1,(0,0))

#arrange button groups depending on level
level1_buttons = [button_01, button_03 , button_04]
level2_buttons = [button_02, button_05, button_06, button_07]
level3_buttons = [button_09, button_10, button_11]
level4_buttons = [button_15, button_16,]#menu 
level5_buttons = [button_02]#menu
level6_buttons = [button_09]#easy game screen
level7_buttons = [button_09]#hard game screen
level8_buttons = [button_18]
level10_buttons = [button_09]#credits
#credits (level 10)
# level3_buttons = [button_08]
#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close bTEAutton
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            if level <= 10:
                mousebuttondown(level)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if level <= 10:
                mousebuttondown(level)
    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(BLACK)
    

    

    # Draw buttons, background, and text
    if level == 1:
        screen.blit(BackGround1,(0,0))
        for button in level1_buttons:
          button.draw()

        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 64)
        textSurfaceTitle1 = fontTitle.render('Indras!', True, GREY) 
        textRectTitle1 = textSurfaceTitle1.get_rect()

        textRectTitle1.center = (380, 110)

        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 64)
        textSurfaceTitle2 = fontTitle.render('Arrow!', True, GREY) 
        textRectTitle2 = textSurfaceTitle2.get_rect()

        textRectTitle2.center = (380, 160)

        screen.blit(textSurfaceTitle1, textRectTitle1)
        screen.blit(textSurfaceTitle2, textRectTitle2)           
    elif level == 2:   
        screen.blit(BackGround2,(0,0))
        for button in level2_buttons:
            button.draw()
    elif level == 3:
        screen.blit(BackGround3,(0,0))
        for button in level3_buttons:
            button.draw()      
    elif level == 4:
        screen.blit(BackGround4,(0,0))
        for button in level4_buttons:
            button.draw()
            

        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 37)
        textSurfaceTitle3 = fontTitle.render('Your village is being invaded', True, TEA) 
        textRectTitle3 = textSurfaceTitle3.get_rect()
        textRectTitle3.center = (390, 250)
        screen.blit(textSurfaceTitle3, textRectTitle3)


        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 37)
        textSurfaceTitle4 = fontTitle.render('By enemy explosives.', True, TEA) 
        textRectTitle4 = textSurfaceTitle4.get_rect()
        textRectTitle4.center = (390, 290)
        screen.blit(textSurfaceTitle4, textRectTitle4)

        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 37)
        textSurfaceTitle5 = fontTitle.render('Defend, ', True, TEA) 
        textRectTitle5 = textSurfaceTitle5.get_rect()
        textRectTitle5.center = (390, 400)
        screen.blit(textSurfaceTitle5, textRectTitle5)


        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 37)
        textSurfaceTitle5 = fontTitle.render('Your village from destruction. ', True, TEA) 
        textRectTitle5 = textSurfaceTitle5.get_rect()
        textRectTitle5.center = (390, 440)
        screen.blit(textSurfaceTitle5, textRectTitle5)


        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 37)
        textSurfaceTitle6 = fontTitle.render('Use the cursor/mouse to pop enemy explosives!', True, TEA) 
        textRectTitle6 = textSurfaceTitle6.get_rect()
        textRectTitle6.center = (395, 480)
        screen.blit(textSurfaceTitle6, textRectTitle6)



    






    elif level == 6:
        #game code

        #check to see if balloon is hit
        #if it is hit, increase score
        for balloon in ALL_sprites_lists:
            if pygame.mouse.get_pressed()[0] and balloon.rect.collidepoint(pygame.mouse.get_pos()):
                balloon.rect.x = random.randint(-2100,0)
                balloon.rect.y = 355
                score += 5
            
                #pygame.sprite.Sprite.remove(myBalloon)
           
  
               
         #pygame.sprite.Sprite.remove
        
        #update positions of balloons
        for Balloon in ALL_sprites_lists:
            Health = Balloon.moveRight(Health)

        #draw background, buttons and sprites
        screen.blit(BackGround5,(0,0))
        for button in level6_buttons:
            button.draw()

       

        ALL_sprites_lists.draw(screen)
       # if Balloon.image.collidepoint(pos):
           # Hit = True
           # Balloon.image.y = (900)
           # Balloon.image.x = (900) 
           # myBalloon = Balloon(BalloonImage1, 70, 70, -5)
        
        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 64)
        textSurfaceTitle7 = fontTitle.render('Village health:' + str(Health) , True, RED) 
        textRectTitle7 = textSurfaceTitle7.get_rect()
        textRectTitle7.center = (260,40)
        screen.blit(textSurfaceTitle7, textRectTitle7)
        if balloon.rect.x > 800:
                Health -= 20

        if Health <= 0:
           level = 8
           for balloon in ALL_sprites_lists:
               balloon.speed = 0


    elif level == 7:
        #game code

        #check to see if balloon is hit
        #if it is hit, increase score
        for balloon in ALL_sprites_lists:
            if pygame.mouse.get_pressed()[0] and balloon.rect.collidepoint(pygame.mouse.get_pos()):
                balloon.rect.x = random.randint(-2100,0)
                balloon.rect.y = random.randint(math.floor(SCREENHEIGHT/3), math.floor(SCREENHEIGHT*3/4))
                score += 5
            
                #pygame.sprite.Sprite.remove(myBalloon)
           
  
               
         #pygame.sprite.Sprite.remove
        
        #update positions of balloons
        for Balloon in ALL_sprites_lists:
            Health = Balloon.moveRight(Health)

        #draw background, buttons and sprites
        screen.blit(BackGround7,(0,0))
        for button in level7_buttons:
            button.draw()

       

        ALL_sprites_lists.draw(screen)
        #Draws players health, if ballon is not clicked health -20
        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 64)
        textSurfaceTitle7 = fontTitle.render('Village health:' + str(Health) , True, RED) 
        textRectTitle7 = textSurfaceTitle7.get_rect()
        textRectTitle7.center = (260,40)
        screen.blit(textSurfaceTitle7, textRectTitle7)
        if balloon.rect.x > 800:
                Health -= 20

        #If health is 0 bringss player to a retry screen, that displays there score
        if Health <= 0:
           level = 8
           for balloon in ALL_sprites_lists:
               balloon.speed = 0

    #Retry screen, displays score and button to retry
    elif level == 8:
        screen.blit(BackGround8,(0,0))
        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 64)
        textSurfaceTitle9 = fontTitle.render('SCORE!:' + str(score) , True, BRED) 
        textRectTitle9 = textSurfaceTitle9.get_rect()
        textRectTitle9.center = (405,300)
        screen.blit(textSurfaceTitle9, textRectTitle9)

        fontTitle = pygame.font.Font('gomarice_no_continue.ttf', 42)
        textSurfaceTitle10 = fontTitle.render("Your village has been destryoed!!", True, BRED) 
        textRectTitle10 = textSurfaceTitle10.get_rect()
        textRectTitle10.center = (405,200)
        screen.blit(textSurfaceTitle10, textRectTitle10)

        for button in level8_buttons:
            button.draw()
            
    elif level == 10:
        screen.blit(BackGround6,(0,0))
        for button in level10_buttons:
            button.draw()

            
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)



pygame.quit()
