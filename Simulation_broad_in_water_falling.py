from Classes import WaterDrops, Board
import pygame

pygame.init()
Screen_size = 1280, 720
screen = pygame.display.set_mode(Screen_size)

clock = pygame.time.Clock()
running = True

times = 0

print(Screen_size[0])

rect_board = Board(
    (255, 0, 0), 10, 5, 1280 / 2, 720 / 2
)

while running:

    screen.fill("black")
    pygame.display.flip()

    clock.tick(60)
    times += 1

    if times > 100:
        pygame.quit()
    pass

pygame.quit()

if __name__ == "__main__":
    pass
