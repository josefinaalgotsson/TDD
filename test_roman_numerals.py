from roman_numerals import roman_numerals
    
def test_roman_of_I_is_one():
    res = roman_numerals("I")
    assert res == 1
    
def test_roman_of_V_is_five():
    res = roman_numerals("V")
    assert res == 5
    
def test_roman_of_II_is_two():
    res = roman_numerals("II")
    assert res == 2
    
def test_roman_of_III_is_three():
    res = roman_numerals("III")
    assert res == 3
    
def test_roman_of_VI_is_six():
    res = roman_numerals("VI")
    assert res == 6
    
def test_roman_of_IV_is_four():
    res = roman_numerals("IV")
    assert res == 4

def test_roman_of_MMVI_is_2006():
    res = roman_numerals("MMVI")
    assert res == 2006
    
def test_roman_of_MCMXLIV_is_2006():
    res = roman_numerals("MCMXLIV")
    assert res == 1944
    
    


