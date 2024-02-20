import pygame        # programmed by M.M.@#
import random
pygame.init()

def draw_square(column, row, color):    #Funktion#
    screen_x = column * SQUARE_SIZE
    screen_y = row * SQUARE_SIZE
    pygame.draw.rect(screen, color, (screen_x, screen_y, SQUARE_SIZE, SQUARE_SIZE))

WIN_SIZE = 800                      # Displaygröße  a * b #
SQUARE_COUNT = 50
SQUARE_SIZE = WIN_SIZE / SQUARE_COUNT
START_LENGHT = 6
DELAY = 90

screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
pygame.display.set_caption("SNAKE")         # Überschrift Fenster #

head_column = SQUARE_COUNT // 2
head_row = SQUARE_COUNT // 2
snake_length = START_LENGHT
body_parts = []
step_x = 0                         # geben die Richtung der Schlange an #
step_y = 0
apple_row = random.randint(0, SQUARE_SIZE-1)
apple_column = random.randint(0, SQUARE_SIZE-1)


run = True
while run:
    pygame.time.delay(DELAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if step_x != -1:
         step_x = 1
         step_y = 0
    elif keys[pygame.K_LEFT]:        # elif frag nur 1 punkt / schritt ab'
        if step_x != 1:
         step_x = -1
         step_y = 0
    elif keys[pygame.K_UP]:
       if step_y != 1:
        step_x = 0
        step_y = -1
    elif keys[pygame.K_DOWN]:
       if step_y != -1:
        step_x = 0
        step_y = 1

    if step_x != 0 or step_y != 0:
       body_parts.append((head_column, head_row))  # ab 15:30 im video#
       if len(body_parts) >= snake_length:
           body_parts.pop(0)


    head_column += step_x
    head_row += step_y

    if head_column == apple_column and head_row == apple_row:
        snake_length += 1                                      # lässt die Schlange um 1 wachsen #
        apple_row = random.randint(0, SQUARE_SIZE - 1)
        apple_column = random.randint(0, SQUARE_SIZE - 1)

    self_hit = (head_column, head_row) in body_parts           # TESTS #
    vertical_border_hit = head_column < 0 or head_column >= SQUARE_COUNT
    horizontal_border_hit = head_row < 0 or head_row >= SQUARE_COUNT

    if self_hit or vertical_border_hit or horizontal_border_hit:
       head_column = SQUARE_COUNT // 2
       head_row = SQUARE_COUNT // 2
       snake_length = START_LENGHT
       body_parts = []
       step_x = 0                     # geben die Richtung der Schlange an #
       step_y = 0


    screen.fill((0, 0, 0))           # Farbe RGB für Hintergrund  von 0 - 255  Rot/Grün/Blau #

    draw_square(head_column, head_row, (0, 255, 0))

    for part in body_parts:
        part_column = part[0]
        part_row = part[1]
        draw_square(part_column, part_row, (0, 255, 0))

    draw_square(apple_column, apple_row, (255, 0, 0))

    for i in range(SQUARE_COUNT):
        line_pos = SQUARE_SIZE * i
        pygame.draw.line(screen, (255, 255, 255), (line_pos, 0), (line_pos, WIN_SIZE), 1)
        pygame.draw.line(screen, (255, 255, 255), (0, line_pos), (WIN_SIZE, line_pos), 1)

    pygame.display.update() # Updatet das Fenster #

pygame.display.quit()