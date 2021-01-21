
from typing import Callable, List, Optional, Sequence


def split_by(separator: str) -> Callable[[str], List]:
    def func(snake_case_string):
        return snake_case_string.split(separator)
    return func


def concat(separator: Optional[str] = None) -> Callable[[Sequence[str]], List]:
    def func(parts, separator=separator):
        separator = '' if separator is None else separator
        return separator.join(parts)
    return func


def capitalize_each() -> Callable[[Sequence[str]], List]:
    def func(parts: Sequence[str]):
        return [part.capitalize() for part in parts]
    return func