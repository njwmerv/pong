import pygame
from sys import exit
from random import randint

# Screen Constants
FPS = 60
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
CENTER_LINE_WIDTH = 10

# Player Constants
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 100
PLAYER_VELOCITY = 15

# Ball Constants
BALL_SIZE = 15

# Colour Constants
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
pygame.font.init()
SCORE_FONT = pygame.font.Font('./assets/RubikMonoOne-Regular.ttf', 48)

pygame.display.set_caption('Pong')
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CENTER_LINE = pygame.Rect(SCREEN_WIDTH / 2 - CENTER_LINE_WIDTH / 2, 0, CENTER_LINE_WIDTH, SCREEN_HEIGHT)

# Helpers

def resetBall(aBall, aBallVelocity):
  aBall.x = SCREEN_WIDTH / 2 - BALL_SIZE / 2
  aBall.y = SCREEN_HEIGHT / 2 - BALL_SIZE / 2
  aBallVelocity['x'] = 5 if randint(0, 1) == 1 else -5
  aBallVelocity['y'] = 5 if randint(0, 1) == 1 else -5

def drawWinner(aText):
    draw_text = SCORE_FONT.render(aText, 1, WHITE)
    WINDOW.blit(draw_text, (SCREEN_WIDTH // 2 - draw_text.get_width()//2, SCREEN_HEIGHT // 2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

# Actual Game

def main():
  run = True
  clock = pygame.time.Clock()
  
  P1 = pygame.Rect(SCREEN_WIDTH / 16, SCREEN_HEIGHT / 2 - PLAYER_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)
  P2 = pygame.Rect(SCREEN_WIDTH - SCREEN_WIDTH / 16 - PLAYER_WIDTH, SCREEN_HEIGHT / 2 - PLAYER_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)
  BALL = pygame.Rect(SCREEN_WIDTH / 2 - BALL_SIZE / 2, SCREEN_HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE)
  
  P1Score = 0
  P2Score = 0
  
  BALL_VELOCITY = {
    'x':5 if randint(0, 1) == 1 else -5,
    'y':5 if randint(0, 1) == 1 else -5
  }

  while run:
    clock.tick(FPS)
    
    # Event Handling
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        pygame.quit()
        exit()
  
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
    if BALL.y >= SCREEN_HEIGHT - BALL_SIZE or BALL.y <= 0:
      BALL_VELOCITY['y'] *= -1.1
    if BALL.x >= SCREEN_WIDTH - BALL_SIZE:
      P2Score += 1
      resetBall(BALL, BALL_VELOCITY)
    elif BALL.x <= 0:
      P1Score += 1
      resetBall(BALL, BALL_VELOCITY)
    elif BALL.colliderect(P1) or BALL.colliderect(P2):
      BALL_VELOCITY['x'] *= -1.05
    
    # Game Display
    WINDOW.fill((0, 0, 0))
    pygame.draw.rect(WINDOW, GRAY, CENTER_LINE)
    
    pygame.draw.rect(WINDOW, WHITE, P1)
    pygame.draw.rect(WINDOW, WHITE, P2)
    pygame.draw.rect(WINDOW, WHITE, BALL)
    
    P1ScoreText = SCORE_FONT.render(f'{P1Score:02d}', False, GRAY)
    P2ScoreText = SCORE_FONT.render(f'{P2Score:02d}', False, GRAY)
    WINDOW.blit(P1ScoreText, (SCREEN_WIDTH / 2 + CENTER_LINE_WIDTH / 2 + SCORE_FONT.get_linesize() / 2, SCORE_FONT.get_linesize() / 2))
    WINDOW.blit(P2ScoreText, (SCREEN_WIDTH / 2 - CENTER_LINE_WIDTH / 2 - SCORE_FONT.get_linesize() / 2 - P2ScoreText.get_width(), SCORE_FONT.get_linesize() / 2))
    
    pygame.display.update()
    
    if P1Score >= 10:
      drawWinner('Player 1 wins!')
      break
    elif P2Score >= 10:
      drawWinner('Player 2 wins!')
      break

if __name__ == '__main__':
  main()
