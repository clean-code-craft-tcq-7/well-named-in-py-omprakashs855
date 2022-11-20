from colorCode import ColorCode
global colorCode_Obj

def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'

def color_coding_manual():
    for color_major in colorCode_Obj.MAJOR_COLORS:
        for color_minor in colorCode_Obj.MINOR_COLORS:
            color_coding_number = colorCode_Obj.get_pair_number_from_color(color_major, color_minor)
            print("{} -> {}".format(color_pair_to_string(color_major, color_minor), str(color_coding_number)))

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = colorCode_Obj.get_color_from_pair_number(pair_number)
    assert(major_color == expected_major_color)
    assert(minor_color == expected_minor_color)

def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = colorCode_Obj.get_pair_number_from_color(major_color, minor_color)
    assert(pair_number == expected_pair_number)

if __name__ == '__main__':
    colorCode_Obj = ColorCode()
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    color_coding_manual()
    print('Done :)')