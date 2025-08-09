import pygame
import random
import math
import os

# Initialize Pygame
pygame.init()

# Set fixed window size
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Light, Green Light")
clock = pygame.time.Clock()
FPS = 60

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
FLESH = (255, 200, 150)  # For fallback doll/player head

# Doll properties
doll_x = WIDTH // 2 - 50
doll_y = HEIGHT // 10
doll_width = 100
doll_height = 100

# Player properties
player_x = WIDTH // 2 - 25
player_y = HEIGHT - HEIGHT // 10
player_width = 50
player_height = 50
player_speed = 2

# Obstacle properties
obstacles = []
NUM_OBSTACLES = 15
obstacle_width = 70
obstacle_height = 70

# Game state
is_green_light = True
game_over = False
game_over_reason = ""
win = False
light_switch_time = 0
light_duration = 2000
game_start_time = 0
TIME_LIMIT = 50000  # 50 seconds

# Font
font = pygame.font.SysFont("arial", 48)

# Load images from assets folder
def load_image(filename, size):
    try:
        path = os.path.join("assets", filename)
        if not os.path.exists(path):
            print(f"Warning: Image not found at {path}")
            return None
        img = pygame.image.load(path).convert_alpha()
        scaled_img = pygame.transform.scale(img, size)
        print(f"Loaded {filename} successfully at size {size}")
        return scaled_img
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return None

# Initial image loading
background_img = load_image("background.png", (WIDTH, HEIGHT))
player_img = load_image("player.png", (player_width, player_height))
obstacle_img = load_image("obstacle.png", (obstacle_width, obstacle_height))
doll_green_img = load_image("doll_green.png", (doll_width, doll_height))
doll_red_img = load_image("doll_red.png", (doll_width, doll_height)) or doll_green_img

def create_obstacles():
    global obstacles
    obstacles.clear()
    for _ in range(NUM_OBSTACLES):
        while True:
            x = random.randint(0, WIDTH - obstacle_width)
            y = random.randint(HEIGHT // 4 + 50, HEIGHT - HEIGHT // 10 - obstacle_height)
            obstacle_rect = pygame.Rect(x, y, obstacle_width, obstacle_height)
            doll_rect = pygame.Rect(doll_x, doll_y, doll_width, doll_height)
            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
            if not (obstacle_rect.colliderect(doll_rect) or obstacle_rect.colliderect(player_rect)):
                obstacles.append(obstacle_rect)
                break

def draw_doll(screen, is_green_light):
    if is_green_light and doll_green_img:
        screen.blit(doll_green_img, (doll_x, doll_y))
    elif not is_green_light and doll_red_img:
        screen.blit(doll_red_img, (doll_x, doll_y))
    else:
        doll_color = GREEN if is_green_light else RED
        pygame.draw.rect(screen, BLACK, (doll_x - 2, doll_y + 30 - 2, doll_width + 4, doll_height - 30 + 4))
        pygame.draw.rect(screen, doll_color, (doll_x, doll_y + 30, doll_width, doll_height - 30))
        pygame.draw.circle(screen, BLACK, (doll_x + doll_width // 2, doll_y + 15), 27)
        pygame.draw.circle(screen, FLESH, (doll_x + doll_width // 2, doll_y + 15), 25)
        pygame.draw.circle(screen, BLACK, (doll_x + doll_width // 2 - 10, doll_y + 10), 5)
        pygame.draw.circle(screen, BLACK, (doll_x + doll_width // 2 + 10, doll_y + 10), 5)

def draw_player(screen):
    if player_img:
        screen.blit(player_img, (player_x, player_y))
    else:
        pygame.draw.rect(screen, BLACK, (player_x - 2, player_y + 15 - 2, player_width + 4, player_height - 15 + 4))
        pygame.draw.rect(screen, BLUE, (player_x, player_y + 15, player_width, player_height - 15))
        pygame.draw.circle(screen, BLACK, (player_x + player_width // 2, player_y + 7), 12)
        pygame.draw.circle(screen, FLESH, (player_x + player_width // 2, player_y + 7), 10)

def draw_obstacle(screen, obstacle):
    if obstacle_img:
        screen.blit(obstacle_img, (obstacle.x, obstacle.y))
    else:
        points = [
            (obstacle.x + obstacle_width // 2, obstacle.y),
            (obstacle.x, obstacle.y + obstacle_height),
            (obstacle.x + obstacle_width, obstacle.y + obstacle_height)
        ]
        pygame.draw.polygon(screen, BLACK, [(x - 2, y - 2) for x, y in points])
        pygame.draw.polygon(screen, YELLOW, points)

def setup():
    global player_x, player_y, doll_x, doll_y, is_green_light, game_over, win, light_switch_time, game_over_reason, game_start_time
    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT - HEIGHT // 10
    doll_x = WIDTH // 2 - doll_width // 2
    doll_y = HEIGHT // 10
    is_green_light = True
    game_over = False
    game_over_reason = ""
    win = False
    light_switch_time = pygame.time.get_ticks()
    game_start_time = pygame.time.get_ticks()
    create_obstacles()

def update_loop():
    global player_x, player_y, is_green_light, game_over, win, light_switch_time, light_duration, game_over_reason
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and (game_over or win):
                setup()
            if event.key == pygame.K_ESCAPE:
                return False
    
    if not game_over and not win:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - game_start_time
        if elapsed_time > TIME_LIMIT:
            game_over = True
            game_over_reason = "Time's Up!"
        
        if current_time - light_switch_time > light_duration:
            is_green_light = random.choice([True, False])
            light_switch_time = current_time
            light_duration = random.randint(2000, 5000)
        
        prev_player_x = player_x
        prev_player_y = player_y
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
            player_y += player_speed
        
        if not is_green_light and (player_x != prev_player_x or player_y != prev_player_y):
            game_over = True
            game_over_reason = "Moved During Red Light"
        
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                game_over = True
                game_over_reason = "Hit Obstacle"
                break
        
        if player_y < HEIGHT // 4:
            win = True
    
    # Draw background
    if background_img:
        screen.blit(background_img, (0, 0))
    else:
        screen.fill(GREEN)
    
    # Draw finish line
    pygame.draw.line(screen, WHITE, (0, HEIGHT // 4), (WIDTH, HEIGHT // 4), 5)
    
    # Draw doll
    draw_doll(screen, is_green_light)
    
    # Draw player
    draw_player(screen)
    
    # Draw obstacles
    for obstacle in obstacles:
        draw_obstacle(screen, obstacle)
    
    # Draw timer
    elapsed_time = pygame.time.get_ticks() - game_start_time
    time_left = max(0, math.ceil((TIME_LIMIT - elapsed_time) / 1000))
    timer_text = font.render(f"Time Left: {time_left} s", True, BLACK)
    screen.blit(timer_text, (10, 10))
    
    # Draw game state text
    light_text = font.render("Green Light" if is_green_light else "Red Light", True, BLACK)
    screen.blit(light_text, (WIDTH // 2 - light_text.get_width() // 2, doll_y + doll_height + 20))
    
    if game_over:
        game_over_text = font.render(f"Game Over! {game_over_reason}! Press R to Restart, ESC to Quit", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
    elif win:
        win_text = font.render("You Win! Press R to Restart, ESC to Quit", True, BLACK)
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)
    return True

def main():
    setup()
    running = True
    while running:
        running = update_loop()

if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()