import pygame
from sys import exit
x = 800
y = 400
pygame.init()
tela = pygame.display.set_mode((x,y))
pygame.display.set_caption('Teste')
relogio = pygame.time.Clock()
teste_fonte = pygame.font.Font('font\Pixeltype.ttf', 50)

teste_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
texto_surface = teste_fonte.render('Pontos', False, 'Black')

caracol_imagem = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
caracol_imagem2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
caracol_retang = caracol_imagem.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_retang = player_surface.get_rect(midbottom = (80,300))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    tela.blit(ground_surface, (0,300))
    tela.blit(teste_surface, (0, 0))
    tela.blit(texto_surface, (300,50))
    caracol_retang.right -= 5
    if caracol_retang.right < -100:
        caracol_retang = 800
    tela.blit(caracol_imagem, caracol_retang)
    tela.blit(player_surface, player_retang)
    pygame.display.update()
    relogio.tick(60)