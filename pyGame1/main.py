import pygame
from sys import exit

x = 800
y = 400
pygame.init()
tela = pygame.display.set_mode((x,y))
pygame.display.set_caption('Teste')
relogio = pygame.time.Clock()
teste_fonte = pygame.font.Font('font\Pixeltype.ttf', 50)

game_ativo = True


teste_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

texto_surface = teste_fonte.render('Pontos', False, 'Black')
pontos_retang = texto_surface.get_rect(center = (400,50))

caracol_imagem = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
caracol_imagem2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
caracol_retang = caracol_imagem.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_retang = player_surface.get_rect(midbottom = (80,300))

player_gravidade = 0

#pontos = 0
#pontos_surface = teste_fonte.render(f'{pontos}', False, 'Black')
#pontos_retang = pontos_surface.get_rect(center = (50,50))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_ativo:
            if evento.type == pygame.MOUSEBUTTONDOWN and player_retang.bottom >= 300:
                #print('mause click')
                #print(evento.pos)
                if player_retang.collidepoint(evento.pos):
                    player_gravidade = -20

            if evento.type == pygame.KEYDOWN and player_retang.bottom >= 300:
                if evento.key == pygame.K_SPACE:
                    player_gravidade = -20
        else:
            if evento.key == pygame.K_SPACE and evento.type == pygame.KEYDOWN:
                game_ativo = True
                caracol_retang.left = 800
    if game_ativo == True:
        tela.blit(ground_surface, (0,300))
        tela.blit(teste_surface, (0, 0))
        pygame.draw.rect(tela, 'Pink', pontos_retang, 6)
        tela.blit(texto_surface, pontos_retang)
        caracol_retang.right -= 5
        if caracol_retang.right < -100:
            caracol_retang.right = 800
        tela.blit(caracol_imagem, caracol_retang)
        tela.blit(player_surface, player_retang)

        #if player_retang.colliderect(caracol_retang):
        #    pontos+=1
        mause_pos = pygame.mouse.get_pos()
        #if player_retang.collidepoint(mause_pos):
            #print(pygame.mouse.get_pressed())
            #print('coledindo')
        player_gravidade +=1
        player_retang.y += player_gravidade
        if player_retang.bottom >= 300:
            player_retang.bottom = 300

        if caracol_retang.colliderect(player_retang):
            game_ativo = False
    else:
        tela.fill('White')

    pygame.display.update()
    relogio.tick(60)
