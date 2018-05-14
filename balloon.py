import pygame


class Balloon(pygame.sprite.Sprite):

    def __init__(self,picture,width,height,speed):

        super().__init__()

        self.image = picture
        self.rect = self.image.get_rect()
        self.speed = speed

    def moveRight(self):
        # speed = 2
        self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
