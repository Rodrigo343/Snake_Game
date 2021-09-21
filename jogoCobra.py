import pygame
from random import randint
from sys import exit

class Cobra():
    
    def __init__(self, x_cobra, y_cobra):
         self.x_cobra = int(x_cobra)
         self.y_cobra = int(y_cobra)
         self.__lista_corpo = []
         self.__lista_cabeca = []
         self.tamanho = 3
         self.morto = False

    @property  
    def x_cobra(self):
        return self.__x_cobra
    
    @x_cobra.setter  
    def x_cobra(self, x_cobra):
       self.__x_cobra = x_cobra

    @property  
    def y_cobra(self):
        return self.__y_cobra
    
    @y_cobra.setter  
    def y_cobra(self, y_cobra):
       self.__y_cobra = y_cobra

    @property  
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter  
    def tamanho(self, tamanho):
       self.__tamanho = tamanho

    @property  
    def morto(self):
        return self.__morto
    
    @morto.setter  
    def morto(self, morto):
       self.__morto = morto

    @property  
    def lista_corpo(self):
        return self.__lista_corpo
    
    @lista_corpo.setter  
    def lista_corpo(self, lista_corpo):
       self.__lista_corpo.append(lista_corpo)

    @property  
    def lista_cabeca(self):
        return self.__lista_cabeca
    
    @lista_cabeca.setter  
    def lista_cabeca(self, lista_cabeca):
       self.__lista_cabeca.append(lista_cabeca)

    def correcaoTamanho(self):
       del self.__lista_corpo[0] 

    def atualizaPosicaoCobra(self, x, y):
        self.x_cobra = self.__x_cobra + x
        self.y_cobra = self.__y_cobra + y

    def atualizaTamanho(self, tamanho):
        self.tamanho = self.__tamanho + tamanho
    
    def resetaCorpo(self):
        self.__lista_corpo = []

    def resetaCabeca(self):
        self.__lista_cabeca = []

class Maca():
    
    def __init__(self, x_maca, y_maca):
         self.x_maca = int(x_maca)
         self.y_maca = int(y_maca)

    @property  
    def x_maca(self):
        return self.__x_maca
    
    @x_maca.setter  
    def x_maca(self, x_maca):
       self.__x_maca = x_maca

    @property  
    def y_maca(self):
        return self.__y_maca
    
    @y_maca.setter  
    def y_maca(self, y_maca):
       self.__y_maca = y_maca

class Game():
    
    def __init__(self, velocidade, y_controle):

         self.velocidade = velocidade
         self.x_controle = velocidade
         self.y_controle = y_controle
         self.largura = 600
         self.altura = 600
         self.pontos = 0

    @property  
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter  
    def velocidade(self, velocidade):
       self.__velocidade = velocidade

    @property  
    def x_controle(self):
        return self.__x_controle
    
    @x_controle.setter  
    def x_controle(self, x_controle):
       self.__x_controle = x_controle

    @property  
    def y_controle(self):
        return self.__y_controle
    
    @y_controle.setter  
    def y_controle(self, y_controle):
       self.__y_controle = y_controle

    @property  
    def largura(self):
        return self.__largura
    
    @largura.setter  
    def largura(self, largura):
       self.__largura = largura

    @property  
    def altura(self):
        return self.__altura
    
    @altura.setter  
    def altura(self, altura):
       self.__altura = altura
    
    @property  
    def pontos(self):
        return self.__pontos
    
    @pontos.setter  
    def pontos(self, pontos):
       self.__pontos = pontos

def main():
    pygame.init()

    game = Game(8, 0)
    cobra = Cobra((game.largura/2), (game.altura/2) )
    maca = Maca(randint(50, (game.largura-50)), randint(60, (game.altura-50)))

    fonte = pygame.font.SysFont('arial', 20, True, True)

    pygame.mixer.music.set_volume(0.05)
    musica_fundo = pygame.mixer.music.load('sons/BoxCat Games.mp3')
    pygame.mixer.music.play(-1)
    barulho_colisao = pygame.mixer.Sound('sons/smw_coin.wav')
    barulho_colisao.set_volume(0.20)

    janela = pygame.display.set_mode((game.largura,game.altura))
    relogio = pygame.time.Clock()

    def aumentaCobra(lista_corpo):
        for i in lista_corpo:
            pygame.draw.rect(janela, (0,255,0), (i[0],i[1],20,20))

    def reiniciar_game():
        game.pontos = 0
        cobra.tamanho = 10
        cobra.x_cobra = game.largura/2
        cobra.y_cobra = game.altura/2
        cobra.morto = False
        cobra.resetaCorpo()
        maca.x_maca = randint(40, game.largura-50)
        maca.y_maca = randint(50, game.altura-50)
    

    def teclas():
        global janela_aberta
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    if game.x_controle == game.velocidade:
                        pass
                    else:
                        game.x_controle = -game.velocidade
                        game.y_controle = 0
                elif event.key == pygame.K_d:
                    if game.x_controle == -game.velocidade:
                        pass
                    else:
                        game.x_controle = game.velocidade
                        game.y_controle = 0
                elif event.key == pygame.K_w:
                    if game.y_controle == game.velocidade:
                        pass
                    else:
                        game.y_controle = -game.velocidade
                        game.x_controle = 0
                elif event.key == pygame.K_s:
                    if game.y_controle == -game.velocidade:
                        pass
                    else:
                        game.y_controle = game.velocidade
                        game.x_controle = 0

                elif event.key == pygame.K_r:
                    reiniciar_game()
                
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

    def comeMaca():
        if cobraDesenho.colliderect(macaDesenho):
            maca.x_maca = randint(50, game.largura-50)
            maca.y_maca = randint(50, game.altura-50)
            game.pontos = game.pontos + 10
            barulho_colisao.play()
            cobra.atualizaTamanho(3)

    def colisaoComCorpo():
        if(cobra.lista_corpo.count(cobra.lista_cabeca) > 1):
            mensagem = "Game Over! Pressione a tecla R para jogar novamente"
            texto_formatado = fonte.render(mensagem, True, (0,0,0))
            ret_texto = texto_formatado.get_rect()

            mensagem2 = "Pressione a tecla Q para Sair do jogo"
            texto_formatado2 = fonte.render(mensagem2, True, (0,0,0))
            ret_texto2 = texto_formatado2.get_rect()

            cobra.morto = True

        while cobra.morto:
            janela.fill((255,255,255))
            ret_texto.center = (game.largura/2, game.altura/2)
            ret_texto2.center = (game.largura/2, game.altura/2 + 25)
            janela.blit(texto_formatado2, ret_texto2)
            janela.blit(texto_formatado, ret_texto)
            pygame.display.update()
  
            teclas()

    def passaTela():
        if cobra.x_cobra > game.largura:
            cobra.x_cobra = 0
        elif cobra.x_cobra < 0:
            cobra.x_cobra = game.largura
        elif cobra.y_cobra > game.altura:
            cobra.y_cobra = 0
        elif cobra.y_cobra < 0:
            cobra.y_cobra = game.altura 

    def limitaTamanhoCobra():
        if len(cobra.lista_corpo) > cobra.tamanho:
            cobra.correcaoTamanho()

    def posicaoCobra():
        cobra.resetaCabeca()
        cobra.lista_cabeca = cobra.x_cobra
        cobra.lista_cabeca = cobra.y_cobra
        cobra.lista_corpo = cobra.lista_cabeca


    while True:

        relogio.tick(30)
        janela.fill((255,255,255))
        mensagem = '{0} pontos'.format(game.pontos)
        texto_formatado = fonte.render(mensagem, True, (0,0,0))

        teclas()

        cobra.atualizaPosicaoCobra(game.x_controle, game.y_controle)
        cobraDesenho = pygame.draw.rect(janela, (0,255,0), (cobra.x_cobra,cobra.y_cobra,20,20))
        macaDesenho = pygame.draw.rect(janela, (255,0,0), (maca.x_maca,maca.y_maca,20,20))

        comeMaca()
        
        posicaoCobra()

        colisaoComCorpo()
                
        passaTela()   
                        
        limitaTamanhoCobra()
        
        aumentaCobra(cobra.lista_corpo)

        janela.blit(texto_formatado, (450, 40))
        pygame.display.update()

if __name__ == '__main__':
    main()