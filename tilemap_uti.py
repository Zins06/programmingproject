import pygame


# reads the tile map layout from the external text file
def read_tilemap_layout(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


# #Loads the tile map layout from the external text file
def load_tilemap_layout(file_path):
    """Load the tilemap layout from a text file."""
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


# Creates a tile map based on the layout
def create_tilemap(tilemap_layout, tile_mapping):
    """Create a tilemap based on the layout."""
    tilemap = []
    for row in tilemap_layout:
        print(row)  # Add this line to see the contents of the row
        tilemap_row = [tile_mapping[char] for char in row]
        tilemap.append(tilemap_row)
    return tilemap


# Draws the tile map on the screen
def draw_tilemap(screen, tilemap, tile_mapping, tile_size, camera_offset):
    for row_index, row in enumerate(tilemap):
        for col_index, char in enumerate(row):
            if char in tile_mapping:
                # Calculate the position to draw the tile, considering camera_offset
                x = col_index * tile_size - camera_offset[0]
                y = row_index * tile_size - camera_offset[1]

                # Ensure x and y are within the screen boundaries
                x = max(0, min(x, screen.get_width() - tile_size))
                y = max(0, min(y, screen.get_height() - tile_size))

                # Print tile position for debugging
                print("Tile Position:", x, y)

                # Draw the tile on the screen
                screen.blit(tile_mapping[char], (x, y))





