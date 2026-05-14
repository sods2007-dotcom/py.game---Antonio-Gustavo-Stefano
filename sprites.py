# Importa pygame
import pygame

# Importa configurações
from settings import WIDTH, HEIGHT, WHITE, BLACK


# Classe da bola
class Ball(pygame.sprite.Sprite):

    # Inicialização da bola
    def __init__(self):

        super().__init__()

        # Define raio
        self.radius = 14

        # Cria superfície da bola
        self.image = pygame.Surface(
            (self.radius * 2, self.radius * 2),
            pygame.SRCALPHA,
        )

        # Desenha círculo branco
        pygame.draw.circle(
            self.image,
            WHITE,
            (self.radius, self.radius),
            self.radius,
        )

        # Borda preta
        pygame.draw.circle(
            self.image,
            BLACK,
            (self.radius, self.radius),
            self.radius,
            2,
        )

        # Cria retângulo da bola
        self.rect = self.image.get_rect()

        # Define posição inicial
        self.rect.center = (WIDTH // 2, HEIGHT - 150)

        # Vetor de posição
        self.pos = pygame.Vector2(self.rect.center)

    # Atualiza posição da bola
    def update(self):

        self.rect.center = self.pos