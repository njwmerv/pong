import os
import pygame

# Screen Constants
FPS = 60
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576

# Player Constants
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 100
PLAYER_VELOCITY = 15

# Ball Constants
BALL_SIZE = 15

# Colour Constants
WHITE = (255, 255, 255)

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# Helpers



# Actual Game

def main():
  run = True
  clock = pygame.time.Clock()
  
  P1 = pygame.Rect(SCREEN_WIDTH / 16, SCREEN_HEIGHT / 2 - PLAYER_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)
  P2 = pygame.Rect(SCREEN_WIDTH - SCREEN_WIDTH / 10, SCREEN_HEIGHT / 2 - PLAYER_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)
  BALL = pygame.Rect(SCREEN_WIDTH / 2 - BALL_SIZE / 2, SCREEN_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE)
  
  P1Score = 0
  P2Score = 0
  
  BALL_VELOCITY = {
    'x':5,
    'y':5
  }

  while run:
    clock.tick(FPS)
    
    # Event Handling
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
  
    # Input Handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and P1.y - PLAYER_VELOCITY >= 0:
      P1.y -= PLAYER_VELOCITY
    elif keys[pygame.K_w]:
      P1.y = 0
    elif keys[pygame.K_s] and P1.y + PLAYER_HEIGHT + PLAYER_VELOCITY <= SCREEN_HEIGHT:
      P1.y += PLAYER_VELOCITY
    elif keys[pygame.K_s]:
      P1.y = SCREEN_HEIGHT - PLAYER_HEIGHT
    
    if keys[pygame.K_UP] and P2.y - PLAYER_VELOCITY >= 0:
      P2.y -= PLAYER_VELOCITY
    elif keys[pygame.K_UP]:
      P2.y = 0
    elif keys[pygame.K_DOWN] and P2.y + PLAYER_HEIGHT + PLAYER_VELOCITY <= SCREEN_HEIGHT:
      P2.y += PLAYER_VELOCITY
    elif keys[pygame.K_DOWN]:
      P2.y = SCREEN_HEIGHT - PLAYER_HEIGHT
      
    BALL.x += BALL_VELOCITY['x']
    BALL.y += BALL_VELOCITY['y']
    if BALL.x >= SCREEN_WIDTH - BALL_SIZE or BALL.x <= 0:
      BALL_VELOCITY['x'] *= -1
    if BALL.y >= SCREEN_HEIGHT - BALL_SIZE or BALL.y <= 0:
      BALL_VELOCITY['y'] *= -1
    
    # Game Display
    WINDOW.fill((0, 0, 0))
    
    pygame.draw.rect(WINDOW, WHITE, P1)
    pygame.draw.rect(WINDOW, WHITE, P2)
    pygame.draw.rect(WINDOW, WHITE, BALL)
    
    pygame.display.update()

if __name__ == "__main__":
    main()
pygame.quit()
