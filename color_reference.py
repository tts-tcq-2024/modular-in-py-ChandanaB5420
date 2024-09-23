# color_reference.py

from color_mapping import ColorMapping

class ColorReference:
    @staticmethod
    def generate_manual():
        manual = "Color Code Reference Manual\n"
        manual += "=" * 30 + "\n"
        for pair_number in range(1, 26):
            major, minor = ColorMapping.get_color_pair(pair_number)
            manual += f"Pair {pair_number}: Major Color - {major}, Minor Color - {minor}\n"
        return manual
