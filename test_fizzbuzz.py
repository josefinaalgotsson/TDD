from fizzbuzz import fizzbuzz #testar att den finns

def test_fizzbuzz_returns_something(): #denna kan tas bort eftersom den andra gör samma
    res = fizzbuzz(1)
    assert res is not None
    
def test_fizzbuzz_of_one_is_one():
    res = fizzbuzz(1)
    assert res == 1
    
def test_fizzbuzz_of_two_is_two():
    res = fizzbuzz(2)
    assert res == 2
    
def test_fizzbuzz_of_three_is_fizz():
    for number in [3,6,9]:
        res = fizzbuzz(number)
        assert res == "fizz"
    
def test_fizzbuzz_of_five_is_buzz():
    res = fizzbuzz(5)
    assert res == "buzz"
    
def test_fizzbuzz_of_ten_is_buzz():
    res = fizzbuzz(10)
    assert res == "buzz"
    
def test_fizzbuzz_of_fifteen_is_fizzbuzz():
    res = fizzbuzz(15)
    assert res == "fizzbuzz"


    

    
