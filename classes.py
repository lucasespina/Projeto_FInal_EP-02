import pygame

class Nota(pygame.sprite.Sprite):
    def __init__(self,img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.aceleracao = 1

    def update(self):
        self.rect.y += self.aceleracao
        if self.rect.y > 600:
            self.kill()