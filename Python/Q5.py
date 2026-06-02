def show_coordinates(coords):
    if len(coords) != 2:
        return "Invalid coordinates"
    x, y = coords
    print(f"X = {x}, Y = {y}")

show_coordinates((10, 20))
