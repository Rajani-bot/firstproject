from app import add

def test_add():
    assert add(5, 6) == 11

def test_add_second():
    assert add(6, 11) == 17

def test_add_third():
    assert add(2, 3) == 5