import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Konstanta
WIDTH, HEIGHT = 800, 400
FPS = 60
GRAVITY = 0.5

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Bros Sederhana")
clock = pygame.time.Clock()

# Karakter Player
player_size = (40, 60)
player = pygame.Rect(100, HEIGHT - player_size[1] - 50, *player_size)
player_velocity = {"x": 0, "y": 0}
on_ground = False

# Platform
platforms = [
    pygame.Rect(0, HEIGHT - 50, WIDTH, 50),   # Tanah
    pygame.Rect(200, 300, 100, 20),          # Platform pertama
    pygame.Rect(400, 250, 150, 20),          # Platform kedua
]

# Fungsi untuk menggambar
def draw():
    screen.fill(WHITE)  # Background
    pygame.draw.rect(screen, BLUE, player)  # Player
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)  # Platform
    pygame.display.flip()

# Game Loop
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kontrol pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_velocity["x"] = -5
    elif keys[pygame.K_RIGHT]:
        player_velocity["x"] = 5
    else:
        player_velocity["x"] = 0

    if keys[pygame.K_SPACE] and on_ground:
        player_velocity["y"] = -10

    # Fisika
    player_velocity["y"] += GRAVITY
    player.x += player_velocity["x"]
    player.y += player_velocity["y"]

    # Deteksi lantai
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform) and player_velocity["y"] > 0:
            player.bottom = platform.top
            player_velocity["y"] = 0
            on_ground = True

    # Batas layar
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH
    if player.top > HEIGHT:
        player.top = 0  # Reset ke atas jika jatuh

    # Gambar semua objek
    draw()

# Keluar dari Pygame
pygame.quit()
sys.exit()
