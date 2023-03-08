import pygame

import image_converter

pygame.init()

WIDTH, HEIGHT = 1280, 720
# WIDTH, HEIGHT = 1920, 1010


class Game:
    window: pygame.Surface

    def __init__(self):
        self.create_window()
        self.bomb = image_converter.convert('bomb')
        self.mainloop()

    def create_window(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))

    def window_updating(self):
        self.window.fill('white')
        self.window.blit(self.bomb, (200, 200))

        pygame.display.flip()

    def mainloop(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.window_updating()


if __name__ == '__main__':
    Game()
