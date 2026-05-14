# Importa a biblioteca pygame
import pygame

# Importa as configurações principais do jogo
from settings import WIDTH, HEIGHT, FPS, TITLE, GREEN


# Função principal do jogo
def main():
    # Inicializa todos os módulos do pygame
    pygame.init()

    # Cria a janela do jogo
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Define o título da janela
    pygame.display.set_caption(TITLE)

    # Controla a taxa de quadros por segundo
    clock = pygame.time.Clock()

    # Variável que controla se o jogo continua rodando
    running = True

    # Loop principal do jogo
    while running:
        # Mantém o jogo rodando no FPS definido
        clock.tick(FPS)

        # Verifica todos os eventos do pygame
        for event in pygame.event.get():
            # Fecha o jogo quando o usuário clica no X da janela
            if event.type == pygame.QUIT:
                running = False

        # Pinta o fundo da tela de verde
        screen.fill(GREEN)

        # Atualiza a tela com tudo que foi desenhado
        pygame.display.flip()

    # Encerra o pygame corretamente
    pygame.quit()


# Garante que o jogo rode apenas quando este arquivo for executado diretamente
if __name__ == "__main__":
    main()