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

    def __init__(self,color,width,height,speed):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        pygame.draw.ellipse(self.image, RED, [100, 100, 100, 100])

        self.rect = self.image.get_rect()

    def moveRight(self):
        speed = 2
        self.rect.x += self.speed
        if self.rect.x > SCREENWIDTH:
            self.rect.x = -100
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
