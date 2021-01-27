import re
from typing import Callable, List, Optional, Sequence


def split_by(separator: str) -> Callable[[str], List]:
    def func(snake_case_string):
        return snake_case_string.split(separator)
    return func


def concat(separator: Optional[str] = None) -> Callable[[Sequence[str]], str]:
    def func(parts, separator=separator):
        separator = '' if separator is None else separator
        return separator.join(parts)
    return func


def capitalize_each() -> Callable[[Sequence[str]], List[str]]:
    def func(parts: Sequence[str]):
        return [part.capitalize() for part in parts]
    return func


def split_by_regex(regex: str) -> Callable[[str], List[str]]:
    def func(string, regex=regex):
        return list(map(str, re.compile(regex).findall(string)))
    return func


def split_by_camel_case() -> Callable[[str], List[str]]:
    def func(string):
        return split_by_regex('[A-Z][a-z0-9]+')(string)
    return func