
def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []

    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_index = i * 5 + j
            color_pair = (color_index, major, minor)
            color_map.append(color_pair)

    return color_map

def print_color_map(color_map):
    for color_pair in color_map:
        print(f'{color_pair[0]:2d} | {color_pair[1]:6s} | {color_pair[2]:6s}')

color_map = generate_color_map()
print_color_map(color_map)
