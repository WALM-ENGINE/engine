def init():

    init_score = []

    from game.engine.modules import audio
    if audio.init() == True:
        init_score.append(True)
    else:
        init_score.append(False)

    from game.engine.modules import fileloader
    if fileloader.init() == True:
        init_score.append(True)
    else:
        init_score.append(False)

    return init_score