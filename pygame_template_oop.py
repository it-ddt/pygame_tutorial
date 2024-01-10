import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Pygame OOP Template")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.run()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

    def update(self):
        # Логика игры
        pass

    def render(self):
        self.screen.fill((255, 255, 255))

        # Render game elements here

        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # Set the frame rate to 60 FPS

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
