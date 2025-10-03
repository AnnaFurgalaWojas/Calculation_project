import pytest
from calculation.Calculation import add_function, divide_function, mean_function

def test_add_function():
    assert add_function(2, 3) == 5
    assert add_function(-1, 1) == 0
    assert add_function(0, 0) == 0
    assert add_function(-1, -1) == -2   
    

def test_divide_function():
    assert divide_function(6, 3) == 2
    assert divide_function(-6, 3) == -2
    assert divide_function(0, 1) == 0
    with pytest.raises(ValueError):
        divide_function(1, 0)
    with pytest.raises(ValueError):
        divide_function('a', 1)

def test_mean_function():
    assert mean_function([1, 2, 3, 4, 5]) == 3
    assert mean_function([-1, 1]) == 0
    assert mean_function([0, 0, 0]) == 0
    with pytest.raises(ValueError):
        mean_function([])
    with pytest.raises(ValueError):
        mean_function(None)