def replace_nines(input_list):
    result = []
    for num in input_list:
        if num == 9:
            result.extend([10, 10])
        else:
            result.append(num)
    return result

# Example usage:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output_list = replace_nines(input_list)
print(output_list)


def test_bla():
    assert False