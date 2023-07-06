import pygame

def detect_collision_side(rect1, rect2):
    left = right = bottom = top = False
    if rect1.right >= rect2.left and rect1.left <= rect2.left:
        # Collision on the left side
        left = True
    if rect1.left <= rect2.right and rect1.right >= rect2.right:
        # Collision on the right side
        right = True
    if rect1.bottom >= rect2.top and rect1.top <= rect2.top:
        # Collision on the top side
        top = True
    if rect1.top <= rect2.bottom and rect1.bottom >= rect2.bottom:
        # Collision on the bottom side
        bottom = True
    return left, right, top, bottom


rect1 = pygame.Rect(0, 0, 10, 10)
rect2 = pygame.Rect(5, 5, 10, 10)
left, right, top, bottom = detect_collision_side(rect1, rect2)
print(left, right, top, bottom)

# initialize pygame
pygame.init()

# set up display
screen = pygame.display.set_mode((500, 500))

# set up clock
clock = pygame.time.Clock()

# initialize player position
player_x = 100
player_y = 250
player_velocity = 0

# set up block positions
block_x = 200
block_y = 300
block_width = 100
block_height = 50

# initialize game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update player position
    player_y += player_velocity
    player_velocity += 1

    # check if player is on block
    if player_y + 50 >= block_y and player_y + 50 <= block_y + block_height and player_x + 50 >= block_x and player_x <= block_x + block_width:
        player_y = block_y - 50
        player_velocity = 0

    # clear screen
    screen.fill((255, 255, 255))

    # draw block
    pygame.draw.rect(screen, (0, 0, 0), (block_x, block_y, block_width, block_height))

    # draw player
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 50, 50))

    # update display
    pygame.display.update()

    # limit framerate
    clock.tick(60)

# quit pygame
pygame.quit()