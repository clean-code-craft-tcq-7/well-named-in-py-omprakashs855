class ColorCode:
    
    def __init__(self):
        self.MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
        self.MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

    def get_color_from_pair_number(self, pair_number):
        zero_based_pair_number = pair_number - 1
        major_index = zero_based_pair_number // len(self.MINOR_COLORS)
        if major_index >= len(self.MAJOR_COLORS):
            raise Exception('Major index out of range')
        minor_index = zero_based_pair_number % len(self.MINOR_COLORS)
        if minor_index >= len(self.MINOR_COLORS):
            raise Exception('Minor index out of range')
        return self.MAJOR_COLORS[major_index], self.MINOR_COLORS[minor_index]

    def get_pair_number_from_color(self, major_color, minor_color):
        try:
            major_index = self.MAJOR_COLORS.index(major_color)
        except ValueError:
            raise Exception('Major index out of range')
        try:
            minor_index = self.MINOR_COLORS.index(minor_color)
        except ValueError:
            raise Exception('Minor index out of range')
        return major_index * len(self.MINOR_COLORS) + minor_index + 1