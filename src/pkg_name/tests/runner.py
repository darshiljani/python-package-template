import importlib
import inspect
import pkgutil
import sys
from shutil import get_terminal_size
from typing import List, Optional, Type

from pkg_name.lib import Logger, Test

TEST_MODULE_PREFIX = "pkg_name.tests.cases."


def load_test_module(module_name: str) -> Optional[object]:
    """Dynamically import a test module by name."""
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        return None


def find_test_classes(module: object) -> List[Type[Test]]:
    """Find all test classes that subclass Test."""
    return [
        obj
        for _, obj in inspect.getmembers(module, inspect.isclass)
        if issubclass(obj, Test) and obj is not Test
    ]


def run_tests(test_module: Optional[str] = None) -> None:
    """Run tests using module names instead of file paths."""
    logger: Logger = Logger()
    test_modules: List[str] = []

    if test_module:
        test_modules.append(TEST_MODULE_PREFIX + test_module)
    else:
        # Automatically discover all test modules inside pkg_name.tests.cases
        import pkg_name.tests.cases

        test_modules = [
            TEST_MODULE_PREFIX + name
            for _, name, is_pkg in pkgutil.walk_packages(pkg_name.tests.cases.__path__)
            if not is_pkg
        ]

    for module_name in test_modules:
        module = load_test_module(module_name)
        if module:
            test_classes: List[Type[Test]] = find_test_classes(module)
            for idx, test_class in enumerate(test_classes):
                test_name = test_class.name()
                logger.info(f"Running {test_name}...")
                cols, _ = get_terminal_size()
                print("-" * (cols // 2), "\n")
                test_instance: Test = test_class()
                test_instance.execute()
                logger.success(f"{test_name} completed")


def main() -> None:
    """Entry point for CLI execution."""
    test_module: Optional[str] = sys.argv[1] if len(sys.argv) > 1 else None
    run_tests(test_module)


if __name__ == "__main__":
    main()
