import pygame

def init():
    
    try:
        pygame.mixer.init()
        pygame.quit()
        return True
    except:
        pygame.quit()
        return False
