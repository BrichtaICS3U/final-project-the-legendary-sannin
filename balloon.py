import pygame
SCREENWIDTH = 800
SCREENHEIGHT = 710

class Balloon(pygame.sprite.Sprite):

    def __init__(self,picture,width,height,speed):

        super().__init__()
        self.image = picture
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed
        self.rect.y = -200
        print(self.rect.x)
        print(self.rect.y)

    def moveRight(self):
        speed = 2
        self.rect.x += self.speed
        if self.rect.x > SCREENWIDTH:
            self.rect.x = -100

    def draw(self, screen):
        screen.blit(self.image, self.rect)
