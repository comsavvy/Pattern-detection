#!/bin/env python
import re


def rearrange_name(n: str):
    pattern = r"(?P<sur>[\[\w'.\]]+) (?P<first>[\w.]+) ?(?P<second>[A-Za-z.]*)?"
    result = re.sub(pattern, lambda ptrn: " ".join(ptrn.group('first', 'sur', 'second')), n, flags=re.M)
    return result.title()


def is_valid_variable(n: str):
    pattern = r"^[_a-zA-Z][\w]+$"
    result = re.search(pattern, n)
    return result is not None


name = """gbenga oladele wamiwa
         olusola timothy ogundepo
"""

for i in (i.strip() for i in rearrange_name(name).splitlines()):
    print(i)
