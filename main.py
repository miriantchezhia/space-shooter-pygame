            laser.move()
            laser.draw(screen)
            if laser.rect.bottom < 0:
                lasers.remove(laser)
                continue
            for enemy in enemies[:]:
                if laser.rect.colliderect(enemy.rect):
                    if laser in lasers:
                        lasers.remove(laser)
                    if enemy.hit():
                        enemies.remove(enemy)
                    break
        for enemy in enemies:
            enemy.move()
            enemy.draw(screen)
            enemy.display_health(screen)
        if not enemies and player.rect.top <= 0:
            if level < max_level:
                level += 1
                player.rect.center = (screen_width // 2, screen_height - 50)
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
                break
        player.draw(screen)
        display_level(level)
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()
