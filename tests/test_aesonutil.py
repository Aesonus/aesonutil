from aesonutil import MapTo, chunked


def test_MapTo_call_calls_each_given_callable():
    class CallFixture:
        called1 = False
        called1_with = None
        called2 = False
        called2_with = None

        @classmethod
        def call1(cls, arg):
            cls.called1 = True
            cls.called1_with = arg
            return arg + '_after_one'

        @classmethod
        def call2(cls, arg):
            cls.called2 = True
            cls.called2_with = arg
            return arg + '_after_two'
    test = MapTo(CallFixture.call1, CallFixture.call2)
    test('expected_arg')
    # Expects the functions to be called with the output from initial argument to the last argument
    assert CallFixture.called1 == True
    assert CallFixture.called1_with == 'expected_arg'
    assert CallFixture.called2 == True
    assert CallFixture.called2_with == 'expected_arg_after_one'


def test_chunked_returns_list_split_into_chunks():
    expected = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8]
    ]
    actual = chunked([1, 2, 3, 4, 5, 6, 7, 8], 3)
    assert actual == expected