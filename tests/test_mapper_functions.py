from typing import Sequence
from aesonutil.mapper import apply_to_each, capitalize_each, concat, split_by, split_by_camel_case, split_by_regex
import pytest



@pytest.fixture(params=(['test', 'string'], ('test', 'string')))
def each_method_arg(request):
    return request.param

def test_concat_returns_func_that_joins_using_a_string(each_method_arg: Sequence):
    test = concat('_')
    actual = test(each_method_arg)
    assert actual == 'test_string'


def test_capitalize_each_returns_func_that_capitalizes_each_item_in_sequence(each_method_arg: Sequence):
    test = capitalize_each()
    actual = test(each_method_arg)
    assert ['Test', 'String'] == actual


def test_split_by_returns_func_that_splits_using_a_string():
    test = split_by('_')
    actual = test('test_string')
    assert actual == ['test', 'string']

def test_split_by_regex_returns_func_that_splits_using_a_regex():
    test = split_by_regex('[A-Z][a-z0-9]+')
    actual = test('TestString')
    assert actual == ['Test', 'String']

def test_split_by_camel_case_returns_func_that_splits_using_a_regex():
    test = split_by_camel_case()
    actual = test('TestString')
    assert actual == ['Test', 'String']

def test_apply_to_each():
    called_items = [
        False, False, False
    ]

    def decorated_fnc(item):
        if item != False:
            return False
        return True

    actual = apply_to_each(decorated_fnc)(called_items)
    assert all(actual)