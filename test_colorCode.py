
def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    global cc_Obj
    major_color, minor_color = cc_Obj.get_color_from_pair_number(pair_number)
    assert(major_color == expected_major_color)
    assert(minor_color == expected_minor_color)

def test_pair_to_number(major_color, minor_color, expected_pair_number):
    global cc_Obj
    pair_number = cc_Obj.get_pair_number_from_color(major_color, minor_color)
    assert(pair_number == expected_pair_number)


def test_main(colorCode_Obj):
    global cc_Obj
    cc_Obj = colorCode_Obj
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)