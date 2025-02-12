import pytest

def replace_numbers(input_list):
    result = []
    previous_num = None
    for i, num in enumerate(input_list):
        if num == 9:
            result.extend([10, 10])
        elif num == 2:
            if previous_num is not None:
                result.extend([1] * previous_num)
        elif num == 6:
            if previous_num is not None and i + previous_num < len(input_list):
                result.extend([3] * input_list[i + previous_num])
        else:
            result.append(num)
        previous_num = num
    return result

def test_replace_nines():
    # not working because this is 1st iteration
    # FAILS
    input_list = [1, 3, 4, 5, 7, 8, 9, 10]
    expected_output = [1, 3, 4, 5, 7, 8, 10, 10, 10]
    assert replace_numbers(input_list) == expected_output

def test_replace_twos():
    input_list = [3, 2, 3, 4, 5]
    expected_output = [3, 1, 1, 1, 3, 4, 5]
    assert replace_numbers(input_list) == expected_output

def test_replace_combined():
    # FAILS
    input_list = [1, 9, 2, 2, 3]
    expected_output = [1, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
    assert replace_numbers(input_list) == expected_output

def test_replace_sixes():
    input_list = [1, 6, 3, 4, 5]
    expected_output = [1, 3, 3, 3, 3, 4, 5]
    assert replace_numbers(input_list) == expected_output


def test_with_2_at_the_beginning():
    input_list = [2, 5, 6, 3, 9]
    expected_output = [5, 3, 10, 10]  # Correct expected output
    assert replace_numbers(input_list) == expected_output

