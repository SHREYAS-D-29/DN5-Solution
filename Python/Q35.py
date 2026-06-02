def display_coordinates(coords):
    if len(coords) != 2:
        print("Invalid coordinates")
        return

    print(f"Coordinates: X = {coords[0]}, Y = {coords[1]}")

coordinates = (10, 20)
display_coordinates(coordinates)
