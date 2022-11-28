import pygame

pygame.init()
pygame.display.set_caption("  clobrda")
velikost = (540, 270)
okno = pygame.display.set_mode(velikost)
clock = pygame.time.Clock()

barva = (100, 200, 0)
barva1 = (0, 200, 0)
hrac = pygame.image.load("pandulak.png")
hrac = pygame.transform.scale(hrac, (45, 45))
otoceny_hrac = pygame.transform.rotate(hrac, 0)

WIDTH = 12
HEIGHT = 6

zx = 2
zy = 1

def game_to_screen(x, y):
    return (x * 45, y *45)
    
def animate(nx, ny):
    global zx, zy
    
    duration = 500
    t = 0
    sx, sy = game_to_screen(zx, zy)
    ex, ey = game_to_screen(nx, ny)
    while t < duration:
        new = t / duration
        old = 1 - new
        x = old * sx + new * ex
        y = old * sy + new * ey
        okno.fill(barva1)
        draw_grid()
        okno.blit(otoceny_hrac, (x, y))
        pygame.display.update()
        t = t + clock.tick()

    zx = nx
    zy = ny
    
def draw_grid():
    for x in range(WIDTH):
      for y in range(HEIGHT):
        rect = (game_to_screen(x, y), (45, 45))
        pygame.draw.rect(okno, barva1, rect)

while True:
    okno.fill(barva)
    draw_grid()
    okno.blit(otoceny_hrac, game_to_screen(zx, zy))
  
    pygame.display.update()

    print("...")
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        otoceny_hrac = pygame.transform.rotate(hrac, 270)
        if zx < WIDTH - 1:
          animate(zx + 1, zy)
      elif event.key == pygame.K_UP:
        otoceny_hrac = pygame.transform.rotate(hrac, 0)
        if zy > 0:
          animate(zx, zy - 1)
      elif event.key == pygame.K_DOWN:
        otoceny_hrac = pygame.transform.rotate(hrac, 180)
        if zy < HEIGHT - 1:
          animate(zx, zy + 1)
      elif event.key == pygame.K_LEFT:
        otoceny_hrac = pygame.transform.rotate(hrac, 90)
        if zx > 0:
          animate(zx - 1, zy)