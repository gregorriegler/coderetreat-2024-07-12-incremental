import pytest

def replace_numbers(input_list):
    result = []
    i = 0
    while i < len(input_list):
        num = input_list[i]
        if num == 9:
            result.extend([10, 10])
        elif num == 2:
            previous_num = result[-1] if result else None
            if previous_num is not None:
                result.extend([1] * previous_num)
        elif num == 6:
            if i > 0 and i < len(input_list) - 1:
                steps_to_right = input_list[i-1]
                if i + steps_to_right < len(input_list):
                    target_value = input_list[i + steps_to_right]
                    result.extend([3] * target_value)
                else:
                    result.append(num)
            else:
                result.append(num)
        else:
            result.append(num)
        i += 1
    return result

def test_replace_nines():
    input_list = [1, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = [1, 3, 4, 5, 3, 3, 3, 3, 3, 3, 7, 8, 10, 10, 10]
    assert replace_numbers(input_list) == expected_output

def test_replace_twos():
    input_list = [3, 2, 3, 4, 5]
    expected_output = [3, 1, 1, 1, 3, 4, 5]
    assert replace_numbers(input_list) == expected_output

def test_replace_sixes():
    input_list = [1, 6, 3, 4, 5]
    expected_output = [1, 3, 3, 3, 3, 4, 5]
    assert replace_numbers(input_list) == expected_output

def test_replace_combined():
    input_list = [1, 9, 2, 2, 3]
    expected_output = [1, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3]
    assert replace_numbers(input_list) == expected_output

def test_replace_sixes_complex():
    input_list = [2, 6, 3, 2, 1, 6, 2, 5]
    expected_output = [2, 3, 3, 3, 2, 1, 3, 3, 5]
    assert replace_numbers(input_list) == expected_output

if __name__ == "__main__":
    pytest.main()
