def replace_nines(input_list):
    result = []
    for num in input_list:
        if num == 9:
            result.extend([10, 10])
        else:
            result.append(num)
    return result

def test_replace_nines():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10]
    assert replace_nines(input_list) == expected_output