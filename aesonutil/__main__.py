from aesonutil.mapper import capitalize_each, concat, split_by
from aesonutil import MapTo


ts = 'test_string'

fnc = MapTo(split_by('_'), capitalize_each(), concat())

print(fnc(ts))

tst = [
    'string_1',
    'another_string'
]

print(list(map(fnc, tst)))

print(list(map(split_by('_'), tst)))
