from sys import stderr, stdout
from typing import Self

from pkg_name.lib.logger.constants import (
    BackgroundColor,
    Color,
    Formatters,
    LogLevel,
)


class _LogStyle:
    """Class to encapsulate styles for log levels."""

    def __init__(
        self: Self,
        text_color: Color,
        background_color: BackgroundColor = BackgroundColor.DEFAULT,
        bold: bool = False,
    ):
        self._text_color = text_color
        self._background_color = background_color
        self.bold = bold

    def format_message(self: Self, message: str, sev: LogLevel) -> str:
        """Format the message with the specified styles."""
        bold_prefix = Formatters.BOLD if self.bold else ""
        return (
            f"{bold_prefix}{self._text_color}{sev.name} : {message}{Formatters.RESET}"
        )


class Logger:
    """Logger class to handle different log levels with colors."""

    def __init__(self: Self) -> None:
        self.styles = {
            LogLevel.DEFAULT: _LogStyle(Color.DEFAULT),
            LogLevel.DEBUG: _LogStyle(Color.CYAN),
            LogLevel.INFO: _LogStyle(Color.BLUE),
            LogLevel.WARNING: _LogStyle(Color.YELLOW),
            LogLevel.SUCCESS: _LogStyle(Color.GREEN),
            LogLevel.ERROR: _LogStyle(Color.RED),
            LogLevel.CRITICAL: _LogStyle(Color.MAGENTA, bold=True),
        }
        self._default_style = _LogStyle(Color.DEFAULT)

    def _print_log(self: Self, sev: LogLevel, message: str) -> None:
        """Log a message with the specified log level."""
        style = self.styles.get(sev, self._default_style)
        formatted_message = style.format_message(message, sev)
        output_stream = stderr if sev in [LogLevel.ERROR, LogLevel.CRITICAL] else stdout
        print(formatted_message, file=output_stream, flush=True)

    def log(self: Self, message: str) -> None:
        """Log a message with the default log level."""
        self._print_log(LogLevel.DEFAULT, message)

    def debug(self: Self, message: str) -> None:
        """Log a debug message."""
        self._print_log(LogLevel.DEBUG, message)

    def info(self: Self, message: str) -> None:
        """Log an info message."""
        self._print_log(LogLevel.INFO, message)

    def warn(self: Self, message: str) -> None:
        """Log a warning message."""
        self._print_log(LogLevel.WARNING, message)

    def success(self: Self, message: str) -> None:
        """Log a success message."""
        self._print_log(LogLevel.SUCCESS, message)

    def error(self: Self, message: str) -> None:
        """Log an error message."""
        self._print_log(LogLevel.ERROR, message)

    def critical(self: Self, message: str) -> None:
        """Log a critical message."""
        self._print_log(LogLevel.CRITICAL, message)
