import pygame
from pyvidplayer2 import Video

def init():
    pygame.init()
    pygame.font.init()
    return True

def load_image(file, scaleX, scaleY):
    background = pygame.image.load(file)
    background = pygame.transform.scale(background, (scaleX, scaleY))
    return background

def load_icon(file):
    background = pygame.image.load(file)
    return background

def load_video(file, disable_audio):
    if disable_audio == False:
        video = Video(file, use_pygame_audio=True, max_chunks=2, no_audio=disable_audio)
    elif disable_audio == True:
        video = Video(file, max_chunks=2, no_audio=True)
    return video

def load_font(font, size):
    font = pygame.font.Font(font, size)
    return font

def load_text(font, text, color=(255,255,255)):
    text_label = font.render(f'{text}', 1, color)
    return text_label