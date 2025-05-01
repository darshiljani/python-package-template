from enum import IntEnum, StrEnum, auto


class Formatters(StrEnum):
    """Utility class to provide ANSI escape codes for text formatting."""

    # ANSI escape codes for text formatting
    RESET = "\033[0m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSED = "\033[7m"
    CONCEALED = "\033[8m"
    STRIKETHROUGH = "\033[9m"


class Color(StrEnum):
    """Utility class to provide ANSI escape codes for colors."""

    # ANSI escape codes for text colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    DEFAULT = "\033[39m"


class BackgroundColor(StrEnum):
    """Utility class to provide ANSI escape codes for background colors."""

    # ANSI escape codes for background colors
    BLACK = "\033[40m"
    RED = "\033[41m"
    GREEN = "\033[42m"
    YELLOW = "\033[43m"
    BLUE = "\033[44m"
    MAGENTA = "\033[45m"
    CYAN = "\033[46m"
    WHITE = "\033[47m"
    DEFAULT = "\033[49m"


class LogLevel(IntEnum):
    """Enumeration for log levels."""

    DEFAULT = auto()
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    SUCCESS = auto()
    ERROR = auto()
    CRITICAL = auto()
