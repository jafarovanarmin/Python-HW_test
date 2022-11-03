from tud_test import set_keyboard_input, get_display_output
from problem_1 import main

def test_1():
    set_keyboard_input([5, 4])
    main()
    output = get_display_output()
    
    assert output[-1] == "Area: 20.00"
