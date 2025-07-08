import pygame
import random
import math

WIDTH, HEIGHT = 640, 960
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 300

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel_x = random.uniform(-10, 10)
        self.vel_y = random.uniform(-10, 10)
        self.gravity = 0.2
        self.bounce = 0.95

    def update(self):
        if abs(self.vel_x) < 0.05:
            self.vel_x = 0
        if abs(self.vel_y )< 0.05:
            self.vel_y = 0

        self.vel_y += self.gravity

        self.x += self.vel_x
        self.y += self.vel_y

        dx = self.x - CENTER[0]
        dy = self.y - CENTER[1]
        dist = math.hypot(dx, dy)
        if dist + self.radius > RADIUS:
            nx = dx / dist
            ny = dy / dist
            overlap = dist + self.radius - RADIUS
            self.x -= nx * overlap
            self.y -= ny * overlap

            dot = self.vel_x * nx + self.vel_y * ny
            self.vel_x -= 2 * dot * nx
            self.vel_y -= 2 * dot * ny

            self.vel_x *= self.bounce
            self.vel_y *= self.bounce

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)


    def collide_with(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dist = math.hypot(dx, dy)
        min_dist = self.radius + other.radius

        if dist < min_dist and dist != 0:
            nx = dx / dist
            ny = dy / dist

            overlap = 0.5 * (min_dist - dist)
            self.x -= nx * overlap
            self.y -= ny * overlap
            other.x += nx * overlap
            other.y += ny * overlap

            dot1 = self.vel_x * nx + self.vel_y * ny
            dot2 = other.vel_x * nx + other.vel_y * ny

            self.vel_x -= 2 * dot1 * nx
            self.vel_y -= 2 * dot1 * ny
            other.vel_x -= 2 * dot2 * nx
            other.vel_y -= 2 * dot2 * ny

            bounce = 0.95
            self.vel_x *= bounce
            self.vel_y *= bounce
            other.vel_x *= bounce
            other.vel_y *= bounce
