# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()
BackGround = pygame.image.load('P:/ICSsummative/final-project-the-legendary-sannin/710573-most-popular-tobi-wallpaper-1920x1080-for-hd-1080p.jpg')

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
<<<<<<< HEAD
    def __init__(self, txt, location, action, bg=RED, fg=BLACK, size=(100, 50), font_name="Segoe Print", font_size=16):
=======
    def __init__(self, txt, location, action, bg=BRED, fg=BLACK, size=(100, 50), font_name="Segoe Print", font_size=16):
>>>>>>> 4343ab8ff483a5424c60cd48faa4cad85110abf9
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
            self.bg = GRAY  # mouseover color

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
    """A function that takesm you to instructions when pressed"""
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
    

def mousebuttondown(level):
    """A function that checks which button was pressed"""
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

    elif level == 10:
        for button in level10_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()


level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects
button_01 = Button("Settings", (SCREENWIDTH/2, SCREENHEIGHT/3), my_settings_function)
button_02 = Button("Back", (SCREENWIDTH/2, SCREENHEIGHT/3), my_back_function)
button_03 = Button("Quit", (SCREENWIDTH/2.4, SCREENHEIGHT*3.2/4), my_quit_function, bg=(50, 200, 20))
button_04 = Button("PLAYGAME", (SCREENWIDTH/2, SCREENHEIGHT/1), my_playgame_function)
button_05 = Button("Sound", (SCREENWIDTH/2, SCREENHEIGHT/2), my_sound_function)
button_06 = Button("Sound On", (SCREENWIDTH/4, SCREENHEIGHT/2), my_soundon_function)
button_07 = Button("Sound Off", (SCREENWIDTH *3/4, SCREENHEIGHT/2), my_soundoff_function)
button_08 = Button("Next", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_next_function)
button_09 = Button("MainMenu", (SCREENWIDTH/2, SCREENHEIGHT*1/5),my_mainmenu_function)
button_10 = Button("Instructions", (SCREENWIDTH/2, SCREENHEIGHT/2), my_instructions_function)
button_11 = Button("Credits", (SCREENWIDTH/2, SCREENHEIGHT*3/4), my_credits_function)
#Game title
<<<<<<< HEAD
fontTitle = pygame.font.Font('P:/ICSsummative/final-project-the-legendary-sannin/gomarice_no_continue.ttf', 64)
textSurfaceTitle = fontTitle.render('Indras!', True, GREY) 
textRectTitle = textSurfaceTitle.get_rect()
=======
fontTitle = pygame.font.Font('P:/final-project-the-legendary-sannin/gomarice_no_continue.ttf', 64)
textSurfaceTitle1 = fontTitle.render('Indras!', True, GREY) 
textRectTitle1 = textSurfaceTitle1.get_rect()

textRectTitle1.center = (380, 110)

fontTitle = pygame.font.Font('P:/final-project-the-legendary-sannin/gomarice_no_continue.ttf', 64)
textSurfaceTitle2 = fontTitle.render('Arrow!', True, GREY) 
textRectTitle2 = textSurfaceTitle2.get_rect()
>>>>>>> 4343ab8ff483a5424c60cd48faa4cad85110abf9

textRectTitle2.center = (380, 160)


#arrange button groups depending on level
level1_buttons = [button_01, button_03 , button_04]
level2_buttons = [button_02, button_03 , button_05, button_06, button_07]
level3_buttons = [button_09, button_10, button_11]
level4_buttons = [button_02, button_09]
level5_buttons = [button_02]
level10_buttons = [button_09]
#credits (level 10)
# level3_buttons = [button_08]
#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)

    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(BLACK)
    screen.blit(BackGround,(0,0))

    screen.blit(textSurfaceTitle1, textRectTitle1)
    screen.blit(textSurfaceTitle2, textRectTitle2)

    # Draw buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()
    elif level == 2:
        for button in level2_buttons:
            button.draw()
    elif level == 3:
        for button in level3_buttons:
            button.draw()      
    elif level == 4:
        for button in level4_buttons:
            button.draw() 
    elif level == 5:
        for button in level5_buttons:
            button.draw()
    elif level == 10:
        for button in level10_buttons:
            button.draw() 
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()


