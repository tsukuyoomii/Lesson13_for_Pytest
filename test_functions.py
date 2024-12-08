from functions import salary,hello_who

def test_hello_who_other():
    assert hello_who('Max') == 'Hello,Max'
    assert hello_who('Igor') == 'Hello,Igor'
    assert hello_who('Arseniy') == 'Hello,Arseniy'
    assert hello_who('Georgiy') == 'Hello,Georgiy'

def test_salary():
    assert salary(2, 2) != 8
    assert salary(3, 1) != 6