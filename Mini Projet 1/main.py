# PyGame template.
 
# Import standard modules.
import sys
import os
 
# Import non-standard modules.
import pygame
from pygame.locals import *

# Set up virtual display for Codespaces
os.environ['SDL_VIDEODRIVER'] = 'dummy'

# Sudoku board data
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def update(dt):
  """
  Update game. Called once per frame.
  dt is the amount of time passed since last frame.
  If you want to have constant apparent movement no matter your framerate,
  what you can do is something like
  
  x += v * dt
  
  and this will scale your velocity based on time. Extend as necessary."""
  
  # Go through events that are passed to the script by the window.
  for event in pygame.event.get():
    # We need to handle these events. Initially the only one you'll want to care
    # about is the QUIT event, because if you don't handle it, your game will crash
    # whenever someone tries to exit.
    if event.type == QUIT:
      pygame.quit() # Opposite of pygame.init
      sys.exit() # Not including this line crashes the script on Windows. Possibly
      # on other operating systems too, but I don't know for sure.
    # Handle other events as you wish.
 
def draw(screen):
    """
    Draw things to the window. Called once per frame.
    """
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    
    # Fill the screen with white
    screen.fill(WHITE)
    
    # Draw the Sudoku grid
    cell_size = 60
    grid_size = 9
    grid_width = cell_size * grid_size
    
    # First draw the main 3x3 grid lines (thicker)
    for i in range(4):
        pygame.draw.line(screen, BLACK, (i * cell_size * 3, 0), (i * cell_size * 3, grid_width), 4)  # Vertical
        pygame.draw.line(screen, BLACK, (0, i * cell_size * 3), (grid_width, i * cell_size * 3), 4)  # Horizontal

    # Then draw the smaller cell lines
    for i in range(10):
        if i % 3 != 0:  # Skip where we already drew the thick lines
            pygame.draw.line(screen, GRAY, (i * cell_size, 0), (i * cell_size, grid_width), 1)  # Vertical
            pygame.draw.line(screen, GRAY, (0, i * cell_size), (grid_width, i * cell_size), 1)  # Horizontal
    
    # Draw numbers
    for i in range(grid_size):
        for j in range(grid_size):
            if board[i][j] != 0:
                x = j * cell_size
                y = i * cell_size
                font = pygame.font.Font(None, 40)
                number = font.render(str(board[i][j]), True, BLACK)
                number_rect = number.get_rect(center=(x + cell_size//2, y + cell_size//2))
                screen.blit(number, number_rect)
    
    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()
    
    # Save a screenshot of the current frame
    pygame.image.save(screen, "Mini Projet 1/pygame_screenshot.png")
 
def runPyGame():
  # Initialise PyGame.
  pygame.init()
  
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
  fps = 60.0
  fpsClock = pygame.time.Clock()
  
  # Set up the window.
  width, height = 1080, 720
  screen = pygame.display.set_mode((width, height))
  
  # screen is the surface representing the window.
  # PyGame surfaces can be thought of as screen sections that you can draw onto.
  # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
  
  # Main game loop.
  dt = 1/fps # dt is the time since last frame.
  while True: # Loop forever!
    try:
        update(dt) # You can update/draw here, I've just moved the code for neatness.
        draw(screen)
        dt = fpsClock.tick(fps)

    except KeyboardInterrupt:
        pygame.quit() # Opposite of pygame.init
        sys.exit() # Not including this line crashes the script on Windows. Possibly



if __name__ == "__main__":
    runPyGame()