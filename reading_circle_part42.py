# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: ReadingCircle
class Color:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    DEFAULT = '\033[39m'
    BRIGHT_DEFAULT = '\033[97m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    @staticmethod
    def enable():
        if os.name != 'nt':
            os.environ['ANSI_COLORS'] = '1'
        return True

    @staticmethod
    def disable():
        if os.name != 'nt':
            os.environ['ANSI_COLORS'] = '0'
        return True

    @staticmethod
    def is_enabled():
        return os.environ.get('ANSI_COLORS', '1') == '1'

    @classmethod
    def color(cls, text, color_name):
        if not cls.is_enabled():
            return text
        color_map = {
            cls.RED: cls.RED, cls.GREEN: cls.GREEN, cls.YELLOW: cls.YELLOW,
            cls.BLUE: cls.BLUE, cls.MAGENTA: cls.MAGENTA, cls.CYAN: cls.CYAN,
            cls.WHITE: cls.WHITE, cls.BRIGHT_RED: cls.BRIGHT_RED,
            cls.BRIGHT_GREEN: cls.BRIGHT_GREEN, cls.BRIGHT_YELLOW: cls.BRIGHT_YELLOW,
            cls.BRIGHT_BLUE: cls.BRIGHT_BLUE, cls.BRIGHT_MAGENTA: cls.BRIGHT_MAGENTA,
            cls.BRIGHT_CYAN: cls.BRIGHT_CYAN, cls.BRIGHT_WHITE: cls.BRIGHT_WHITE,
        }
        return color_map.get(color_name, cls.DEFAULT) + text + cls.RESET
