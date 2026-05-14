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

# Importa a biblioteca pygame
import pygame

# Importa configurações do jogo
from settings import (
    WIDTH,
    HEIGHT,
    FPS,
    TITLE,
    GREEN,
    DARK_GREEN,
    WHITE,
    GRAY,
    GOAL_X,
    GOAL_Y,
    GOAL_WIDTH,
    GOAL_HEIGHT,
)


# Função responsável por desenhar o campo
def draw_field(screen):

    # Cor principal do gramado
    screen.fill(GREEN)

    # Parte superior do gramado
    pygame.draw.rect(
        screen,
        DARK_GREEN,
        (0, 0, WIDTH, HEIGHT // 2),
    )

    # Desenha o gol
    pygame.draw.rect(
        screen,
        WHITE,
        (GOAL_X, GOAL_Y, GOAL_WIDTH, GOAL_HEIGHT),
        5,
    )

    # Linha inferior do gol
    pygame.draw.line(
        screen,
        GRAY,
        (GOAL_X, GOAL_Y + GOAL_HEIGHT),
        (GOAL_X + GOAL_WIDTH, GOAL_Y + GOAL_HEIGHT),
        6,
    )

    # Área do goleiro
    pygame.draw.rect(
        screen,
        WHITE,
        (WIDTH // 2 - 250, GOAL_Y + GOAL_HEIGHT, 500, 210),
        3,
    )

    # Semi círculo da área
    pygame.draw.arc(
        screen,
        WHITE,
        (WIDTH // 2 - 90, GOAL_Y + GOAL_HEIGHT + 150, 180, 110),
        3.14,
        6.28,
        3,
    )

    # Marca do pênalti
    pygame.draw.circle(
        screen,
        WHITE,
        (WIDTH // 2, HEIGHT - 150),
        6,
    )


# Função principal do jogo
def main():

    # Inicializa o pygame
    pygame.init()

    # Cria a janela do jogo
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Define o título da janela
    pygame.display.set_caption(TITLE)

    # Controla FPS
    clock = pygame.time.Clock()

    # Variável principal do loop
    running = True

    # Loop principal
    while running:

        # Define FPS
        clock.tick(FPS)

        # Verifica eventos
        for event in pygame.event.get():

            # Fecha o jogo
            if event.type == pygame.QUIT:
                running = False

        # Desenha o campo
        draw_field(screen)

        # Atualiza a tela
        pygame.display.flip()

    # Finaliza pygame
    pygame.quit()


# Executa o jogo
if __name__ == "__main__":
    main()