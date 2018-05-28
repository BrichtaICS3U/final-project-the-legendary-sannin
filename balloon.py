import pygame
SCREENWIDTH = 800
SCREENHEIGHT = 710
WHITE = (255,255,255)
class Balloon(pygame.sprite.Sprite):

    def __init__(self,color,width,height,speed):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.width=width
        self.height=height
        self.color = color
        self.speed = speed

        pygame.draw.rect(self.image, color, [405, 355, 30, 30])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed
        print(self.rect.x)
        print(self.rect.y)

    def moveRight(self):
        speed = 2
        self.rect.x += self.speed
        if self.rect.x > SCREENWIDTH:
            self.rect.x = -100
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
