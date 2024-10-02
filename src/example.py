"""Module docstring."""

from typing import Any


class Example:
    """Example class docstring."""

    def __init__(self, variable: Any = None) -> None:
        self.variable = variable

    def function(self, *args: Any, **kwargs: Any) -> int:
        """Function docstring.

        Returns:
            int: Number of arguments passed
        """
        return len(args) + len(kwargs)
