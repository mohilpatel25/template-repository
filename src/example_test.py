"""Tests for example module."""

from typing import Any

import pytest

from src import example


class TestExample:
    """Testcases for Example class"""

    def test_init(self) -> None:
        """Test init."""

        obj = example.Example("test_variable")
        assert obj.variable == "test_variable"

    @pytest.mark.parametrize(
        "args,kwargs,expected_num_args",
        [
            ((1, 2, "A"), {}, 3),
            ((), {"A": "A"}, 1),
            (("A", "B"), {"a": "a"}, 3),
            (("A", "B"), {}, 2),
        ],
    )
    def test_function(self, args: Any, kwargs: Any, expected_num_args: int) -> None:
        """Test function."""

        obj = example.Example()
        num_args = obj.function(*args, **kwargs)
        assert num_args == expected_num_args
