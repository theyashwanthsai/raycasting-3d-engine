import pygame 
import sys
from settings import *
from map import *
from player import *
from raycasting import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(str(self.clock.get_fps()))
        
        
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()
        
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            
            
if __name__ == '__main__':
    game = Game()
    game.run()