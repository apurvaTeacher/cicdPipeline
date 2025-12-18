import app

def test_add():
    assert app.add(3, 3) == 6

def test_multiply():
    assert app.multiply(3, 3) == 9

def test_subtract():
    assert app.sub(10, 3) == 7
