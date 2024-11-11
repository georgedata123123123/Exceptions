from pytest import mark, raises
from try_exception import main
from squared_ex import squaredd
from mid_arifmetic import mid_arif
from generator_random_numeric import random_generator

def test_main_pos():
    assert main() == "GOOGLE.RU"

def test_sq_exc_pos(capsys):
    squaredd(1, 1, 0)
    captured = capsys.readouterr()
    assert captured.out == 'Ответ: 0.0, -1.0\n'

@mark.parametrize("exceptions, a, b, c",
                  [(ValueError, 100, 1, 100),
                  (ZeroDivisionError, 0, 10, 10),
                  (Exception, 'f', 1, 2)])
def test_squaredd_exc_neg(exceptions, a, b, c):
    with raises(exceptions):
        squaredd(a, b, c)


def test_mid_arif_raise():
    assert mid_arif(1) == "Используйте другой тип данных(list)"

def test_mid_arif_real():
    assert mid_arif([1, 2, 3, 4, 5, 6]) == f"Среднее арифметическое: {21/6}"


def test_generator_neg():
    with raises(ValueError):
        assert random_generator(-3, 5)

def test_generator_pos():
    c = random_generator(3, 6)
    assert (c in [3, 4, 5, 6]) == True