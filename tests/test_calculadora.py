import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculadora import soma, sub, mul, div

import pytest

def test_soma():
    assert soma(2, 3) == 5

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(3, 4) == 12

def test_div():
    assert div(10, 2) == 5

def test_div_zero():
    import pytest
    with pytest.raises(ValueError):
        div(10, 0)
