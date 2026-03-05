from calculator import add, clear

def test_full_addition_flow():
   
    first_number = 5
    second_number = 3
    result = add(first_number, second_number)
    assert result == 8, f"Expected 8 but got {result}"

def test_clear_after_calculation():

    result = add(10, 5)      
    result = clear()          
    assert result == 0, "Clear should reset result to 0"