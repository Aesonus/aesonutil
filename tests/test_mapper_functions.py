from typing import Sequence
from aesonutil.mapper import capitalize_each, concat, split_by
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