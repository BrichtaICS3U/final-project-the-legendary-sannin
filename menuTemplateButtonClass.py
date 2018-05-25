

# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

# for balloon in Balloon:
# if Balloon.rect.collidepoint(pos):
# pygame.sprite.Sprite.remove
import pygame, sys, random
from balloon import Balloon
from car import Car
pygame.init()

BackGround1 = pygame.image.load('P:/final-project-the-legendary-sannin/710573-most-popular-tobi-wallpaper-1920x1080-for-hd-1080p.jpg')
BackGround2 = pygame.image.load('P:/final-project-the-legendary-sannin/maxresdefault (2).jpg')
BackGround3 = pygame.image.load('P:/final-project-the-legendary-sannin/893996-beautiful-cool-naruto-backgrounds-1920x1080.jpg')
BackGround4 = pygame.image.load('P:/final-project-the-legendary-sannin/Nijū_Shōtai_Raidō.png')
BackGround5 = pygame.image.load('P:/final-project-the-legendary-sannin/grass_template_straightpath.jpg')

#https://stackoverflow.com/questions/21947389/how-to-continuously-move-an-image-in-pygame
import pygame, sys
pygame.init()


 #P:/maxresdefault.jpg
#pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
#pygame.mixer.music.load('Naruto_Song.mp3')
#pygame.mixer.music.play(-1)

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

def my_mainmenu_function():
    """A funtion that will return you to the main menu"""
    global level
    level = 1

def pop(score):
    pos =pygame.mouse.get_pos()
    Pop = False
    for balloon in Balloon:
        if Balloon.rect.collidepoint(pos):
            Pop = True
            score += 1
        print ("gang gang finna work")
        
def mousebuttondown(level):
    """A function th        screen.blit(BackGround3,(0,0))
at checks which button ):
                was pressed"""
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
             for balloon in Balloon:
                    button.call_back()
    elif level == 10:
        for button in level10_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()


level = 1
carryOn = True
clock = pygame.time.Clock()


ALL_sprites_lists = pygame.sprite.Group()
BalloonImage1 = pygame.image.load("P:/final-project-the-legendary-sannin/new-red-balloon-hi.png")
for i in range(5):
    myBalloon = Balloon(BalloonImage1, 30, 70, 5)
    myBalloon.rect.x = random.randint(-2100,0)
    ALL_sprites_lists.add(myBalloon)


#create button objects
button_01 = Button("Settings", (SCREENWIDTH*2/3.3, SCREENHEIGHT*3.5/4), my_settings_function)
button_02 = Button("Back", (SCREENWIDTH/2, SCREENHEIGHT/3), my_back_function)
button_03 = Button("Quit", (SCREENWIDTH/2.7, SCREENHEIGHT*3.5/4), my_quit_function, bg=(50, 200, 20))
button_04 = Button("Gemu Shimasu", (SCREENWIDTH/2, SCREENHEIGHT/2), my_playgame_function)
button_05 = Button("Sound", (SCREENWIDTH/2, SCREENHEIGHT/2), my_sound_function)
button_06 = Button("Sound On", (SCREENWIDTH/4, SCREENHEIGHT/2), my_soundon_function)
button_07 = Button("Sound Off", (SCREENWIDTH *3/4, SCREENHEIGHT/2), my_soundoff_function)
button_08 = Button("Next", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_next_function)
button_09 = Button("MainMenu", (SCREENWIDTH/2, SCREENHEIGHT*1/5), my_mainmenu_function)
button_10 = Button("Instructions", (SCREENWIDTH/2, SCREENHEIGHT/2), my_instructions_function)
button_11 = Button("Credits", (SCREENWIDTH/2, SCREENHEIGHT*3/4), my_credits_function)
button_12 = Button("Gemu Shimasu", (SCREENWIDTH/2 , SCREENHEIGHT*2/5), my_playgame_function)
button_13 = Button("MainMenu", (SCREENWIDTH/2.7, SCREENHEIGHT*2.5/5), my_mainmenu_function) # level 4 main menu
button_14 = Button("Gemu Shimasu", (SCREENWIDTH/1.6 , SCREENHEIGHT*2.5/5), my_playgame_function) #level 4 game start

#Game title
#for Balloon in ALL_sprites_lists:
   # Balloon.moveRight()
    #Balloon.rect.y > SCREENWIDTH


#screen.blit(BackGround1,(0,0))

#arrange button groups depending on level
level1_buttons = [button_01, button_03 , button_04]
level2_buttons = [button_02, button_05, button_06, button_07]
level3_buttons = [button_09, button_10, button_11]
level4_buttons = [button_13, button_14,] 
level5_buttons = [button_02]
level6_buttons = [button_09]
level7_buttons = []
level10_buttons = [button_09]
#credits (level 10)
# level3_buttons = [button_08]
#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close bTEAutton
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            if level <= 6:
                mousebuttondown(level)
            else:
                score = pop(score)

    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(BLACK)
    

    

    # Draw buttons
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
        #screen.blit(BackGround5,(0,0))
        screen.blit(BackGround5,(0,0))
        for button in level6_buttons:
            button.draw()
        for Balloon in ALL_sprites_lists:
            Balloon.moveRight() #Balloon.rect.y > SCREENWIDTH
            ALL_sprites_lists.draw(screen)
            #game code
    elif level == 10:
        screen.blit(BackGround6,(0,0))
        for button in level10_buttons:
            button.draw() 
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)



pygame.quit()


