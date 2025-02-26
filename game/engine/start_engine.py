from game.engine.modules import version as engine_version 

print(f'{engine_version.engine_name} - {engine_version.version}')

from game.engine.modules import initialer
import game.engine.config as config
 
init_score = initialer.init()
if init_score[0] == True:
    if config.sound_level > 0.0:
        pass
    else:
        pass
else:
    if config.sound_level > 0.0:
        config.sound_level <= 0.0
    else:
        config.sound_level == 0.0
if init_score[1] == True:
    pass
else:
    print('!!!WALMEN cannot to init libraries!!!')
    quit()

import game.engine.startscript