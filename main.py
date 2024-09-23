from color_reference.py import ColorReference

def print_color_reference():
    manual = ColorReference.generate_manual()
    print(manual)

if __name__ == "__main__":
    print_color_reference()

