"""Module docstring."""

from typing import Any


class Example:
    """Example class docstring."""

    def __init__(self, variable: Any = None) -> None:
        """Initialize the Example class."""
        self.variable = variable

    def function(self, *args: Any, **kwargs: Any) -> int:
        """Perform some action.

        Returns:
            int: Number of arguments passed

        """
        return len(args) + len(kwargs)
