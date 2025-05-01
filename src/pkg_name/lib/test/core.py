from abc import ABC, abstractmethod

from pkg_name.lib.checker import Checker
from pkg_name.lib.logger import Logger


class Test(ABC):
    def __init__(self) -> None:
        self.check = Checker()
        self.logger = Logger()

    @staticmethod
    @abstractmethod
    def name() -> str: ...

    @abstractmethod
    def test(self) -> None: ...

    def execute(self) -> None:
        try:
            self.test()
        finally:
            if self.__is_cleanup_required:
                self.logger.debug("Cleaning up test environment")
                self.clean_up()

    @property
    def __is_cleanup_required(self) -> bool:
        return self.clean_up is not Test.clean_up

    def clean_up(self) -> None:
        pass
