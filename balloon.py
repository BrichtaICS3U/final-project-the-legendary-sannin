import pygame
SCREENWIDTH = 800
SCREENHEIGHT = 710
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (188, 16, 22)
BLUE = (0, 0, 255)
BRED = (188, 16, 22)
BBRED = (216, 15, 21)
TEA = (208, 240, 192)
class Balloon(pygame.sprite.Sprite):

    def __init__(self,image,width,height,speed):

        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        self.speed = speed

        self.image = pygame.transform.scale(self.image, (width, height))
        
        self.rect = self.image.get_rect()

    def moveRight(self):
        self.rect.x += self.speed
        if self.rect.x > SCREENWIDTH:
            self.rect.x = -2*self.width
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
