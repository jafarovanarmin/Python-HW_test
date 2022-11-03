import builtins
#import tud_test
from problem_1 import main

input_values = []
print_values = []

def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)

def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)

def get_display_output():
    global print_values
    return print_values

def set_keyboard_input(mocked_inputs):
    global input_values
    
    mock_input_output_start()
    input_values = mocked_inputs

def test_3():
    set_keyboard_input([5, 4.7])
    problem_1.main()

    output = get_display_output()
    
    assert output == ["length:", "width:","Area: 23.50"]
