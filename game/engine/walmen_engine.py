import math
import pygame
import fileinput
import importlib
#from game.engine.modules import audio
from game.engine.modules import fileloader
from game.engine import config 
from game.assets import lang
import os, sys, time
from threading import Thread
from game.engine.modules import technology

class Engine:
    def __init__(self):

        #audio.init()
        pygame.init()
        fileloader.init()

        pygame.display.set_caption(config.window_name)
        pygame.display.set_icon(fileloader.load_icon(config.icon))
        
        pygame.mixer.init()

        self.walmen_audio = pygame.mixer.music
        self.audio = pygame.mixer.music

        self.MUSIC_END = pygame.USEREVENT+1
        self.audio.set_endevent(self.MUSIC_END)

        self.walmen_const = pygame
        self.walmen_config = config
        self.walmen_language = lang
        self.DOUBLEBUF = pygame.DOUBLEBUF

        self.walmen_time = time
        self.walmen_os = os
        self.walmen_thread = Thread
        self.walmen_technology = technology

        self.width_native=config.width_native
        self.height_native=config.height_native
        self.fps_timer=pygame.time.Clock()
        self.fps=config.fps
        self.vsync=config.vsync
        self.enable_fullscreen=config.enable_fullscreen
        self.sound_level = config.sound_level
        self.screenfetch=pygame.display.Info()

        if self.enable_fullscreen == True:
            self.screen = pygame.display.set_mode((self.screenfetch.current_w,self.screenfetch.current_w), flags=pygame.FULLSCREEN | self.DOUBLEBUF, vsync=self.vsync)
        if self.enable_fullscreen == False:
            self.screen = pygame.display.set_mode((self.width_native,self.height_native), pygame.RESIZABLE | self.DOUBLEBUF, vsync=self.vsync)

        self.audio.set_volume(self.sound_level)

        self.current_size_window = self.screen.get_size()
        self.last_size_window = self.current_size_window
        self.virtual_surface = pygame.Surface((self.width_native,self.height_native))

    def turn_fullscreen(self, mode: False):
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'enable_fullscreen={config.enable_fullscreen}', f'enable_fullscreen={mode}'), end='')
        importlib.reload(config)
        self.enable_fullscreen = config.enable_fullscreen

    def volume_up(self):
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'sound_level = 0.0', f'sound_level = 100.0'), end='')
        self.audio.set_volume(100.0)
        importlib.reload(config)
        self.sound_level = config.sound_level

    def volume_down(self):
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'sound_level = 100.0', 'sound_level = 0.0'), end='')
        self.audio.set_volume(0.0)
        importlib.reload(config)
        self.sound_level = config.sound_level

    def speak_up(self):
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'enable_speak = {config.enable_speak}', f'enable_speak = True'), end='')
        importlib.reload(config)

    def speak_down(self):
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'enable_speak = {config.enable_speak}', 'enable_speak = False'), end='')
        importlib.reload(config)

    def change_lang(self, lang_change):
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f"language = '{config.language}'", f"language = '{lang_change}'"), end='')
        importlib.reload(config)
        importlib.reload(lang)

    def update_screen(self):
        self.scaled_surface = pygame.transform.scale(self.virtual_surface, self.current_size_window)
        self.screen.blit(self.scaled_surface, (0,0))
        self.fps_timer.tick(self.fps)
        self.virtual_surface.fill('black')
        pygame.display.flip()

    def update_teck_screen(self):
        self.scaled_surface = pygame.transform.scale(self.virtual_surface, self.current_size_window)
        self.screen.blit(self.scaled_surface, (0,0))
        self.fps_timer.tick(self.fps)
        pygame.display.flip()

    def load_font(self, font, size):
        return fileloader.load_font(font, size)
    
    def load_text(self, font, text, color=(255,255,255)):
        return fileloader.load_text(font, text, color)

    def load_image(self, file, ScaleX, ScaleY):
        return fileloader.load_image(file, ScaleX, ScaleY)

    def draw(self, source, x, y):
        self.virtual_surface.blit(source, (x, y))

    def display_mod(self, mod):
        self.screen = pygame.display.set_mode((self.width_native,self.height_native), flags=mod | self.DOUBLEBUF, vsync=self.vsync)

    def display_reinit(self):
        self.virtual_surface = pygame.Surface((self.width_native,self.height_native))
        if self.enable_fullscreen == True:
            self.screen = pygame.display.set_mode((self.screenfetch.current_w,self.screenfetch.current_w), flags=pygame.FULLSCREEN | self.DOUBLEBUF, vsync=self.vsync)
        if self.enable_fullscreen == False:
            self.screen = pygame.display.set_mode((self.width_native,self.height_native), pygame.RESIZABLE | self.DOUBLEBUF, vsync=self.vsync)

    def draw_engine_logo(self):
        self.screen.blit(pygame.transform.scale(pygame.image.load('game/startassets/logo_engine.png'), (self.width_native, self.height_native)), (0,0))
        pygame.display.flip()

    def video_load(self, path, disable_audio):
        return fileloader.load_video(path, disable_audio)

    def exit(self):
        pygame.quit()
        os._exit(0)

    def set_resize_window(self, size):
        self.current_size_window = size

    def moding_virtual_screen(self, mod):
        if mod == 'default':
            self.virtual_surface = pygame.Surface((self.width_native,self.height_native))
        else:
            self.virtual_surface = self.walmen_const.Surface((mod))
