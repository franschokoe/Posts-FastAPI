from app.calculations import add
import pytest

@pytest.mark.parametrize("num1 , num2 , expected" , [
    (3,2,5),
    (1,2,3),
    (6,6,12),
])
def test_add(num1 , num2 , expected):
    assert  add(num1 ,num2) == expected

