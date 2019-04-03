from blatt0 import pascal
from blatt0 import is_palindrome
from blatt0 import flatten
from blatt0 import fizz_buzz
from blatt0 import solve_equation
from blatt0 import myint
from blatt0 import mybin
import random

def test_is_palindrome():
    input = "abba"
    assert is_palindrome(input) == True

def test_is_palindrome2():
    input = "abxa"
    assert is_palindrome(input) == False

#@pytest.mark.fail um Test zu failen

def test_pascal():
    assert  [1] == pascal(0)

def test_pascal1():
    assert[1,1] == pascal(1)

def test_pascal2():
    assert [1,4,6,4,1] == pascal(4)

def test_flatten():
    assert ['a',1,2] == flatten(['a',1,2])

def test_flatten2():
    assert [1,2,1,2] == flatten([[1,2],1,2])

def test_flatten3():
    assert [1,2,2,3,4,1,2] == flatten([[1,2,[2,3,4]],1,2])

def test_fizz_buzz():
    assert [1] == fizz_buzz(1)

def test_fizz_buzz2():
    assert [1,2,"fizz",4] == fizz_buzz(4)

def test_fizz_buzz3():
    assert [1,2,"fizz",4,"buzz"] == fizz_buzz(5)

def test_fizz_buzz4():
    assert [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz"] == fizz_buzz(10)

def test_fizz_buzz5():
    assert [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11,"fizz",13,14,"fizzbuzz"] == fizz_buzz(15)

def test_solve_equation():
    assert [0] == solve_equation(2, 0, 0)

def test_solve_equation1():
    assert [] == solve_equation(2, 0, 8)

def test_solve_equation2():
    assert [3, -3] == solve_equation(1, 0, -9)

def test_solve_equation3():
    assert [0, -9] == solve_equation(1, 9, 0)

def test_solve_equation4():
    assert [1, 3] == solve_equation(2, -8, 6)

def test_int_to_bin():
    input = random.sample(range(1000), 10)
    for x in input:
        assert mybin(x) == bin(x)

def test_bin_to_int():
    input = [(i, bin(i)) for i in random.sample(range(1000), 10)]
    for i, bini in input:
        assert myint(bini) == i

def test_int_to_bin1():
    assert "0b1" == mybin(1)

def test_int_to_bin2():
    assert "0b0" == mybin(0)

def test_int_to_bin3():
    assert "0b10" == mybin(2)

def test_int_to_bin4():
    assert "-0b10" == mybin(-2)