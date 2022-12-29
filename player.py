from settings import *
import pygame
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED*self.game.delta_time
        speed_sin = speed*sin_a
        speed_cos = speed*cos_a
        
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
            
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
            
        if keys[pygame.K_a]:
            dx += speed_cos
            dy += -speed_sin 
            
        if keys[pygame.K_d]:
            dx += -speed_cos
            dy += speed_sin
            
        # self.x += dx
        # self.y += dy
        
        self.check_wall_collision(dx, dy)
        
        
        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED*self.game.delta_time
            
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED*self.game.delta_time
            
        self.angle %= math.tau
        
        
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
            if self.check_wall(int(self.x + dx), int(self.y)):
                self.x += dx
            if self.check_wall(int(self.x), int(self.y + dy)):
                self.y += dy
        
    def draw(self):
        # pygame.draw.line(self.game.screen, 'yellow', (self.x*100, self.y*100), (self.x*100 + WIDTH*math.cos(self.angle), self.y*100 + WIDTH*math.sin(self.angle)), 2) 
        
        pygame.draw.circle(self.game.screen, 'green', (self.x*100, self.y*100), 15)
    
    def update(self):
        self.movement()
        
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)