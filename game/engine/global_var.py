
try:
    from . import _initialized
except ImportError:
    _initialized = False

if not _initialized:
    from game.engine import walmen_engine
    # Код инициализации движка
    engine_root = walmen_engine.Engine()
    _initialized = True
else:
    # Движок уже инициализирован
    pass