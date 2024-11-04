import pytest
from calculator import calculate

def test_calculate_sub_add():  
    assert calculate(1, 2, '+') == 3  
    assert calculate(2, 1, '-') == 1 
    assert calculate(2, 1, '/') == 2
    assert calculate(2, 1, '*') == 2