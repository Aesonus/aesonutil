
from typing import Any, Callable, List, Optional, Sequence, Union


name="aesonutil/aesonutil"
__version__ = "1.0.0"

class MapTo:
    """
    Builds a callable class that attaches decorators to each other to return something.
    """
    def __init__(self, *args: Callable[[Any], Any]):
        """
        Pass in multiple callables that accept one argument and return anything. This callable will
        call each callable in order given with the results of the last callable.
        """
        def func(input):
            result = input
            for func in args:
                result = func(result)
            return result
        self.func = func

    def __call__(self, value) -> Any:
        return self.func(value)