import os
import sys

if os.path.isdir('game/startassets') == True:
    pass
else:
    quit()


if os.path.isfile('game/startassets/logo_engine.png') == True:
    pass
else:
    quit()

if os.path.isdir('game/startassets/intro') == True:
    if os.path.isfile('game/startassets/intro/logo.mp4') == True:
        pass
else:
    quit()

if os.path.isfile('game/startassets/script.py') == True:
    from game.startassets import script
else:
    quit()