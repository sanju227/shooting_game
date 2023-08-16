#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the player character
player_width = 50
player_height = 50
player = pygame.Rect(screen_width // 2, screen_height - player_height, player_width, player_height)

# Set up the bullet
bullet_width = 10
bullet_height = 30
bullet = pygame.Rect(0, 0, bullet_width, bullet_height)
bullet_speed = 5
bullet_state = "ready"  # "ready" means the bullet is ready to be fired, "fired" means the bullet is currently moving

# Set up the enemy properties
enemy_width = 50
enemy_height = 50
enemy_speed = 2

# Create a list to hold the enemy objects
enemies = []

def create_enemy():
    enemy = pygame.Rect(random.randint(0, screen_width-enemy_width), 0, enemy_width, enemy_height)
    enemies.append(enemy)

def draw_player():
    pygame.draw.rect(screen, WHITE, player)

def draw_bullet():
    pygame.draw.rect(screen, RED, bullet)

def move_enemies():
    for enemy in enemies:
        enemy.y += enemy_speed

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

def check_collision():
    global bullet_state
    for enemy in enemies:
        if bullet.colliderect(enemy):
            enemies.remove(enemy)
            bullet_state = "ready"

        if enemy.colliderect(player):
            pygame.quit()
            sys.exit()

        if enemy.y > screen_height:
            enemies.remove(enemy)

# Game loop
clock = pygame.time.Clock()
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_state = "fired"
                    bullet.x = player.x + player.width // 2 - bullet.width // 2
                    bullet.y = player.y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < screen_width - player_width:
        player.x += 5

    if bullet_state == "fired":
        bullet.y -= bullet_speed
        if bullet.y <= 0:
            bullet_state = "ready"

    move_enemies()
    draw_enemies()
    check_collision()

    draw_player()
    if bullet_state == "fired":
        draw_bullet()

    if len(enemies) < 5:  # Adjust the maximum number of enemies on the screen as needed
        create_enemy()

    pygame.display.update()
    clock.tick(60)  # Set the desired frame per second (FPS) rate (e.g., 60 FPS)


# In[ ]:




