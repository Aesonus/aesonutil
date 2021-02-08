from collections import namedtuple
import csv as csv_
from typing import Any

__all__ = []

class NamedTupleReader(csv_.DictReader):
    def __next__(self):
        dict_ = super().__next__()
        CsvRow = namedtuple('CsvRow', dict_.keys())
        return CsvRow(**dict_)