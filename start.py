#from game.engine import start_engine
#from game.assets import script

#Это лаунчер
from customtkinter import *
from PIL.ImageTk import PhotoImage
from game.engine import config
from importlib import reload
import pygame
import fileinput

pygame.init()

des = CTk()
des.geometry('1000x600')
des.resizable(False, False)
des.title('WALMEN')

bg_image = PhotoImage(file='game/startassets/launcher/images/bg.png')
bg2_image = PhotoImage(file='game/startassets/launcher/images/bg3.png')
bg3_image = PhotoImage(file='game/startassets/launcher/images/bg2.png')
bg4_image = PhotoImage(file='game/startassets/launcher/images/bg4.png')

while_key = False
register_key = None

tkinter_to_pygame = {
    'a': pygame.K_a,
    'b': pygame.K_b,
    'c': pygame.K_c,
    'd': pygame.K_d,
    'e': pygame.K_e,
    'f': pygame.K_f,
    'g': pygame.K_g,
    'h': pygame.K_h,
    'i': pygame.K_i,
    'j': pygame.K_j,
    'k': pygame.K_k,
    'l': pygame.K_l,
    'm': pygame.K_m,
    'n': pygame.K_n,
    'o': pygame.K_o,
    'p': pygame.K_p,
    'q': pygame.K_q,
    'r': pygame.K_r,
    's': pygame.K_s,
    't': pygame.K_t,
    'u': pygame.K_u,
    'v': pygame.K_v,
    'w': pygame.K_w,
    'x': pygame.K_x,
    'y': pygame.K_y,
    'z': pygame.K_z,
    '0': pygame.K_0,
    '1': pygame.K_1,
    '2': pygame.K_2,
    '3': pygame.K_3,
    '4': pygame.K_4,
    '5': pygame.K_5,
    '6': pygame.K_6,
    '7': pygame.K_7,
    '8': pygame.K_8,
    '9': pygame.K_9,
    
    '\r': pygame.K_RETURN,
    ' ': pygame.K_SPACE,
    '\x08': pygame.K_BACKSPACE,
    '\t': pygame.K_TAB,
    'Escape': pygame.K_ESCAPE,
    'Delete': pygame.K_DELETE,
    'Insert': pygame.K_INSERT,
    'Home': pygame.K_HOME,
    'End': pygame.K_END,
    'PageUp': pygame.K_PAGEUP,
    'PageDown': pygame.K_PAGEDOWN,
    'Left': pygame.K_LEFT,
    'Right': pygame.K_RIGHT,
    'Up': pygame.K_UP,
    'Down': pygame.K_DOWN,
    
    'F1': pygame.K_F1,
    'F2': pygame.K_F2,
    'F3': pygame.K_F3,
    'F4': pygame.K_F4,
    'F5': pygame.K_F5,
    'F6': pygame.K_F6,
    'F7': pygame.K_F7,
    'F8': pygame.K_F8,
    'F9': pygame.K_F9,
    'F10': pygame.K_F10,
    'F11': pygame.K_F11,
    'F12': pygame.K_F12,
    
    'Control_L': pygame.K_LCTRL,
    'Shift_L': pygame.K_LSHIFT,
    'Control_R': pygame.K_RCTRL,
    'Shift_R': pygame.K_RSHIFT,
    'Alt_L': pygame.K_LALT,
    'Alt_R': pygame.K_RALT,
    'Super_L': pygame.K_LMETA,
    'Meta_L': pygame.K_LMETA,
}

bg = CTkLabel(des, image=bg_image, text='')
bg.place(x=0, y=0)

def animation_right():
    x_start = -84

    for i in range(42):
        x_start += 2
        game.place(x=x_start, y=0)
        info.place(x=x_start, y=90)
        close.place(x=x_start,y=500)
        keyboard.place(x=x_start, y=180)
        des.update()
        des.after(1)

def animation_left():
    x_start = 0

    for i in range(42):
        x_start -= 2
        game.place(x=x_start, y=0)
        info.place(x=x_start, y=90)
        close.place(x=x_start,y=500)
        keyboard.place(x=x_start, y=180)
        des.update()
        des.after(1)

    game.place_forget()
    info.place_forget()
    close.place_forget()
    keyboard.place_forget()
    des.update()

def menu():
    play.place_forget()
    close_game_menu.place_forget()
    control_1.place_forget()
    control_2.place_forget()
    control_3.place_forget()
    control_4.place_forget()
    control_5.place_forget()
    control_6.place_forget()
    text_touched.place_forget()
    bg.configure(image=bg_image)
    des.update()
    animation_right()

def game_menu():
    animation_left()
    bg.configure(image=bg2_image)
    play.place(x=550, y=250)
    close_game_menu.place(x=700, y=250)
    des.update()

def info_menu():
    animation_left()
    bg.configure(image=bg3_image)
    close_game_menu.place(x=700, y=250)
    des.update()

def play_game():
    des.destroy()
    pygame.quit()
    from game.engine import start_engine
    #from game.assets import script

def keyboard_menu():
    animation_left()
    bg.configure(image=bg4_image)
    close_game_menu.place(x=800, y=400)
    text_touched.place(x=560,y=420)
    control_1.place(x=70, y=150)
    control_2.place(x=330, y=150)
    control_3.place(x=580, y=150)
    control_4.place(x=820, y=150)
    control_5.place(x=60, y=450)
    control_6.place(x=330, y=450)
    des.update()

def on_key_press(event):
    global register_key
    if event.char == "":
        if tkinter_to_pygame.get(event.keysym) != None:
            register_key = tkinter_to_pygame.get(event.keysym)
    else:
        # Обычная клавиша
        if tkinter_to_pygame.get(event.char) != None:
            register_key = tkinter_to_pygame.get(event.char)
    text_touched.configure(text=f'{pygame.key.name(register_key)}')
    des.update()
    
def while_key_run(key_name, origin_key, key_output):
    global while_key, register_key

    if register_key is None:
        return False

    if key_name == 'key_up':
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'key_up = {origin_key}', f'key_up = {key_output}'), end='')
        reload(config)
        control_1.configure(text=f'{pygame.key.name(config.key_up)}')
    if key_name == 'key_down':
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'key_down = {origin_key}', f'key_down = {key_output}'), end='')
        reload(config)
        control_2.configure(text=f'{pygame.key.name(config.key_down)}')
    if key_name == 'key_left':
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'key_left = {origin_key}', f'key_left = {key_output}'), end='')
        reload(config)
        control_3.configure(text=f'{pygame.key.name(config.key_left)}')
    if key_name == 'key_right':
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'key_right = {origin_key}', f'key_right = {key_output}'), end='')
        reload(config)
        control_4.configure(text=f'{pygame.key.name(config.key_right)}')
    if key_name == 'key_abilities':
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'key_abilities = {origin_key}', f'key_abilities = {key_output}'), end='')
        reload(config)
        control_5.configure(text=f'{pygame.key.name(config.key_abilities)}')
    if key_name == 'key_attack':
        for line in fileinput.input('game/engine/config.py', inplace=True):
            print(line.replace(f'key_attack = {origin_key}', f'key_attack = {key_output}'), end='')
        reload(config)
        control_6.configure(text=f'{pygame.key.name(config.key_attack)}')

game_image = PhotoImage(file='game/startassets/launcher/images/game.png')
game = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', text='', image=game_image, hover_color='grey', command=game_menu)

info_image = PhotoImage(file='game/startassets/launcher/images/info.png')
info = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', text='', image=info_image, hover_color='grey', command=info_menu)

play_image = PhotoImage(file='game/startassets/launcher/images/play.png')
play = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', text='', image=play_image, hover_color='grey', command=play_game)

keyboard_image = PhotoImage(file='game/startassets/launcher/images/keyboard.png')
keyboard = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', text='', image=keyboard_image, hover_color='grey', command=keyboard_menu)
control_1 = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', font=('Arial', 35), text=f'{pygame.key.name(config.key_up)}', hover_color='grey', command=lambda: while_key_run('key_up', config.key_up, register_key))
control_2 = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', font=('Arial', 35), text=f'{pygame.key.name(config.key_down)}', hover_color='grey', command=lambda: while_key_run('key_down', config.key_down, register_key))
control_3 = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', font=('Arial', 35), text=f'{pygame.key.name(config.key_left)}', hover_color='grey', command=lambda: while_key_run('key_left', config.key_left, register_key))
control_4 = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', font=('Arial', 35), text=f'{pygame.key.name(config.key_right)}', hover_color='grey', command=lambda: while_key_run('key_right', config.key_right, register_key))
control_5 = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', font=('Arial', 35), text=f'{pygame.key.name(config.key_abilities)}', hover_color='grey', command=lambda: while_key_run('key_abilities', config.key_abilities, register_key))
control_6 = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', font=('Arial', 35), text=f'{pygame.key.name(config.key_attack)}', hover_color='grey', command=lambda: while_key_run('key_attack', config.key_attack, register_key))

text_touched = CTkLabel(des, bg_color='black', width=100, fg_color='black', text_color='white', text='', font=('Arial', 40))

close_image = PhotoImage(file='game/startassets/launcher/images/cls.png')
close = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', text='', image=close_image, hover_color='grey',command=lambda: os._exit(0))

close_game_menu = CTkButton(des, width=84, height=80, bg_color='black', fg_color='black', text='', image=close_image, hover_color='grey',command=menu)

des.after(500, animation_right)

des.bind("<Key>", on_key_press)

des.mainloop()