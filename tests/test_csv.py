import pytest
import csv as csv_
from aesonutil import csv
from pathlib import Path

@pytest.fixture
def csv_file(tmpdir: Path):
    tmpfile = tmpdir / 'test.csv'
    with open(str(tmpfile), mode='w', encoding='utf-8', newline='') as csvfile:
        csv_.writer(csvfile).writerows([
            ('test', 'tester'),
            ('42', '84'),
            ('84', '42')
        ])
    return str(tmpfile)

def test_named_tuple_reader(csv_file: Path):
    with open(csv_file, encoding='utf-8', newline='') as csvfile:
        rows = list(csv.NamedTupleReader(csvfile))
    assert rows == [
        ('42', '84'),
        ('84', '42')
    ]