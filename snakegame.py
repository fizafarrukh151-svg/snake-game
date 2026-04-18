import pygame      # graphics, window, keyboard input ke liye
import random      # food ko random jagah rakhne ke liye
import sys         # game se clean exit ke liye

# 1) Pygame ko start karo
pygame.init()

# 2) Window / canvas size define
WIDTH, HEIGHT = 400, 400

# 3) Display window banao (surface jisme draw karte hain)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# 4) Kuch colors define (RGB tuples)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)   # snake color
RED   = (255, 0, 0)   # food color

# 5) Snake ko represent karna:
#   - list of (x, y) cells, jisme index 0 = HEAD
#   - har cell 20x20 ka square hai (grid step)
snake = [(100, 100)]

# 6) Snake ki initial direction (x, y)
#   - (20, 0) ka matlab har frame 20 pixels right move
snake_dir = (20, 0)

# 7) Food ki shuruati position (grid pe hi honi chahiye)
food = (200, 200)

# 8) FPS control (game speed)
clock = pygame.time.Clock()

# 9) Game loop — jab tak quit na ho
while True:
    # --- Events handle karo (close button, key press waghera) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # pygame resources band
            sys.exit()     # program exit

    # --- Keyboard se direction change ---
    keys = pygame.key.get_pressed()

    # Note: reverse turn block kiya gaya hai (upar ja rahe ho to seedha neeche nahi ja sakte)
    if keys[pygame.K_UP] and snake_dir != (0, 20):
        snake_dir = (0, -20)
    if keys[pygame.K_DOWN] and snake_dir != (0, -20):
        snake_dir = (0, 20)
    if keys[pygame.K_LEFT] and snake_dir != (20, 0):
        snake_dir = (-20, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-20, 0):
        snake_dir = (20, 0)

    # --- Snake ko move karna ---
    # new_head = purane head + direction vector
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # head ko front me insert karo
    snake.insert(0, new_head)

    # --- Food check ---
    # agar head bilkul food pe aa gaya to:
    if snake[0] == food:
        # naya food grid pe random jagah
        food = (random.randrange(0, WIDTH, 20), random.randrange(0, HEIGHT, 20))
        # NOTE: yahan body grow hoti hai kyunki hum tail POP nahi kar rahe
    else:
        # warna normal move: tail ko hata do (length same rahe)
        snake.pop()

    # --- Wall collision ya self collision check ---
    if (
        snake[0][0] < 0 or snake[0][0] >= WIDTH  or  # left/right wall
        snake[0][1] < 0 or snake[0][1] >= HEIGHT or  # top/bottom wall
        snake[0] in snake[1:]                        # head body se takraya?
    ):
        pygame.quit()
        sys.exit()

    # --- Drawing / Rendering ---
    win.fill(BLACK)  # background clear karo

    # saray body parts draw karo (20x20 squares)
    for s in snake:
        pygame.draw.rect(win, GREEN, (s[0], s[1], 20, 20))

    # food draw karo
    pygame.draw.rect(win, RED, (food[0], food[1], 20, 20))

    # screen ko update/dikhana
    pygame.display.update()

    # --- Speed control (FPS) ---
    clock.tick(15)  # 10 frames per second ≈ slow/medium speed
