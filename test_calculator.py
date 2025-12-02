import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(10, 4) == 6
    assert calculator.subtract(0, 5) == -5

def test_addition():
    # Было: assert 1 + 1 == 2
    assert 1 + 1 == 2  # Заведомо неверный результат

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_addition()
    print("Все тесты прошли!")