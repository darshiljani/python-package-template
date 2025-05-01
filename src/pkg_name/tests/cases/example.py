from typing import Self

from pkg_name.lib import Test


class ExampleTest(Test):
    @staticmethod
    def name() -> str:
        return "Example Test"

    def test(self):
        self.check.that(1).equals(1, "Example check")

        self.check.that(1).equals(2, "Example check")
