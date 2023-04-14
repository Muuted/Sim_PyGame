from Classes import WaterDrops,Board
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()
running = True

times = 0

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
