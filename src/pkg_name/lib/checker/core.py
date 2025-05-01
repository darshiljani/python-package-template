from enum import Enum, auto
from typing import Any, Iterable, Self

from pkg_name.lib.checker.constants import (
    FAILURE_OUTPUT_MESSAGE_FORMAT,
    SUCCESS_OUTPUT_MESSAGE_FORMAT,
)
from pkg_name.lib.exceptions import CheckerAbort, CheckerSkip
from pkg_name.lib.logger.core import Logger


class Checker:
    class CheckMode(Enum):
        """Enum for check modes."""

        NONE = auto()
        SKIP = auto()
        ABORT = auto()

    def __init__(self) -> None:
        self.logger = Logger()

    def _log_check_success(self: Self, message: str, operator: str, value: Any) -> None:
        formatted_message = SUCCESS_OUTPUT_MESSAGE_FORMAT.format(
            message=message, operator=operator, value=value
        )
        self.logger.success(formatted_message)

    def _log_check_skip(self: Self, message: str, expected: Any, received: Any) -> None:
        formatted_message = FAILURE_OUTPUT_MESSAGE_FORMAT.format(
            check_type="SKIP", message=message, expected=expected, actual=received
        )
        self.logger.info(formatted_message)

    def _log_check_fail(self: Self, message: str, expected: Any, received: Any) -> None:
        formatted_message = FAILURE_OUTPUT_MESSAGE_FORMAT.format(
            check_type="FAIL", message=message, expected=expected, actual=received
        )
        self.logger.error(formatted_message)

    def _handle_failure(self: Self, message: str, expected: Any, received: Any) -> None:
        if self.mode == self.CheckMode.SKIP:
            self._log_check_skip(message=message, expected=expected, received=received)
            raise CheckerSkip(message=message)
        elif self.mode == self.CheckMode.ABORT:
            self._log_check_fail(message=message, expected=expected, received=received)
            raise CheckerAbort(message=message)
        else:
            self._log_check_fail(message=message, expected=expected, received=received)

    def that(self: Self, value: Any, mode: CheckMode = CheckMode.NONE) -> Self:
        self.mode = mode
        self.value = value
        return self

    def equals(self: Self, expected: Any, message: str) -> None:
        self.result = self.value == expected
        if not self.result:
            return self._handle_failure(
                message=message,
                expected=expected,
                received=self.value,
            )
        self._log_check_success(message=message, operator="=", value=expected)

    def not_equals(self: Self, expected: Any, message: str) -> None:
        self.result = self.value != expected
        if not self.result:
            return self._handle_failure(
                message=message,
                expected=expected,
                received=self.value,
            )
        self._log_check_success(message=message, operator="!=", value=expected)

    def is_in(self: Self, expected: Iterable[Any], message: str) -> None:
        self.result = self.value in expected
        if not self.result:
            return self._handle_failure(
                message=message,
                expected=expected,
                received=self.value,
            )

        self._log_check_success(message=message, operator="is in", value=expected)

    def is_less_than(self: Self, expected: Any, message: str) -> None:
        self.result = self.value < expected
        if not self.result:
            return self._handle_failure(
                message=message,
                expected=expected,
                received=self.value,
            )

        self._log_check_success(message=message, operator="<", value=expected)

    def is_less_than_or_equals(self: Self, expected: Any, message: str) -> None:
        self.result = self.value <= expected
        if not self.result:
            return self._handle_failure(
                message=message,
                expected=expected,
                received=self.value,
            )

        self._log_check_success(message=message, operator="<=", value=expected)

    def is_greater_than(self: Self, expected: Any, message: str) -> None:
        self.result = self.value > expected
        if not self.result:
            return self._handle_failure(
                message=message,
                expected=expected,
                received=self.value,
            )

        self._log_check_success(message=message, operator=">", value=expected)

    def is_greater_than_or_equals(self: Self, expected: Any, message: str) -> None:
        self.result = self.value >= expected
        if not self.result:
            return self._handle_failure(
                message=message,
                expected=expected,
                received=self.value,
            )

        self._log_check_success(message=message, operator=">=", value=expected)
