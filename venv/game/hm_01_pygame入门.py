import pygame
from plane_sprite import *

hero = pygame.Rect(150, 500, 102, 126)
clock = pygame.time.Clock()
bg = pygame.image.load("../images/background.png")
hero_bg = pygame.image.load("../images/me1.png")
screen = pygame.display.set_mode((480, 700))

while True:
    clock.tick(60)
    hero.y -= 1

    if hero.y +hero.height <= 0:
        hero.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero_bg, hero)
    pygame.display.update()

    for event in pygame.event.get():
        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            # 直接退出系统
            exit()