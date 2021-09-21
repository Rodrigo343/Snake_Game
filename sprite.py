import pygame
from pygame.locals import *
from sys import exit

pygame.init()

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(1,16):
            self.sprites.append(pygame.image.load('sprites/snake{0}.png'.format(i)))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))


        self.rect = self.image.get_rect()
        self.rect.topleft = 300,100

        self.animar = False

    def atacar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if(self.atual >= len(self.sprites)):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128*3, 64*3))
            
largura = 640
altura = 480

preto = (0,0,0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')



todasSprites = pygame.sprite.Group()
sapo = Sapo()
todasSprites.add(sapo)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            sapo.atacar()

    todasSprites.draw(tela)
    todasSprites.update()

    pygame.display.flip()
