import pygame
import time

pygame.init()

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Догонялки")
x1 = 0
y1 = 400
x2 = 400
y2 = 0
game = True

class Player():
    def __init__(self, image):
        self.image = image
        self.sprite = pygame.transform.scale(pygame.image.load(self.image), (100, 100))
        self.rect = self.sprite.get_rect()
    def otrisovka(self, x, y):
            self.x = x
            self.y = y 
            window.blit(self.sprite, (x, y))

    def fire(self):
        pass

class Monster():
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.sprite = pygame.transform.scale(pygame.image.load(self.image), (100, 100))
        self.rect = self.sprite.get_rect()
    


num_fire = 0
backgraund = pygame.transform.scale(pygame.image.load("galaxy.jpg"), (700, 500))

player = Player("rocket.png")

clock = pygame.time.Clock()
FPS = 60

clock.tick(FPS)

#создай 2 спрайта и размести их на сцене

sprite2 = pygame.transform.scale(pygame.image.load("ufo.png"), (100, 100))

rect2 = sprite2.get_rect()


#обработай событие «клик по кнопке "Закрыть окно"»
while game:
    keys = pygame.key.get_pressed()
    window.blit(backgraund, (0, 0))
    player.otrisovka(x1, x2)
    window.blit(sprite2, (x2, y2))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    if keys[pygame.K_LEFT] and x1 > 0:
        x1 -= 10
    if keys[pygame.K_RIGHT] and x1 < 600:
        x1 += 10

    y2 += 1
    y = y1 - y2

    pygame.display.update()