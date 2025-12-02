import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(10, 4) == 6
    assert calculator.subtract(0, 5) == -5

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("Все тесты прошли!")