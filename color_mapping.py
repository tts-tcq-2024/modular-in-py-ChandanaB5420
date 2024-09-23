# color_mapping.py

class ColorMapping:
    major_colors = [
        "White", "Red", "Green", "Brown", "Blue",
        "Black", "Orange", "Yellow", "Slate", "Violet"
    ]

    minor_colors = [
        "White", "Red", "Green", "Brown", "Blue",
        "Black", "Orange", "Yellow", "Slate", "Violet"
    ]

    @staticmethod
    def get_color_pair(pair_number):
        if 1 <= pair_number <= 25:
            major_index = (pair_number - 1) // 5
            minor_index = (pair_number - 1) % 5
            return ColorMapping.major_colors[major_index], ColorMapping.minor_colors[minor_index]
        raise ValueError("Pair number must be between 1 and 25.")

