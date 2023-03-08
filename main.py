import pygame

import image_converter

pygame.init()

WIDTH, HEIGHT = 1280, 720
# WIDTH, HEIGHT = 1920, 1010


class Game:
    window: pygame.Surface

    def __init__(self):
        self.create_window()
        self.size = 900
        self.bomb = image_converter.convert(filename='bomb', width=self.size)
        self.bomb_transform = pygame.transform.scale(pygame.image.load(r'.\images\originals\original_bomb.png'), (self.size, self.size))
        self.mainloop()

    def create_window(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))

    def window_updating(self):
        self.window.fill('white')
        self.window.blit(self.bomb, (20, 20))
        self.window.blit(self.bomb_transform, (700, 20))

        pygame.display.flip()

    def mainloop(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.window_updating()


if __name__ == '__main__':
    Game()
