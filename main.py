import pygame
import time   

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")


backgrounds = [
    pygame.transform.scale(pygame.image.load("space.jpg"), (screen_width, screen_height)),
    pygame.transform.scale(pygame.image.load("space_pic_2.jpg"), (screen_width, screen_height)),
    pygame.transform.scale(pygame.image.load("space_pic_3.jpg"), (screen_width, screen_height)),
    pygame.transform.scale(pygame.image.load("space_pic_4.jpg"), (screen_width, screen_height)),
    pygame.transform.scale(pygame.image.load("space_pic_5.jpg"), (screen_width, screen_height)),
        
]


mad_max = pygame.image.load("player.png")
lazer = pygame.image.load("lazer.png")
rictus = pygame.image.load("enemy.png")
lose_image = pygame.image.load("lost.png")
win_image = pygame.image.load("won.jpg")



class MadMax(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = mad_max
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
        self.speed = 3

    def move(self, keys):
        if keys[pygame.K_d] and self.rect.right < screen_width:  
            self.rect.x += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:  
            self.rect.x -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < screen_height:  
            self.rect.y += self.speed
        if keys[pygame.K_w] and self.rect.top > 0: 
            self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Lazer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = lazer
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -7

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)



class Rictus(pygame.sprite.Sprite):
    def __init__(self, x, y, hp):
        super().__init__()
        self.image = rictus
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = -1
        self.speed = 2
        self.health = hp

    def move(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right >= screen_width or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 20  

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def hit(self):
        self.health -= 1
        return self.health <= 0  

    def display_health(self, surface):
        font = pygame.font.Font(None, 24)
        text = font.render(f"HP: {self.health}", True, (255, 0, 0))
        surface.blit(text, (self.rect.x, self.rect.y - 20))



def initialize_enemies(level):
    enemies = []
    if level == 1:
        enemies.append(Rictus(screen_width - 50, 50, 10))
    elif level == 2:
        enemies.append(Rictus(screen_width - 50, 50, 20))
    elif level == 3:
        enemies.append(Rictus(screen_width - 50, 50, 10))
        enemies.append(Rictus(50, 50, 10))
    elif level == 4:
        enemies.append(Rictus(screen_width - 50, 50, 15))
        enemies.append(Rictus(50, 50, 15))
    elif level == 5:
        enemies.append(Rictus(screen_width // 2 - 25, 50, 40))
    return enemies

def display_level(level):
    font = pygame.font.Font(None, 36)  
    text = font.render(f"Level: {level}", True, (255, 255, 255))  
    screen.blit(text, (10, 10))

def start_screen():
    font = pygame.font.Font(None, 48)
    text = font.render("Press Any Button to Start the Game", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False
def pause_menu():
    font = pygame.font.Font(None, 48)
    paused = True
    while paused:
        screen.fill((0, 0, 0))

        text = font.render("Paused", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        screen.blit(text, text_rect)

        button_text = font.render("Main Menu", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(screen_width // 2, screen_height // 2))
        pygame.draw.rect(screen, (255, 0, 0), button_rect.inflate(20, 10))
        screen.blit(button_text, button_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    start_screen()
                    paused = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = False

level = 1
max_level = 5
enemies = initialize_enemies(level)
lasers = []
player = MadMax()
game_running = True


last_shot_time = 0  
shoot_cooldown = 500

start_screen()

while game_running:
    screen.blit(backgrounds[level - 1], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause_menu()

    keys = pygame.key.get_pressed()
    player.move(keys)

    current_time = pygame.time.get_ticks()

    
    if keys[pygame.K_SPACE] and current_time - last_shot_time > shoot_cooldown:
        lasers.append(Lazer(player.rect.centerx, player.rect.top))
        last_shot_time = current_time

    
    for laser in lasers[:]:
        laser.move()
        laser.draw(screen)
        if laser.rect.bottom < 0:
            lasers.remove(laser)

        for enemy in enemies[:]:
            if laser.rect.colliderect(enemy.rect):
                lasers.remove(laser)
                if enemy.hit():
                    enemies.remove(enemy)

    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)
        enemy.display_health(screen)

    if not enemies and player.rect.top <= 0:
        if level < max_level:
            level += 1
            player.rect.center = (screen_width // 2, screen_height - 50)  # Reset player position
            enemies = initialize_enemies(level)
        else:
            win_image_scaled = pygame.transform.scale(win_image, (screen_width, screen_height))
            screen.blit(win_image_scaled, (0, 0))
            pygame.display.update()
            pygame.time.wait(2000)
            game_running = False

    for enemy in enemies:
        if enemy.rect.bottom >= screen_height or enemy.rect.colliderect(player.rect):
            lose_image_scaled = pygame.transform.scale(lose_image, (screen_width, screen_height))
            screen.blit(lose_image_scaled, (0, 0))
            pygame.display.update()
            pygame.time.wait(2000)
            game_running = False

    player.draw(screen)
    display_level(level)

    pygame.display.update()

pygame.quit()
