
def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'

def color_coding_manual(colorCode_Obj):
    for color_major in colorCode_Obj.MAJOR_COLORS:
        for color_minor in colorCode_Obj.MINOR_COLORS:
            color_coding_number = colorCode_Obj.get_pair_number_from_color(color_major, color_minor)
            print("{} -> {}".format(color_pair_to_string(color_major, color_minor), str(color_coding_number)))